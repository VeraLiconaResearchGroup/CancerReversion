import pandas as pd
import sys

##1. read in logss sfa
##2. read in key for apoptosis and leukemia sfas
##3. compute DAC against one leukemia attractor
##4. write out files separately
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


##ref = int(sys.argv[1])
ref = 0
##logss = pd.read_csv('sfa_logss.txt', delim_whitespace = True, index_col = ['name'])
logss = pd.read_csv('../landscape_simulation/attr_logss.txt', delim_whitespace = True, index_col = ['name'])
refs = pd.read_csv('is_to_A_L_inBN.txt', delim_whitespace = True, index_col = ['Initial_state'])

leuks = refs[refs['label'] != "Apoptosis"]
is_ref = leuks.index.tolist()[ref]
label = leuks.loc[is_ref, 'label2']
is_ref= 'attr_001'

logss = logss.iloc[0:700, 0:5]

DACdf = logss.apply(DAC, axis =1, args = [logss.loc[is_ref,:]])
DACdf = DACdf.apply(disc, axis = 1)
##DAC.to_csv('Vs_' + label + '.txt', sep = " ")

