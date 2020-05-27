#---------------------------------------------------------
# compare_knn.py compares classification of attractors from virtual screenings from the same initialization using different
# datasets (logss, DAC, both, and disc versions) for one value of nearest neighbors 
#
# Requires user specification of the folder where results from virtual screenings can be found and the number of nearest neihgbors
#
# INPUTS:
# 1-6. logss, DAC, both, logss_disc, DAC_disc, both_disc datasets from virtual screenings
#
# OUTPUTS:
# 1. knn_comp_i.txt: A file with the number of datasets classified each perturbation as normal
# 2. A table showing the size of the intersection between classification of attractors in the goal cluster between datasets
#---------------------------------------------------------

import pandas as pd
import os
import sys

################## Inputs #################
pert_folder = sys.argv[1] #Path to folder containing results of virutal screening
i = sys.argv[2] #Specify the number of neighbors
##########################################

def Intersect(l1, l2): #Function to find the intersection of two lists
    if len(l2) > len(l1):
        l3 = l1
        l1 = l2
        l2 = l3
    return(set(l1).intersection(l2))

# Read in knn classifications from same value of k and initialization, but different datasets
df1 = pd.read_csv(os.path.join(pert_folder, "knn_logss", "knn" + i + '_goal.txt'), delim_whitespace = True, index_col = ["name"])
df2 = pd.read_csv(os.path.join(pert_folder, "knn_logss_disc", "knn" + i + '_goal.txt'), delim_whitespace = True, index_col = ["name"])
df3 = pd.read_csv(os.path.join(pert_folder, "knn_DAC", "knn" + i + '_goal.txt'), delim_whitespace = True, index_col = ["name"])
df4 = pd.read_csv(os.path.join(pert_folder, "knn_DAC_disc", "knn" + i + '_goal.txt'), delim_whitespace = True, index_col = ["name"])
df5 = pd.read_csv(os.path.join(pert_folder, "knn_both", "knn" + i + '_goal.txt'), delim_whitespace = True, index_col = ["name"])
df6 = pd.read_csv(os.path.join(pert_folder, "knn_both_disc", "knn" + i + '_goal.txt'), delim_whitespace = True, index_col = ["name"])

dfs = [df1, df2, df3, df4, df5, df6]
indexx = []
for df in dfs:
    indexx = indexx + df.index.tolist()

perturbs = list(set(indexx)) #Make a list of all perturbations that result in attractors classified in the goal cluster

# Make a dataframe with the number of times each attractor was classified in the goal cluster using separate datasets
final = pd.DataFrame(index = perturbs, columns = ["Number of Datasets"])
for pert in perturbs:
    k = 0
    for df in dfs:
        if pert in df.index.tolist():
            k += 1
    final.loc[pert, "Number of Datasets"] = k

final.to_csv(os.path.join(pert_folder, "knn_comp_"+i+'.txt'), sep = " ")

# Create a dataframe with the size of the intersection between perturbations resulting in attractors classified in the goal cluster from each dataset
common = pd.DataFrame(index = ["logss", "DAC", "both", "logss_disc", "DAC_disc", "both_disc"], columns = ["logss", "DAC", "both", "logss_disc", "DAC_disc", "both_disc"])
for n in range(len(dfs)):
    for m in range(len(dfs)):
        i = len(Intersect(dfs[n].index, dfs[m].index))
        common.iloc[n,m] = i

print(common)
    
