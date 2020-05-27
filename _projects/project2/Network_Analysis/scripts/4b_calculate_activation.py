#################################
# calculate_activation.py calculates the activation level of each FVS/FC node
# Activation value = a factor*mean of the normalized expression data for the undesird phenotype
#
# Requires specifiction of factor for activation calculation.
#
# INPUTS:
# 1. list of FC or FVS nodes
# 2. Normalized expression values from experimental conditions
#
# OUTPUTS:
# 1. dataframe with activation level of each FVS node
#################################

import pandas as pd
import os
import sys
import re

#########
FCname = sys.argv[1] #Name of FVS or FC file
undesired = sys.argv[2] #Prefix of replicates for undesired phenotype
factor = int(sys.argv[3]) #Setting activation level to 2*mean expression value for undesired phenotype
nexp = sys.argv[4]

dpath = os.path.dirname('inputfiles/') #specifies input folder used to look for input files
FCset = pd.read_csv(os.path.join(dpath, FCname), delim_whitespace=True,index_col = ["name"])#FC set for perturbations

# Read in normalized expression values of experimental conditions
exp = pd.read_csv(os.path.join(dpath, nexp), delim_whitespace = True, index_col = ['name']) #RNAseq expression values for the 8 experimental replicates

#create dataframe of RNAseq expression values for undesired initial state of FVS nodes
cols = [name for name in exp.columns if re.search(undesired, name)]
exp = exp.loc[FCset.index,cols] 
mean = exp.mean(axis = 1) #Calculate mean of expression values for undesired phenotype

##### Using the mean + 3*sd between the expresesion replicates does not produce a large enough expression value
sd = exp.std(axis = 1)
df = pd.concat([mean, sd, mean+3*sd], axis = 1)
df.columns  = ["Mean", "SD", "Mean + 3SD"]
df.to_csv('virtual_screening/perturbation_level_sd.txt', sep = " ")

pert = mean*factor #Calculate activation level
df2 = pd.concat([mean, pert], axis = 1) # create dataframe with FVS node, mean, and activation level of mean
df2.columns = ["Mean", str(factor)+"*Mean"]
pert.columns = str(factor)+"*Mean"
pert.to_csv('virtual_screening/perturbation_level_factor'+ str(factor) + '.txt', sep = " ")

print(pert)

                
