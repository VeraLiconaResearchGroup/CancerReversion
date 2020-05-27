from re import *
import pandas as pd
import itertools


aron = {"apoptosis":1, "bid":1, "ceramide":1, "disc":1, "fas":1, "iap":-1}
lron = {"apoptosis":-1, "s1p":1, "ceramide":-1, "disc":-1, "fas":-1}
##lron = {"apoptosis":-1, "s1p":1, "ceramide":-1, "disc":-1, "fas":-1}
##aron = {"apoptosis":1, "bid":1, "ceramide":1, "disc":1, "fas":1, "iap":-1}
aron = pd.DataFrame(aron.values(), index = aron.keys(), columns = ['value'])
##aron.index = [n + '_DAC' for n in aron.index]
lron = pd.DataFrame(lron.values(), index = lron.keys(), columns = ['value'])
##lron.index = [n + '_DAC' for n in lron.index]


pd.options.display.float_format = '{:,.0f}'.format

RONs = list(set(aron.index.tolist() + lron.index.tolist()))

df2=pd.read_csv('sfa_DAC_disc.txt',delim_whitespace=True,index_col=['name'])
df5 = pd.read_csv('sfa_DAC_disc_vsAPOP.txt',delim_whitespace=True,index_col=['name'])

candf = pd.DataFrame(columns = df2.columns)
apopdf = pd.DataFrame(columns = df2.columns)

df3 = df2[aron.index] #df2 with only apoptosis RONs
df4 = df5[lron.index] #df2 with only leukemia RONs

a = 0
l = 0

for index, row in df3.iterrows():
    if row.tolist() == aron.loc[:,'value'].tolist():
        apopdf.loc[index] = df2.loc[index,]
        a += 1

for index, row in df4.iterrows():
    if row.tolist() == lron.loc[:,'value'].tolist():
        candf.loc[index] = df2.loc[index,]
        l += 1

leuk = candf.index.tolist()
apop = apopdf.index.tolist()


otherdf = df2.drop(index = leuk+apop)

print('There are ' + str(l) + ' leukemia attractors and ' + str(a)+ ' apopotosis attractors.')

apopdf.index.name = 'name'
candf.index.name = 'name'

otherdf.to_csv('classify_attractors2/other_attractors_sfa.txt', sep = " ")
candf.to_csv('classify_attractors2/leukemia_attractors_sfa.txt', sep = " ")
apopdf.to_csv('classify_attractors2/apoptosis_attractors_sfa.txt', sep = " ")

with open('classify_attractors2/leukemia_sfa.txt', 'w') as outfile:
    outfile.write("\n".join(leuk))

with open('classify_attractors2/apoptosis_sfa.txt', 'w') as outfile:
    outfile.write("\n".join(apop))

with open('classify_attractors2/other_sfa.txt', 'w') as outfile:
    outfile.write("\n".join(otherdf.index.tolist()))
           

