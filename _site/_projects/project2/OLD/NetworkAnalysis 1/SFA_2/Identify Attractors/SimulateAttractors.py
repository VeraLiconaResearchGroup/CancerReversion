#.:/usr/lib/python3.7
import os
import numpy as np
import networkx as nx
import random
import sfa*
import csv
from discretize import *
from randomStateGenerator import *

num_conditions = 100000
num_nodes = 114

generate random basal states
generateBasalState(num_nodes, num_conditions)

class ThreeNodeCascade(sfa.base.Data):
    def __init__(self):
        super().__init__()
        self._abbr = "TNC"
        self._name = "A simple three node cascade"

        # Specify the file path for network file in SIF.
        dpath = os.path.dirname(__file__)
        fpath = os.path.join(dpath, '../../../Network Construction 2/Network_full.sif')
        # Use read_sif function.
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
    

    n = data.dg.number_of_nodes() #the number of nodes
    b = np.zeros((n,))

##  read in full network nodes, and their initial conditions 
    network=open('../expression_nodes_114').read().split('\n')
    n = 1
    attractors = []
    names = []
    while n <= num_conditions:
        networkstatesfile=open('Simulated Basal States/basal'+ str(n).rjust(len(str(num_conditions)), '0') + '.txt').read()
##  create list of node states (normexp)
        nwstates=networkstatesfile.split('\n') #create list of initial state file
    
        for node in network:
            nw_state=float(nwstates[0])
            b[data.n2i[node]]=nw_state #set node to its initial state
            nwstates.pop(0)

        readout_dict={} #initialize dict for readout nodes steady state values

        
##  RUN SFA        
        x = alg.compute(b)

## write out results
        outputfile=open('Simulated Attractors/attractor' + str(n).rjust(len(str(num_conditions)), '0') + '.txt','w+')
        ls = []
        for i, act in enumerate(x): #for all nodes (i) and their activity (act) in network
           outputfile.write("%s %f"%(data.i2n[i], act))
           outputfile.write('\n')
           if n == 1:
               names.append("%s"%data.i2n[i])
           ls.append("%f"%(act))
        if n == 1:
            attractors.append(names)
        attractors.append(ls)
        if n % 100 ==0:
            print(n)
        n += 1
        
    df = []                                              
    for i in range(len(names)):
        row = []
        for list in attractors:
            row.append(list[i])
        df.append(row)

    with open('attractor_df.txt', 'w') as myfile:
        wr = csv.writer(myfile,quoting=csv.QUOTE_NONE,delimiter='\t')
        for row in df:
            wr.writerow(row)

    df2 = discrete(df)

    with open('attractor_df_discrete.txt', 'w') as myfile:
        wr = csv.writer(myfile,quoting=csv.QUOTE_NONE,delimiter='\t')
        for row in df2:
            wr.writerow(row)
    

outputfile.close()

