from re import *
import pandas as pd
import itertools

def main():
    
    aronval=['0','1','1','1','1','1','1','1']
    aronr=['iap','caspase','disc','ceramide','fas','gzmb','bid','apoptosis']
    aron=pd.DataFrame(aronval,index=aronr, columns = ['value'])
    canval=['0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1']
    canr=['disc','caspase','tradd','ceramide',
           'fas','apoptosis','fasl','fast','nfkb',
           'tpl2','ifngt','pdgfr','gpcr','s1p','sphk1','pi3k']
    can=pd.DataFrame(canval,index=canr, columns = ['value'])

    df2=pd.read_csv('boolnet_attractors_RONS.txt',delim_whitespace=True,index_col=['name'], dtype = 'str')



    candf = pd.DataFrame(columns = df2.columns)
    candf.index.name = 'name'
    apopdf = pd.DataFrame(columns = df2.columns)
    apopdf.index.name = 'name'

    df3 = df2[aron.index] #df2 with only apoptosis RONs
    df4 = df2[can.index] #df2 with only leukemia RONs

    a = 0
    l = 0

    for index, row in df3.iterrows():
        if row.tolist() == aron.loc[:,'value'].tolist():
            apopdf.loc[index,] = df2.loc[index,]
            a += 1

    for index, row in df4.iterrows():
        if row.tolist() == can.loc[:,'value'].tolist():
            candf.loc[index,] = df2.loc[index,]
            l += 1

    leuk = candf.index.tolist()
    apop = apopdf.index.tolist()


    otherdf = df2.drop(index = leuk+apop)

    print('There are ' + str(l) + ' leukemia attractors and ' + str(a)+ ' apopotosis attractors.')

    otherdf.to_csv('other_attractors.txt', sep = " ")
    candf.to_csv('leukemia_attractors.txt', sep = " ")
    apopdf.to_csv('apoptosis_attractors.txt', sep = " ")

    with open('leukemia.txt', 'w') as outfile:
        outfile.write("\n".join(leuk))

    with open('apoptosis.txt', 'w') as outfile:
        outfile.write("\n".join(apop))

    with open('other.txt', 'w') as outfile:
        outfile.write("\n".join(otherdf.index.tolist()))
               

main()
