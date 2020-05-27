import scipy.spatial
import pandas as pd
import numpy as np

#DAC for readout nodes between boolean attractors (Apoptosis- Leukemia)
##booleanDAC = [1,1,1,1,1,1,0,0,-1,0,-1,0,0,-1,0,-1,-1,0,0]
b = {'apoptosis': 1, 'bid':1, 'ceramide': 1, 'disc':1, 'fas':1, 'iap':-1, 's1p':-1}
boolDAC = pd.DataFrame.from_dict(b, 'index', columns = ['value'])

df = pd.read_csv('sfa_fixednodes/DAC/DAC_A_L1_rons.txt', delim_whitespace = True, index_col = ["leuk_attr", "apop_attr"])
df1 = pd.read_csv('sfa_fixednodes/DAC/DAC_A_L2_rons.txt', delim_whitespace = True, index_col = ["leuk_attr", "apop_attr"])
df = pd.concat([df,df1], axis = 0)
df = df[boolDAC.index]
print(df)

hamming  = pd.DataFrame(columns = ['hamming_distance'], index = df.index)
hamming = df.apply(scipy.spatial.distance.hamming, 1, args = [boolDAC.value])

##hamming.to_csv('DAC_results_L1A/Hamming_distance_RONs.txt', sep= " ", index_label=["leuk_attr", "apop_attr"])
print(hamming.value_counts())

### Hamming distance for nodes without Boolean DAC of 0
##
##boolDAC2 = boolDAC[boolDAC["BooleanDAC"] !=0]
##hamming2 = pd.DataFrame(columns = ['hamming_distance'], index = boolDAC2.index)
##
##df2 = df.loc[:,boolDAC2.index]
##hamming = df2.apply(scipy.spatial.distance.hamming, 1, args = [boolDAC2["BooleanDAC"]])
##print(hamming.value_counts())
####hamming.to_csv('DAC_results_L1A/Hamming_distance_RONs_no0.txt', sep= " ", index_label=["leuk_attr", "apop_attr"])
