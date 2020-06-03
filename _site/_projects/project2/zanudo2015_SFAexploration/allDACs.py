# ---------------
# allDACs.py calculates the direction of activity change (DAC) pairwise between
# attractors estimated with SFA from initial conditions in the basin of Leukemia
# and Apoptosis attractors of the Boolean model.
# --------------


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
    apop=pd.read_csv("sfa_apoptosis.txt",delim_whitespace=True,index_col=["name"])
    leuk=pd.read_csv("sfa_leukemia1.txt",delim_whitespace=True,index_col=["name"])

    RONS = ["apoptosis","bid","caspase","ceramide","disc",
            "fas","fasl","fast","gpcr","gzmb","iap","ifngt","nfkb",
            "pdgfr","pi3k","s1p","sphk1","tpl2","tradd"]

    I1 = list(leuk.index)
    I2 = list(apop.index)
    iterables = [I1, I2]
    mI = pd.MultiIndex.from_product(iterables, names=['leuk', 'apop'])
##        df = pd.DataFrame(index = mI, columns = RONS)
    df = pd.DataFrame(index = mI, columns = apop.columns)
    

    for index,row in leuk.iterrows():
        x=apop.apply(DAC, axis = 1, args =[row])
        xd=x.copy(deep=True).apply(disc,0).astype(np.int64)
        xd2 = xd
        for index2,row in xd2.iterrows():
            df.loc[(index, index2)] = row
    df.to_csv("DAC_results_L1A/DAC_all.txt",sep=' ',index_label=["leuk_attr", "apop_attr"])

main()
