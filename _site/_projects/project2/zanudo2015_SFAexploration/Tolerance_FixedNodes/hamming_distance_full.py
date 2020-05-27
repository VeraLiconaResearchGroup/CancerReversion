import scipy.spatial
import pandas as pd
import numpy as np

#DAC for readout nodes between boolean attractors (Apoptosis- Leukemia)
booleanDAC = [1,1,1,1,1,1,0,0,-1,0,-1,0,0,-1,0,-1,-1,0,0]
tols = [2,3,4,5,6,8,10,12, '_mache']

for tol in tols:
    folder = "tol" + str(tol)
    df = pd.read_csv(folder + "/DAC_A_L1_rons.txt", delim_whitespace = True, index_col = ["leuk_attr", "apop_attr"])

    boolDAC = pd.DataFrame(booleanDAC, index = df.columns, columns = ["BooleanDAC"])

    hamming  = pd.DataFrame(columns = ['hamming_distance'], index = df.index)


    hamming = df.apply(scipy.spatial.distance.hamming, 1, args = [booleanDAC])
##    hamming.to_csv('DAC_results_L1A/Hamming_distance_RONs.txt', sep= " ", index_label=["leuk_attr", "apop_attr"])
    print(hamming.value_counts())

    # Hamming distance for nodes without Boolean DAC of 0

##    boolDAC2 = boolDAC[boolDAC["BooleanDAC"] !=0]
##    hamming2 = pd.DataFrame(columns = ['hamming_distance'], index = boolDAC2.index)
##
##    df2 = df.loc[:,boolDAC2.index]
##    hamming = df2.apply(scipy.spatial.distance.hamming, 1, args = [boolDAC2["BooleanDAC"]])
####    print(hamming.value_counts())
##    hamming.to_csv('DAC_results_L1A/Hamming_distance_RONs_no0.txt', sep= " ", index_label=["leuk_attr", "apop_attr"])
