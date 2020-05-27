#-------------------------------------------------
# feedback_loops.py identifies the number of negative feedback loops each FVS node is in
# !! Needs to be revised
#-------------------------------------------------

import os
import numpy as np
import pandas as pd
import networkx as nx
import sys
import sfa


fpath = os.path.join('inputfiles', 'network.sif')
signs = {'activates':1, 'inhibits':-1}
A, n2i, dg = sfa.read_sif(fpath, signs=signs, as_nx=True)

FVS = pd.read_csv('inputfiles/FVS_12', delim_whitespace = True, index_col = 'name')
FVSnodes = FVS.index.tolist()

loops = pd.DataFrame(np.zeros((12, 2)), index = FVS.index, columns = ['Negative','Positive'])

cycles = nx.find_cycle(dg)

print(len(cycles))


# for cycle in cycles:
#     product = dg.get_edge_data(cycle[-1], cycle[0])['SIGN']
#     for i in range(len(cycle)-1):
#         edge = tuple(cycle[i:i+2])
#         edge = dg.get_edge_data(*(edge))
#         product *= edge["SIGN"]
#     col = 'Positive'
#     if product == -1:
#         col = 'Negative'
#     for node in FVSnodes:
#         if node in cycle:
#             loops.loc[node, col] += 1

# loops.to_csv('FVSnode_feedbackloops.txt', sep = " ")
# print(loops)
        
        


