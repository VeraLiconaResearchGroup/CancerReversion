# -----------------------------------------------------------
# SimulateAttractors.py
# A python script for simulating random attractors from an initial state using SFA algorithm
# 
# Requires user specification of the # random attractors to be produced, and the attractor the simulations are compared to for DAC calculation
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

#.:/usr/lib/python3.7
import os
import numpy as np
import pandas as pd
import networkx as nx
import random
import sfa
import csv
from randomStateGenerator import *

##Input files and user specified variables###################
dpath = os.path.dirname('inputfiles/') #specifies input folder used to look for input files
fpath = os.path.join(dpath, 'network.sif') #location of network.sif


##exp_nodes=pd.read_csv(os.path.join(dpath, exp), delim_whitespace=True,index_col = ["name"]) #expressed nodes for basal value simulation
ref=pd.read_csv(os.path.join(dpath,'reference_attractors.txt'), delim_whitespace=True,index_col = ["name"]) #reference (experitmental) attractors
exp_nodes = ref
##comp=sys.argv[2] #specify column of dataframe with attractor to be compared to for DAC caclulation

output_folder = '' #name of output folder specified in batch file

num_sim= 50000  # please specify6 the number of attractors to be simulated
m = 7 # modulo to work with for generating basal states
##################################

def DAC(row,refval):
    return refval-row #calculates DAC for attractor 

def disc(row): #discrtizes results
    for i in range(len(row)):
        if row[i] > 0:
            row[i] = 1
        elif row[i] <0:
            row[i] = -1
        elif row[i] ==0:
            row[i] = 0
    return row


# def generateBasalState(nodes,num_nodes, num_conditions):
#     sets = [] #create a list to be used to determine unique basal states
#     while len(sets)  < num_conditions: #unitl we generate the desired number of basal states
#         temp = tuple(np.random.randint(-1,2, size = num_nodes)) #generate random basal state of -1, 0, or 1
#         sets.append(temp)
#         sets = list(set(tuple(sets)))#check it is unique
#         if len(sets) % 100 == 0:
#             print(len(sets))

#     basal_states = pd.DataFrame(index=nodes)
#     for ls in sets:
#         basal_states['attr_' + str(sets.index(ls)+1).rjust(len(str(num_conditions)), '0')] = list(ls)
        
#     print("Basal Levels Generated")

#     basal_states.to_csv(output_folder+'/basal_states.txt', sep=' ')            
#     return basal_states


#generate random basal states

num_nodes = len(exp_nodes.index) 
##basal_states=generateBasalState(exp_nodes.index,num_nodes, num_sim, m, output_folder) 
basal_states = pd.read_csv("stat1.txt", delim_whitespace=True,index_col = ["name"])

class ThreeNodeCascade(sfa.base.Data):
    def __init__(self):
        super().__init__()
        self._abbr = "TNC"
        self._name = "A simple three node cascade"

        signs = {'activates':1, 'inhibits':-1}
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
    alg.params.exsol_forbidden=True
    alg.params.alpha=0.9
    alg.initialize()


## Initialize output dataframes

    
    netnodes= list(data.dg.nodes)               #get network node names and
##    DACcol = [i + '_DAC' for i in netnodes]     #initialize list for DAC column names
    
    attr_logss=ref.transpose(copy=True)         #transpose reference attractor for logss frame

    n = data.dg.number_of_nodes() #the number of nodes
    b = np.zeros((n,))

    network = exp_nodes.index
    n = 1


    while n <= 1:       
        nwstates = [0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,0]
        current='attr_' + str(n).rjust(len(str(num_sim)), '0')
        #print(current)
        #if current=='attr_A':
        for node in network:
            nw_state=float(nwstates[0])
            b[data.n2i[node]]=nw_state          #set node to its simulated initial state
            nwstates.pop(0)
      
        x = alg.compute(b)                      #Run SFA calculation
        
        for i, act in enumerate(x): #write out activity of all nodes
            print(i,data.i2n[i])
            attr_logss.loc[current,data.i2n[i]]=act
        #nwstates.pop(0)
        n+=1
        

# Populate DAC and both tables
##    attr_DAC=attr_logss.copy(deep=True)
##    attr_DAC=attr_DAC.apply(DAC, axis = 1, args = [attr_logss.loc[comp,]])
##    attr_DAC.columns=DACcol
##    attr_both=pd.concat([attr_logss,attr_DAC],axis=1, ignore_index = True)
##    attr_both.columns = netnodes + DACcol

###Discretize tables
##    attr_logss_disc = attr_logss.copy(deep=True).apply(disc,0)
##    attr_DAC_disc = attr_DAC.copy(deep=True).apply(disc, 0)
##    attr_both_disc = attr_both.copy(deep=True).apply(disc, 0)

#Write out results tables
##    attr_logss_disc.to_hdf(output_folder+'/attr_logss_disc.h5', key = 'attr_logss_disc') 
##    attr_DAC_disc.to_csv(output_folder+'/attr_DAC_disc.txt', sep=' ',index_label="name") 
##    attr_both_disc.to_csv(output_folder+'/attr_both_disc.txt', sep=' ',index_label="name") 
    attr_logss.to_csv(output_folder+'attr_logss_15_1_alpha9.txt', sep=' ',float_format='%.4f',index_label="name") 
##    attr_DAC.to_csv(output_folder+'/attr_DAC.txt', sep=' ',float_format='%.4f',index_label="name")
##    attr_both.to_csv(output_folder+'/attr_both.txt', sep=' ',float_format='%.4f',index_label="name")
    
