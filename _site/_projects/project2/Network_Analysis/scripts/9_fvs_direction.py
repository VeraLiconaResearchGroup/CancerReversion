#------------------------------------------------------
# fvs_direction.py identifies the orientation of FVS node perturbations resulting in attractors in the goal cluster (successful perturbations)
# 
# INPUTS:
# 1. Basal states of randomly generated perturbations of FVS nodes
# 2. A list of perturbations resulting in attractors in the goal cluster
# 3. A list of FVS nodes
#
# OUTPUTS:
# 1. A file with the frequency of each perturbation orientation (knocked-in, knocked-out, or no change) for the perturbations resulting in attractors in the goal cluster
#------------------------------------------------------

import pandas as pd
import os
import sys


###################### User Inputs: #####################
sub = sys.argv[1] #File with names of perturbations of inteerest
FCname = sys.argv[2] #Name of perturbed FVS set
#########################################################

dirname = os.path.dirname('virtual_screening/')
basal = pd.read_csv(os.path.join(dirname, 'basal_states.txt'), delim_whitespace = True, index_col = ['name']) #Read in FVS node perturbations 
subset = pd.read_csv(os.path.join(dirname, sub), delim_whitespace = True, index_col = ['name']) #Read in list of successful perturbations
fvs = pd.read_csv(os.path.join('inputfiles', FCname), index_col = ['name']) #Read in list of FVS nodes

#Create dataframe with perturbation orientations for successful perturbations
df = basal.loc[basal.index.isin(subset.index), :] 
df.columns = fvs.index

#Create dataframe with frequency of orientation of each FVS node in successful perturbations
freq = pd.DataFrame(index = ['knocked-in', 'knocked-out', 'no_change'], columns = fvs.index)
for node, col in df.iteritems():
    col = col.tolist()
    up = col.count(1)
    down = col.count(-1)
    nc = col.count(0)
    freq.loc['Knocked-in', node] = round(up/npert*100, 3)
    freq.loc['Knocked-out', node] = round(down/npert*100,3)
    freq.loc['No_Change', node] = round(nc/npert*100,3)

print(freq)
outf = sub.split('.txt')[0] + '_fvsDir.txt'
freq.to_csv(os.path.join(dirname, outf), sep = " ")

#### Write out dataframe including number of nodes that must be perturbed (not no-change) in a successful perturbation:
count = pd.DataFrame(index = basal.index, columns = ['Number_of_Perturbed_Nodes'])
    
for pert, row in df.iterrows():
    row = row.tolist()
    nc = row.count(0)
    npert = len(basal.columns) - nc
    count.loc[pert, 'Number_of_Perturbed_Nodes'] = npert
count.to_csv(os.path.join(dirname, 'number_of_perturbed_nodes_' + sub), sep = " ", index_label = 'name')
print(count.Number_of_Perturbed_Nodes.value_counts())
