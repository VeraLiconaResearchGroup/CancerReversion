#---------------------------------------------------------
# compare_replicates.py compares classification of attractors from virtual screenings of perturbations applied to each experimental replicate
# for one value of k and one dataset
#
# Requires user specification of the folder where results from knn can be found, the number of nearest neighbors, and the label(s) of the goal cluster(s)
#
# INPUTS:
# 1-4. classifications of attractors from virtual screenings applied to each experimental replicate of MDA-MB-231
#
# OUTPUTS:
# 1. A table showing the numbr of perturbations resulting in attractors in the goal cluster from eeach of the initial conditions
# 2. A table showing the size of the intersection between classification of attractors in the goal cluster between initializations
# 3. A list of perturbations resulting in attractors in the normal cluster from all four initial conditions
#---------------------------------------------------------

import pandas as pd
import os
import sys

################ Inputs: ###############
knn_folder = sys.argv[1] #Specify the name of the folder containing knn results
i = sys.argv[2] #Specify the number of neighbors
FC = sys.argv[3] #Specify the name of the perturbed FVS or FC set
#########################################

print('knn_folder: ', knn_folder)
print('nearest neighbors: ', i)
print('\n')

def Intersect(l1, l2): #Function to find the intersection of two lists
    if len(l2) > len(l1):
        l3 = l1
        l1 = l2
        l2 = l3
    return(set(l1).intersection(l2))

# Read in knn classifications from each replicate
data1 = pd.read_csv(os.path.join('virtual_screening/MDAMB231_1' , FC, knn_folder, 'knn'+ i + '.txt'), delim_whitespace = True, index_col = ['name'])
data2 = pd.read_csv(os.path.join('virtual_screening/MDAMB231_2', FC, knn_folder, 'knn'+ i + '.txt'), delim_whitespace = True, index_col = ['name'])
data3 = pd.read_csv(os.path.join('virtual_screening/MDAMB231_3', FC, knn_folder, 'knn'+ i + '.txt'), delim_whitespace = True, index_col = ['name'])
data4 = pd.read_csv(os.path.join('virtual_screening/MDAMB231_4', FC, knn_folder, 'knn'+ i + '.txt'), delim_whitespace = True, index_col = ['name'])

# Specify label of goal cluster
goal = ['MCF10A_1', 'MCF10A_2', "MCF10A"]

# Subset knn classifications to include only attractors that are classified in the goal cluster
data1 = data1.loc[data1.classification.isin(goal),:]
data2 = data2.loc[data2.classification.isin(goal),:]
data3 = data3.loc[data3.classification.isin(goal),:]
data4 = data4.loc[data4.classification.isin(goal),:]

dfs = [data1, data2, data3, data4]

# Create a dataframe with the number of perturbations resulting in attractors classified in the goal cluster from each initial condition
size = pd.DataFrame(index= ['MDAMB231_' + str(n) for n in range(1,5)], columns = ['number of normal perts'])

for l in range(4):
    n , m = dfs[l].shape
    size.iloc[l,:] = n

print(size)

# Create a dataframe with the size of the intersection between perturbations resulting in attractors classified in the goal cluster from each initial condition
common = pd.DataFrame(index = size.index, columns = size.index)

for n in range(4):
    for m in range(4):
        l = len(Intersect(dfs[n].index, dfs[m].index))
        common.iloc[n,m] = l

print(common)

dataset = knn_folder.split('knn_')[-1]
common.to_csv(os.path.join('virtual_screening', 'compare_replicates_' + dataset +'_knn' + str(i) + '.txt'), sep = " ")

# Create list with the perturbations resulting in attractors in the goal cluster from all four initial conditions
alll = Intersect(data1.index, Intersect(data2.index, Intersect(data3.index, data4.index)))
print('all:')
print(len(alll))

print('\n')
print(alll)


    
