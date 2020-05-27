#------------------------------------------
# generate_basal_states_lockedNodes.py generates a pre-defineed numbeere of perturbations of the FVS
# nodes with some nodes "locked" in a specific orientation in all perturbations
# 1 = knock-in, 0 = no change, -1 = knock-out
#
# Requires user specification of the number of perturbations to be generated, FVS nodes to be locked, and their orientation
#------------------------------------------

import os
import numpy as np
import pandas as pd
import networkx as nx
import random
from collections import Counter
import csv
import sys

def main():
    numpert=int(sys.argv[1]) #Specify the number of perturbations to generate
    outpath = sys.argv[2] #Output folder

    FVS = pd.read_csv('inputfiles/FVS_12', delim_whitespace = True, index_col = 'name') #Read in list of FVS nodes
    lock = {'CTNNB1': 0, 'GSK3B':0, 'RELA':-1, 'FOXM1':-1, "PIAS1":1} #Dictionary of FVS nodes to be locked and their orientation

    lockdf = pd.DataFrame.from_dict(lock, orient = 'index')
    FVS2 = FVS.drop(lock.keys(), axis = 0) #Remove FVS nodes to be locked from the list of FVS nodes
    numnodes = len(FVS2.index) #The number of nodes to genereate random states for
    
    #Generate unique perturbation combinations of FVS nodes that are not locked
    temp=np.random.choice(a=[-1,0,1],size=[numpert, numnodes])
    df1=pd.DataFrame(temp)
    df1.drop_duplicates(keep = 'first', inplace = True)
    while df1.shape[0] < numpert:
        temp=np.random.choice(a=[-1,0,1],size=[numpert-df1.shape[0],numnodes])
        temp=pd.DataFrame(temp)
        df1 = pd.concat([df1, temp])
        df1.drop_duplicates(keep = 'first', inplace = True)
    df1 = df1.transpose(copy = True)
    
    l1=[] #Generate list for dataframe column names
    for i in range(numpert):
        l1.append(prefix+'_' + str(i+1).rjust(len(str(numpert)), '0'))
    df1.columns=l1
    df1.index = FVS2.index

    #Make a dataframe with the locked FVS nodes 
    df2 = pd.concat([lockdf]*numpert, axis = 1)
    df2.columns = l1

    #Combine dataframe of random perturbations with dataframe of locked FVS node values
    df1 = pd.concat([df1,df2], axis = 0)
    df1 = df1.reindex(FVS.index)

    #Write out results
    prefix = "Perturb"
    num_out= int(numpert/20000)
    if num_out>1: #Split basal states into files with 20,000 perturbations if numpert>20000
        j=0
        for i in range(1,int(num_out+1)):
            k=j+1
            j=20000*i
            dfs=df1.loc[:, prefix +'_'+ str(k).rjust(len(str(numpert)), '0'): prefix +'_'+str(j).rjust(len(str(numpert)), '0')]
            dfs.to_csv(os.path.join(outpath, 'basal_states'+str(i)+'.txt'),sep=' ',index=False)   
    else:
        df1.to_csv(os.path.join(outpath, 'basal_states.txt'),sep=' ')      
        
            
main()
