'''
This file contains test cases to test the FVS function.
'''

import networkx as nx
import random
import FVS
import re
import csv


###A random graph example
##N=6
##M=12
##G1=nx.gnm_random_graph(N, M, seed=None, directed=True)
###calculate FVS
##G1_FVS=FVS.FVS(G1)
##print G1.edges()
##print G1_FVS
##
#A fixed graph example, the solution should be ['A']
##G2=nx.DiGraph()
##G2.add_edges_from([('A','B'),('B','C'),('C','A'),('A','D'),('D','A')])
###calculate FVS
##G2_FVS=FVS.FVS(G2)
##print G2.edges()
##print G2_FVS

#A three node feedback loops. The solution could be any node.
#With fixed randomseed, one should get the same answer.
outputfile=open('231_FVS_output2.txt','w+')
edges=open('test_network.sif').readlines() #open file with edges formatted as downloaded (no changes)
data=[tuple(line.strip().split()) for line in edges] #creates tuple from file
print ('edges loaded')
G3=nx.DiGraph()
G3.add_edges_from(data)
#print G3.edges()
#calculate FVS
i=1
for i in range(1,11):
    #print 'calculating FVS'+str(i)
    #G3_SCC_max= max(nx.strongly_connected_components(G3), key=len)
    G3_FVS1=FVS.FVS(G3, T_0=0.6, alpha=0.99, maxMvt_factor=5, maxFail=50, randomseed=i)
    #print'FVS set: '+ str(G3_FVS1)
    print(i)
    outputfile.write(str(G3_FVS1)+'\n')
outputfile.close()
    
##G3_SCC_max= max(nx.strongly_connected_components(G3), key=len)
##G3_SCC_tot=[len(c) for c in sorted(nx.strongly_connected_components(G3),key=len, reverse=True)]
##G3_SCC_num=nx.number_strongly_connected_components(G3)
##print 'Generated graph contains '+str(len(G3.nodes()))+' nodes and '+str(len(G3.edges()))+' edges'
##print 'strongly connected components: '
##print(G3_SCC_tot)

##into=G3.in_degree(G3_SCC)
##outof=G3.out_degree(G3_SCC)
##
##
##print 'number of edges into: '
##print into
##print 'number of edges out of: '
##print outof
####print pred
###print G3_FVS
