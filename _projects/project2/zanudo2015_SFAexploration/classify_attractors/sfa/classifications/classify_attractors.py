from re import *
import pandas as pd
import itertools

##def main():

##aronval=['-1','1','1','1','1','0','1','1'] #DAC forr apoptosis nodes
aronval=['-1','1','1','1','1','1','1'] #DAC for apoptosis nodes
##aronr=['iap','caspase','disc','ceramide','fas','gzmb','bid','apoptosis']
aronr=['iap','caspase','disc','ceramide','fas','bid','apoptosis']
aron=pd.DataFrame(aronval,index=aronr, columns = ['value'])
##canval=['1','1','0','0','0','0','1','1','1','1','1','1','1','1','1','1'] #DAC for leukemia nodes
##canval = ["-1","-1","-1","-1","-1","-1","1","1","1","1","1"]
##canval = ['0']*9
canval = ['-1','-1','-1','-1','-1','1','1','1','1']
##canr=['disc','caspase','tradd','ceramide',
##       'fas','apoptosis','fasl','fast','nfkb',
##       'tpl2','ifngt','pdgfr','gpcr','s1p','sphk1','pi3k']
canr=["apoptosis","caspase","ceramide","disc","fas","gpcr","pdgfr","s1p","sphk1"]
can=pd.DataFrame(canval,index=canr, columns = ['value'])

RONs = sorted(list(set(aronr + canr)))

df2=pd.read_csv('sfa_DAC_disc.txt',delim_whitespace=True,index_col=['name'], dtype = 'str')
df2 = df2[RONs]
df5 = pd.read_csv('sfa_DAC_disc_vsAPOP.txt',delim_whitespace=True,index_col=['name'], dtype = 'str')
df5 = df5[RONs]

candf = pd.DataFrame(columns = df2.columns)
candf.index.name = 'name'
apopdf = pd.DataFrame(columns = df2.columns)
apopdf.index.name = 'name'

df3 = df2[aron.index] #df2 with only apoptosis RONs
df4 = df5[can.index] #df5 with only leukemia RONs
##df4 = df2[can.index] #df5 with only leukemia RONs

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

otherdf.to_csv('classification_test/take2/other_attractors.txt', sep = " ")
candf.to_csv('classification_test/take2/leukemia_attractors.txt', sep = " ")
apopdf.to_csv('classification_test/take2/apoptosis_attractors.txt', sep = " ")

with open('classification_test/take2/leukemia_list.txt', 'w') as outfile:
    outfile.write("\n".join(leuk))

with open('classification_test/take2/apoptosis_list.txt', 'w') as outfile:
    outfile.write("\n".join(apop))

with open('classification_test/take2/other_list.txt', 'w') as outfile:
    outfile.write("\n".join(otherdf.index.tolist()))
           

##main()
