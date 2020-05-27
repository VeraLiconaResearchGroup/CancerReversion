import scipy.spatial
import pandas as pd
import numpy as np

#DAC for readout nodes between boolean attractors (Apoptosis- Leukemia)
DAC = [0,0,0,0,0,0,0,0]
RON_0 = ['fasl','fast', 'gzmb', 'ifngt', 'nfkb', 'pi3k', 'tpl2', 'tradd']
tols = [2,3,4,5,6,8,10,12, '_mache']

DAC_no0 = [1,1,1,1,1,1,-1,-1,-1,-1,-1]

for tol in tols:
    folder = "tol" + str(tol)
    df = pd.read_csv(folder + "/DAC_A_L1_rons.txt", delim_whitespace = True, index_col = ["leuk_attr", "apop_attr"])
    df2 = df[RON_0]
    
##    boolDAC = pd.DataFrame(DAC, index = df2.columns, columns = ["DAC"])
##
##    hamming = pd.DataFrame(columns = ['hamming_distance'], index = df2.index)
##
##    hamming = df2.apply(scipy.spatial.distance.hamming, 1, args = [DAC])
##    hamming.to_csv(folder+'/Hamming_distance_0s.txt', sep= " ", index_label=["leuk_attr", "apop_attr"])
##    print(hamming.value_counts())

    df3 = df.drop(RON_0, 1)
    boolDAC = pd.DataFrame(DAC_no0, index = df3.columns, columns = ["DAC"])
    
    hamming = pd.DataFrame(columns = ['hamming_distance'], index = df3.index)

    hamming = df3.apply(scipy.spatial.distance.hamming, 1, args = [DAC_no0])
##    hamming.to_csv(folder+'/Hamming_distance_0s.txt', sep= " ", index_label=["leuk_attr", "apop_attr"])
    print(hamming.value_counts())

    

