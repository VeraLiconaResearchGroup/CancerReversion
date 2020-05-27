# -----------------------------------------------------------
# combine_sfa.py Combines the split files with attractors from virtual screenings to produce one file with all of the attractors
#
# Requires user specification of the FVS name, the name of the experimental replicate that perturbations were applied to, and which dataset is being created 
#
# INPUTS:
# 1. Split files from SFA (perturb_dataseti.txt)
#
# OUTPUTS:
# 1. A single file with all attractors from virtual screenings
# -----------------------------------------------------------

import pandas as pd
import os
import sys

############## INPUTS: #################
FCname = sys.argv[1] #name of FVS or FC set
init = sys.argv[2] # Which replicate to use as basal value
dataset = sys.argv[3] #which dataset we are combining into one dataframe
#########################################


dirpath = os.path.dirname('virtual_screening/')
df1=pd.read_csv(os.path.join(dirpath, init, FCname,  "splitfiles", 'perturb_' +dataset + '1.txt'),delim_whitespace=True, index_col=["name"])
df2=pd.read_csv(os.path.join(dirpath, init, FCname,  "splitfiles", 'perturb_' + dataset + '2.txt'),delim_whitespace=True, index_col=["name"])
df3=pd.read_csv(os.path.join(dirpath, init, FCname,"splitfiles", 'perturb_' + dataset + '3.txt'),delim_whitespace=True, index_col=["name"])
df4=pd.read_csv(os.path.join(dirpath, init, FCname, "splitfiles", 'perturb_' + dataset + '4.txt'),delim_whitespace=True, index_col=["name"])
df5=pd.read_csv(os.path.join(dirpath, init, FCname, "splitfiles", 'perturb_' + dataset + '5.txt'),delim_whitespace=True, index_col=["name"])
attr=pd.concat([df1,df2,df3,df4,df5],axis=0)
attr.to_csv(os.path.join(dirpath, init, FCname, dataset+'.txt'), sep = ' ')
