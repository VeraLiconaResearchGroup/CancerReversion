#---------------------------------------------------------
# compare_num_neigh.py compares classification of attractors from virtual screenings from one dataset with different values of k
#
# Requires user specification of the folder where results from knn can be found
#
# INPUTS:
# 1-8. Files with attractors classified in the goal cluster for k values 1-8
#
# OUTPUTS:
# 1. A table showing the size of the intersection between classification of attractors in the goal cluster between different values of k
#---------------------------------------------------------

import pandas as pd
import os
import sys

################ User Inputs: ####################
knn_folder = sys.argv[1] #Name of folder containing knn results
replicate = sys.argv[2] #Name of experimental replicate used for virtual screenings
FVS_name = sys.argv[3] #Name of perturbed FVS set
#############################################

print('knn_folder: ', knn_folder)
print('replicate: ', replicate)
print('\n')

def Intersect(l1, l2): #Function to find the intersection of two lists
    if len(l2) > len(l1):
        l3 = l1
        l1 = l2
        l2 = l3
    return(set(l1).intersection(l2))

# read in datasets from same virtual screening run with different number of neighbors
outpath = os.path.join('virtual_screening', replicate, FVS_name, knn_folder)
data1 = pd.read_csv(os.path.join(outpath, 'knn1_goal.txt'), delim_whitespace = True, index_col = ['name'])
data2 = pd.read_csv(os.path.join(outpath, 'knn2_goal.txt'), delim_whitespace = True, index_col = ['name'])
data3 = pd.read_csv(os.path.join(outpath, 'knn3_goal.txt'), delim_whitespace = True, index_col = ['name'])
data4 = pd.read_csv(os.path.join(outpath, 'knn4_goal.txt'), delim_whitespace = True, index_col = ['name'])
data5 = pd.read_csv(os.path.join(outpath, 'knn5_goal.txt'), delim_whitespace = True, index_col = ['name'])
data6 = pd.read_csv(os.path.join(outpath, 'knn6_goal.txt'), delim_whitespace = True, index_col = ['name'])
data7 = pd.read_csv(os.path.join(outpath, 'knn7_goal.txt'), delim_whitespace = True, index_col = ['name'])
data8 = pd.read_csv(os.path.join(outpath, 'knn8_goal.txt'), delim_whitespace = True, index_col = ['name'])


dfs = [data1, data2, data3, data4, data5, data6, data7, data8]

# Create a dataframe with the size of the intersection between perturbations resulting in attractors classified in the goal cluster using each number of neighbors for classification
common = pd.DataFrame(index= range(1,9), columns = range(1,9))
common.index.name = 'number of neighbors'
for n in range(len(dfs)):
    for m in range(len(dfs)):
        i = len(Intersect(dfs[n].index, dfs[m].index))
        common.iloc[n,m] = i

# Writeout Dataframe
dataset = knn_folder.split('knn_')[-1]
common.to_csv(os.path.join(outpath, 'comp_num_neigh_' + dataset), sep = " ")

print(common)
print('\n') 
print('*'*100)
print('\n') 
