# -----------------------------------------------------------
# virtual_screenings.py
# A python script for simulating attractors from random perturbation of FVS nodes using SFA algorithm
# 
# Requires user specification of the undesired initial state to calculate direction of activity change and the suffix of file containing basal perturbations
#
# INPUTS:
# 1. Network as a .sif file
# 2. List of FVS nodes
# 3. Randomly generated perturbations of FVS set
# 4. Activation values for FVS nodes
#
# OUTPUTS:
# 1. attr_logss.txt: a dataframe containing the log steady state values of each network node for all simulated attractors 
# 2. attr_logss_disc.txt: a dataframe containing the discretized log steady state values of each network node for all simulated attractors
# 3. attr_DAC.txt: a dataframe containing the calculated direction of activity change (DAC) values f each network node for all simulated attractors
#	the calculated DAC is the (specified attractor state value)- (simulated attractor state value).
# 4. attr_DAC_disc.txt: a dataframe containing the discretized calculated direction of activity change (DAC) values of each network node for all simulated attractors
# 5. attr_both.txt: a dataframe containing the log steady state values AND DAC values of each network node for all simulated attractors
# 6. attr_both_disc.txt: a dataframe containing the discretized log steady state values and discretized DAC values of each network node for all simulated attractors
#-----------------------------------------------------------

import os
import numpy as np
import pandas as pd
import networkx as nx
import random
import sfa
import csv
import sys
import re

##################INPUTS##########################
FCname = sys.argv[1] # Name of filee with FVS nodes
init = sys.argv[2] # Which replicate to use as basal value
bfile = sys.argv[3] # Which file of basal perturbations
factor = sys.argv[4] # Which set of activation levels to use
undesired= sys.argv[5] #specify column of dataframe with attractor to be compared to for DAC caclulation
nexp = sys.argv[6] # File name for normalized RNAseq expression data for experimental replicates
################################################

dpath = os.path.dirname('inputfiles/') #specifies input folder used to look for input files
fpath = os.path.join(dpath, 'network.sif') #location of network.sif
dirname = os.path.dirname("virtual_screening/") #Directory with basal states 

FCset = pd.read_csv(os.path.join(dpath, FCname), delim_whitespace=True,index_col = ["name"]) #FC set for perturbations
FCset = FCset.sort_values(by = 'name', axis = 0) #Sort list of FC nodes alphabetically

exp_nodes = pd.read_csv(os.path.join(dpath, nexp), delim_whitespace = True, index_col = ['name']) #RNAseq expression values for the 8 experimental replicates

# Find median expression of reference attractors for undesired state to compute DAC
ref = pd.read_csv(os.path.join('reference_attrs', 'ref_attrs_logss.txt'), delim_whitespace = True, index_col = ['name'])
undesired_list = [name for name in exp_nodes.columns if re.search(undesired, name)]
comp = ref.loc[undesired_list,:].median().tolist() #median of attractor values of undesired phenotype to calculate DAC

# Read in values for activation perturbations:
stim = pd.read_csv(os.path.join(dirname, 'perturbation_level_factor' + factor +  '.txt'),delim_whitespace=True,index_col = ['name']) 

# Read in perturbation orientation file with perturbations as columns, FVS nodes as rows:
basal_states=pd.read_csv(os.path.join(dirname, 'basal_states' + bfile +  '.txt'), delim_whitespace=True, index_col = ['name']) 
basal_states = basal_states.transpose(copy = True)
basal_states.index = FCset.index
print(basal_states)

# Make dataframe of perturbation values
pert_val = pd.DataFrame(columns = basal_states.columns, index = basal_states.index)
for pert, col in basal_states.iteritems():
    temp = [] 
    for i in range(len(col)):
        item = col[i]
        if item == 0:
            temp.append('nc') #Don't alter initial value for no changes
        elif item == 1:
            temp.append(stim.iloc[i, 0]) #Set initial value to pre-calculated activity level for knock-ins
        elif item == -1:
            temp.append(0) #Set initial value to 0 for knock-outs
    pert_val[pert]=temp

####################
def DAC(row,refval):
    return row-refval #calculates DAC for attractor 
####################
def disc(row): #group results into 1s, 0s, and -1s
    for i in range(len(row)):
        if row[i] > 0:
            row[i] = 1
        elif row[i] <0:
            row[i] = -1
        elif row[i] ==0:
            row[i] = 0
    return row

