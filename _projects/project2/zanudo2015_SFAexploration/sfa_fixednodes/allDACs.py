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

def main():
    apop=pd.read_csv("sfa_Apop_all.txt",delim_whitespace=True,index_col=["name"])
    leuk=pd.read_csv("sfa_L2_states.txt",delim_whitespace=True,index_col=["name"])

    RONS = ["apoptosis","bid","caspase","ceramide","disc",
            "fas","fasl","fast","gpcr","gzmb","iap","ifngt","nfkb","pdgfr","pi3k","s1p","sphk1","tpl2","tradd"]

    I1 = list(leuk.index)
    I2 = list(apop.index)
    iterables = [I1, I2]
    mI = pd.MultiIndex.from_product(iterables, names=['leuk', 'apop'])
    df = pd.DataFrame(index = mI, columns = RONS)

    dfall = pd.DataFrame(index = mI, columns = apop.columns)


    for index,row in leuk.iterrows():
        x=apop.apply(DAC, axis = 1, args =[row])
        xd=x.copy(deep=True).apply(disc,0).astype(np.int64)
##        xd2 = xd[RONS]

        for index2,row in xd.iterrows():
            df.loc[(index, index2),] = xd.loc[index2,RONS]
            dfall.loc[(index, index2),] = xd.loc[index2,:]
    dfall.to_csv("DAC/DAC_A_L2_all.txt",sep=' ',index_label=["leuk_attr", "apop_attr"])
##    df.to_csv("DAC/DAC_A_L1_rons.txt",sep=' ',index_label=["leuk_attr", "apop_attr"])

main()
