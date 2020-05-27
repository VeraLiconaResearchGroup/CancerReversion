# Determine if attractors in the same cluster have similar values for their nodes

from cluster_patterns import *
import re

attrs = open("Cluster Both Discrete/attractors_both_discrete.txt").read().split('\n')
##attrs = open("Cluster Both Discrete/test.txt").read().split('\n')
names = attrs[0].split(' ')
print(len(names))

cl_ca = [names]
cl_n = [names]

for line in attrs:
        row = line.split(' ')
        if row[0] in cancerous:
                cl_ca.append(line)
        elif row[0] in normal:
                cl_n.append(line)
          
def find_common(df):
    percent = {}
    for n in range(len(names)):
        one = 0
        none = 0
        zero = 0
        i = 1
        while i < len(df):
            row  = df[i].split(' ')
            if len(row)>1:
                    if row[n+1] == '1':
                        one +=1
                    elif row[n+1] == '-1':
                        none += 1
                    elif row[n+1] == '0':
                        zero += 1
            i += 1
        fone = round(one/(len(df)-1),3)
        fnone = round(none/(len(df)-1), 3)
        fzero = round(zero/(len(df)-1), 3)
        percent[names[n]] = ['Ones:', fone, 'Neg ones:', fnone, 'Zeros:', fzero]
    return percent


ca_perc = find_common(cl_ca)
norm_perc = find_common(cl_n)

with open('test_cancer_percent','w+') as f:
   for key,val in ca_perc.items():
       f.write(key+'\t'+str(val[1])+'\t'+str(val[3])+'\t'+str(val[5])+'\n') 

with open('test_normal_percent','w+') as f:
   for key,val in norm_perc.items():
       f.write(key+'\t'+str(val[1])+'\t'+str(val[3])+'\t'+str(val[5])+'\n') 

        
    
    