class ThreeNodeCascade(sfa.base.Data):
    def __init__(self):
        super().__init__()
        self._abbr = "TNC"
        self._name = "A simple three node cascade"

        signs = {'activates':1, 'inactivates':-1}
        A, n2i, dg = sfa.read_sif(fpath, signs=signs, as_nx=True)
        self._A = A
        self._n2i = n2i
        self._dg = dg
        self._i2n = {idx: name for name, idx in n2i.items()}
        
    # end of def __init__
# end of def class

if __name__ == "__main__":
##    initalize SF Class
    data = ThreeNodeCascade()
    algs = sfa.AlgorithmSet()
    alg = algs.create('SP')
    alg.data = data
    alg.params.apply_weight_norm = True
    alg.initialize()
    alg.params.exsol_forbidden=True #Run SFA iteratively to manually override the state of each FVS node at each time step

## Initialize output dataframes

    netnodes= list(data.dg.nodes)               #get network node names and
    
    perturb_logss = pd.DataFrame(index = basal_states.columns, columns = netnodes) # Initialize a dataframe for SFA output
    
    n = data.dg.number_of_nodes() #the number of nodes
    b = np.zeros((n,))

    
    nw_state=exp_nodes[init].tolist() #Subset expression data to include only data for network nodes for specific replicate
    
    for node in exp_nodes.index:
        b[data.n2i[node]]=float(nw_state[0]) #set node to it's initial state if there is expression data for it
        nw_state.pop(0)
    for name, item in pert_val.iteritems():
        FC = item.tolist()
        current=name

        pi = []
        for FCnode in FCset.index:
            fc_state=FC[0]
            if fc_state != 'nc':
                fc_state = float(FC[0])
                b[data.n2i[FCnode]]=fc_state
                pi.append(data.n2i[FCnode])
            elif fc_state == 'nc':
                pass
            FC.pop(0)
        x = alg.compute(b, pi)                      #Run SFA calculation
        
        for i, act in enumerate(x): #write out activity of all nodes
            perturb_logss.loc[current,data.i2n[i]]=act

# Populate "DAC" and "both" tables

    perturb_DAC=perturb_logss.copy(deep=True)
    perturb_DAC=perturb_DAC.apply(DAC, axis = 1, args = [comp])
    DACcol = [name + "_DAC" for name in perturb_logss.columns.tolist()]
    perturb_DAC.columns=DACcol
    perturb_both=pd.concat([perturb_logss,perturb_DAC],axis=1, ignore_index = True)
    perturb_both.columns = perturb_logss.columns.tolist() + DACcol


#Discretize tables
    perturb_logss_disc = perturb_logss.copy(deep=True).apply(disc,0)
    perturb_DAC_disc = perturb_DAC.copy(deep=True).apply(disc, 0)
    perturb_both_disc = perturb_both.copy(deep=True).apply(disc, 0)

#Write out results tables
    if len(bfile) > 0:
       split = 'splitfiles'
    else:
       split = ''
       
    perturb_logss_disc.to_csv(os.path.join(dirname, init,  FCname, split, "perturb_logss_disc"+bfile+'.txt'), sep=' ',float_format='%.0f',index_label="name",chunksize=10000) 
    perturb_DAC_disc.to_csv(os.path.join(dirname, init, FCname,  split, 'perturb_DAC_disc'+bfile+'.txt'), sep=' ',float_format='%.0f',index_label="name",chunksize=10000) 
    perturb_both_disc.to_csv(os.path.join(dirname, init, FCname,  split, 'perturb_both_disc'+bfile+'.txt'), sep=' ',float_format='%.0f',index_label="name",chunksize=10000) 
    perturb_logss.to_csv(os.path.join(dirname, init, FCname,  split, 'perturb_logss'+bfile+'.txt'),sep=' ',float_format='%.4f',index_label="name",chunksize=10000) 
    perturb_DAC.to_csv(os.path.join(dirname, init,FCname,  split, 'perturb_DAC'+bfile+'.txt'),sep=' ',float_format='%.4f',index_label="name",chunksize=10000)
    perturb_both.to_csv(os.path.join(dirname, init, FCname, split,'perturb_both'+bfile+'.txt'), sep=' ',float_format='%.4f',index_label="name",chunksize=10000)


