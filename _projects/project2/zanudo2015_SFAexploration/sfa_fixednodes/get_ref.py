import os
import numpy as np
import pandas as pd

def DAC(row,refval):

    return row-refval #calculates DAC for attractor 

def disc(row): #discrtizes results
    for i in range(len(row)):
        if row[i] > 0:
            row[i] = 1
        elif row[i] <0:
            row[i] = -1
        elif row[i] ==0:
            row[i] = 0
    return row

df = pd.read_csv('sfa_ref_logss.txt', delim_whitespace = True, index_col = ['name'])

# calculate DAC for the leukemeia and apoptosis reference attractors
x=df.apply(DAC, axis = 1, args =[df.iloc[0]])
x.columns = [col + '_DAC' for col in df.columns]

# discretize logss and DAC dfs
xd=x.copy(deep=True).apply(disc,0).astype(np.int64)
xd.to_csv('sfa_ref_DAC_disc.txt', sep =' ')
dfd=df.copy(deep=True).apply(disc,0).astype(np.int64)
dfd.to_csv('sfa_ref_logss_disc.txt', sep =' ')


# Concat the dataframes

dfall = pd.concat([dfd,xd], axis = 1)
dfall.to_csv('sfa_ref_both_disc.txt', sep =' ')

