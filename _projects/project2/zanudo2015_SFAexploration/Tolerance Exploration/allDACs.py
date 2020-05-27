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
    rawDAC = pd.DataFrame(index = range(60))
    tols = [2,3,4,5,6,8,10,12]
    for tol in tols:
        apop=pd.read_csv("sfa_A1_" + str(tol)+".txt",delim_whitespace=True,index_col=["name"]).round(tol)
        leuk=pd.read_csv("sfa_leuk1_" + str(tol) + ".txt",delim_whitespace=True,index_col=["name"]).round(tol)
        rawDAC.index = apop.columns.tolist()

        RONS = ["apoptosis","bid","caspase","ceramide","disc",
                "fas","fasl","fast","gpcr","gzmb","iap","ifngt","nfkb","pdgfr","pi3k","s1p","sphk1","tpl2","tradd"]

        I1 = list(leuk.index)
        I2 = list(apop.index)
        iterables = [I1, I2]
        mI = pd.MultiIndex.from_product(iterables, names=['leuk', 'apop'])
        df = pd.DataFrame(index = mI, columns = RONS)
        

        ##    DACall = pd.dataframe(columns = apop.columns 

        for index,row in leuk.iterrows():
            x=apop.apply(DAC, axis = 1, args =[row])
        ##        x = apop.round(decimals=2)
        ##        x.to_csv('check_this_out.csv', sep = ',', index_label = "name")
        ##        die
            xd=x.copy(deep=True).apply(disc,0).astype(np.int64)
            xd2 = xd[RONS]
            for index2,row in xd2.iterrows():
                df.loc[(index, index2)] = row
##            xd.to_csv("DAC/full_" + str(tol) + ".txt",sep=' ',index_label="name")
##            x.to_csv("DAC/full_" + str(tol) + "_RAW.txt",sep=' ',index_label="name")
            rawDAC['DAC_' + str(tol)] = x.iloc[0,]
##        df.to_csv("DAC/RONs_" + str(tol)+".txt",sep=' ',index_label=["leuk_attr", "apop_attr"])
    rawDAC.to_csv("DAC/RAW_all.txt", sep = " ", index_label = "tolerance")

main()
