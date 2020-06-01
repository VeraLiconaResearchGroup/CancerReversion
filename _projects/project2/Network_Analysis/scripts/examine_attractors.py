#------------------------------------------------
# examine_attractors.py returns a summary about the reference attractors
#
# INPUTS:
# 1. Log steady state of reference attractors
# 2. list of FVS nodes
#
# OUTPUTS:
# 1. Attractor values of FVS nodes
# 2. Standard deviation between expression values of each node in normal and cancerous attractors
#------------------------------------------------

import pandas as pd
import math

df1 = pd.read_csv('reference_attrs/ref_attrs_logss.txt', delim_whitespace = True, index_col = 'name')
fvs = pd.read_csv('inputfiles/FVS_12', delim_whitespace = True, index_col = ["name"])

df2 = df1.loc[:,df1.columns.isin(fvs.index)].transpose()
df2.to_csv('FVS_attractor_state.txt', sep  = " ")

norm = df1.iloc[0:4,:]
ca = df1.iloc[4:8,:]


ns = norm.std(axis = 0)
cs = ca.std(axis = 0)

df3 = pd.concat([ns, cs], axis = 1)
df3.columns = ["normal", "cancerous"]

df3.to_csv('Attractor_sd.txt', sep = " ")



