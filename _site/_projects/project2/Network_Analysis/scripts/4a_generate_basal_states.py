#------------------------------------------
# generate_basal_states.py generates a predefined number of unique random perturbation combinations of the FVS nodes for virtual screening
# 1 = knock-in, 0 = no change, -1 = knock-out
#
# Requires user specification of the # random perturbations to be produced
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
    ############ User Inputs: ################
    numpert=int(sys.argv[1]) #Number of perturbation comninations to generate
    numnodes=int(sys.argv[2]) #Number of FVS nodes to perturb
    ############################################

    outpath = os.path.dirname('virtual_screening/') #Output location for basal states
    temp=np.random.choice(a=[-1,0,1],size=[numpert,numnodes]) #Make dataframe of random perturbations
    df1=pd.DataFrame(temp)
    df1.drop_duplicates(keep = 'first', inplace = True) #Remove duplicate perturbations
    
    while df1.shape[0] < numpert: #Generate more perturbation combinations and remove duplicates until they are all unique
        temp=np.random.choice(a=[-1,0,1],size=[numpert-df1.shape[0],numnodes])
        temp=pd.DataFrame(temp)
        df1 = pd.concat([df1, temp])
        df1.drop_duplicates(keep = 'first', inplace = True)
    
    l1=[] #Create list for dataframe column names
    for i in range(numpert):
        l1.append('Perturb_' + str(i+1).rjust(len(str(numpert)), '0'))
    df1.index=l1

    # Write out perturbations
    num_out= int(numpert/20000) 
    print(num_out)
    if num_out>1: #Split basal states into files with 20,000 perturbations if numpert>20000
        j=0
        for i in range(1,int(num_out+1)):
            k=j+1
            j=20000*i
            dfs=df1.loc[prefix +'_'+ str(k).rjust(len(str(numpert)), '0'): prefix +'_'+str(j).rjust(len(str(numpert)), '0'),:]
            dfs.to_csv(os.path.join(outpath, 'basal_states'+str(i)+'.txt'),sep=' ',index_label = 'name')
        df1.to_csv(os.path.join(outpath, 'basal_states.txt'), sep = " ", index_label = 'name')
    else:
        df1.to_csv(os.path.join(outpath, 'basal_states.txt'), sep=' ', index_label = 'name')      
    
            
main()

