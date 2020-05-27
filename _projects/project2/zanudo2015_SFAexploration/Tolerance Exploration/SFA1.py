import os
import numpy as np
import pandas as pd
import networkx as nx
import random
import sfa
import csv


##Input files and user specified variables###################
dpath = os.path.dirname('../inputfiles/') 
fpath = os.path.join(dpath, 'network.sif')
states = pd.read_csv('../initial_states_Leuk_Apop.txt', delim_whitespace = True, index_col = ["name"])
states = states.transpose()
inits = states.iloc[[0]]

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
    #alg.params.exsol_forbidden=True
    alg.params.alpha=0.9
    alg.initialize()
    alg.params.exsol_forbidden=True

    netnodes= list(data.dg.nodes)

    n = data.dg.number_of_nodes() #the number of nodes
    b = np.zeros((n,))
    #print(inits)
    cols=list(inits.columns)
    #print(cols)
    attr_logss=pd.DataFrame(index=inits.index,columns=inits.columns)
    for index,row in inits.iterrows():
        for node in cols:
            #print(inits.loc[index,node])
            b[data.n2i[node]]=inits.loc[index,node]
        x=alg.compute(b)

        for i, act in enumerate(x): #write out activity of all nodes
            attr_logss.loc[index,data.i2n[i]]=act

            
    attr_logss.to_csv('sfa_leuk1_3.txt', sep=' ',float_format='%.4f',index_label="name") 
