import os
import sfa
import numpy as np
import networkx as nx
import random

class ThreeNodeCascade(sfa.base.Data):
    def __init__(self):
        super().__init__()
        self._abbr = "TNC"
        self._name = "A simple three node cascade"

        # Specify the file path for network file in SIF.
        dpath = os.path.dirname(__file__)
        fpath = os.path.join(dpath, 'Network_full.sif')
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
    network=open('network_nodes_173').read().split('\n')
    networkstatesfile=open('10A_basal').read()
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
    outputfile=open('attractor_10A.txt','w+')
    for i, act in enumerate(x): #for all nodes (i) and their activity (act) in network
       outputfile.write("%s %f"%(data.i2n[i], act))
       outputfile.write('\n')
                                                  

outputfile.close()









