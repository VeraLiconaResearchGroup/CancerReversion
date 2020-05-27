# -----------------------------------------------------------
# reference_attractors_filpped.py
# A python script for simulating attractors from experimental initial conditions using SFA algorithm
# with initial conditions for GSK3B and CTNNB1 swapped betweeen the cancer and normal replicates
#
# INPUTS:
# 1. The intracellular signaling network in .sif format
# 2. A dataframe of normalized RNAseq expression data for all experimental conditions (rows = nodes, columns = attractors)
#
# OUTPUTS:
# 1. ref_attrs_logss.txt: a dataframe containing the log steady state values of each network node for all simulated attractors 
# 2. ref_attrs_logss_disc.txt: a dataframe containing the discretized log steady state values of each network node for all simulated attractors
# 3. ref_attrs_DAC.txt: a dataframe containing the calculated direction of activity change (DAC) values f each network node for all simulated attractors
#	the calculated DAC is the (specified attractor state value)- (simulated attractor state value).
# 4. ref_attrs_DAC_disc.txt: a dataframe containing the discretized calculated direction of activity change (DAC) values of each network node for all simulated attractors
# 5. ref_attrs_both.txt: a dataframe containing the log steady state values AND DAC values of each network node for all simulated attractors
# 6. ref_attrs_both_disc.txt: a dataframe containing the discretized log steady state values and discretized DAC values of each network node for all simulated attractors
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
import sys

##Input files and user specified variables###################
dpath = os.path.dirname('inputfiles/') #specifies input folder used to look for input files
fpath = os.path.join(dpath, 'network.sif') #location of network.sif

# read in initial conditions with flipped values for GSK3B and CTNNB1
basal_states = pd.read_csv('test_flip/basal_states_flip.txt', index_col = ['name'], delim_whitespace = True)
basal_states = basal_states.transpose()
basal_states = basal_states.loc[:,basal_states.columns.isin(ref.index)]

####################
def DAC(row,refval):
    return row-refval #calculates DAC for attractor 
####################
def disc(row): #discrtizes results
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


## Initialize output dataframes

    
    netnodes= list(data.dg.nodes)               #get network node names and
    
    attr_logss=ref.transpose(copy=True)         #transpose reference attractor for logss frame
    attr_logss=attr_logss.iloc[0:0]

    n = data.dg.number_of_nodes() #the number of nodes
    b = np.zeros((n,))

    network = basal_states.columns
    pi = []

    
    for index, row in basal_states.iterrows():
        nwstates = row.tolist()
        current = index
        for node in network:
            nw_state=float(nwstates[0])
            b[data.n2i[node]]=nw_state          #set node to its simulated initial state
            nwstates.pop(0)
      
        x = alg.compute(b, pi)                      #Run SFA calculation
        
        for i, act in enumerate(x): #write out activity of all nodes
            attr_logss.loc[current,data.i2n[i]]=act


#Write out results tables

    comp =  attr_logss.iloc[4:9,:].median().tolist()
    attr_DAC=attr_logss.copy(deep=True)
    attr_DAC=attr_DAC.apply(DAC, axis = 1, args = [comp])
    DACcol = [name + '_DAC' for name in attr_logss.columns]
    attr_DAC.columns=DACcol
    attr_both=pd.concat([attr_logss,attr_DAC],axis=1, ignore_index = True)
    attr_both.columns = netnodes + DACcol

#Discretize tables
    attr_logss_disc = attr_logss.copy(deep=True).apply(disc,0)
    attr_DAC_disc = attr_DAC.copy(deep=True).apply(disc, 0)
    attr_both_disc = attr_both.copy(deep=True).apply(disc, 0)

# Write out dataframes
    attr_logss_disc.to_csv('test_flip/ref_attrs_logss_disc.txt', sep=' ',float_format='%.0f',index_label="name") 
    attr_DAC_disc.to_csv('test_flip/ref_attrs_DAC_disc.txt', sep=' ',float_format='%.0f',index_label="name") 
    attr_both_disc.to_csv('test_flip/ref_attrs_both_disc.txt', sep=' ',float_format='%.0f',index_label="name") 
    attr_logss.to_csv('test_flip/ref_attrs_logss.txt',sep=' ',float_format='%.4f',index_label="name") 
    attr_DAC.to_csv('test_flip/ref_attrs_DAC.txt',sep=' ',float_format='%.4f',index_label="name",)
    attr_both.to_csv('test_flip/ref_attrs_both.txt', sep=' ',float_format='%.4f',index_label="name")

    

    
