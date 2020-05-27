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
    RON_0 = ['fasl','fast', 'gzmb', 'ifngt', 'nfkb', 'pi3k', 'tpl2', 'tradd']
    tols = [2,3,4,5,6,8,10,12, '_mache']
    for tol in tols:
        folder = "tol" + str(tol)
        apop=pd.read_csv(folder + "/sfa_Apop_states_all.txt",delim_whitespace=True,index_col=["name"])
        leuk=pd.read_csv(folder +"/sfa_L2_states.txt",delim_whitespace=True,index_col=["name"])

        RONS = ["apoptosis","bid","caspase","ceramide","disc",
                "fas","fasl","fast","gpcr","gzmb","iap","ifngt","nfkb","pdgfr","pi3k","s1p","sphk1","tpl2","tradd"]

        I1 = list(leuk.index)
        I2 = list(apop.index)
        iterables = [I1, I2]
        mI = pd.MultiIndex.from_product(iterables, names=['leuk', 'apop'])
        df = pd.DataFrame(index = mI, columns = RONS)
        c_correct0 = 0
        c_incorrect0 = 0
        

        ##    DACall = pd.dataframe(columns = apop.columns 

        for index,row in leuk.iterrows():
            x=apop.apply(DAC, axis = 1, args =[row])
        ##        x = apop.round(decimals=2)
        ##        x.to_csv('check_this_out.csv', sep = ',', index_label = "name")
        ##        die
            xd=x.copy(deep=True).apply(disc,0).astype(np.int64)
            xd2 = xd[RONS]
            xd3 = xd2[RON_0]

            for index2,row in xd2.iterrows():
                df.loc[(index, index2),] = list(row)
                l = df.loc[(index, index2), RON_0]
                l2 = [abs(n) for n in l]
                c_correct0 += (8-sum(l2))
                l3 = [abs(n) for n in list(row)]
                c_incorrect0 += 11 - sum(l3) +sum(l2)
            p_correct0 = c_correct0/(8*df.shape[0])*100
            p_incorrect0= c_incorrect0/(11*df.shape[0])*100
        print('tolerance: ', tol)
        print('percent correct 0: ', p_correct0)
        print('percent incorrect 0: ', p_incorrect0)
            
        df.to_csv(folder + "/DAC_A_L2_rons.txt",sep=' ',index_label=["leuk_attr", "apop_attr"])

main()
