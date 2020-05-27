# Determine if attractors in the same cluster have similar values for their nodes

from cluster_patterns import *
import re

attrs = open("attractors.txt").read().split('\n')
names = attrs[0].split('\t')

cl_ca = []
cl_n = []

for line in attrs:
        for attr in cancerous:
                if re.search(str(attr) + '\t' + r'\b', line):
                        cl_ca.append(line)
        for attr in normal:
                if re.search(str(attr) + '\t' + r'\b', line):
                        cl_n.append(line)
            

def find_common(df):
    percent = {}
    for n in range(len(names[2:])):
        one = 0
        none = 0
        zero = 0
        i = 2
        while i <= len(df)-1:
            row  = df[i].split('\t')
            if row[n+2] == '1':
                one +=1
            elif row[n+2] == '-1':
                none += 1
            elif row[n+2] == '0':
                zero += 1
            i += 1
        fone = round(one/(len(df)-2),3)
        fnone = round(none/(len(df)-2), 3)
        fzero = round(zero/(len(df)-2), 3)
        percent[names[n+2]] = ['Ones:', fone, 'Neg ones:', fnone, 'Zeros:', fzero]
    return percent


##dfs = [cl_ca, cl_n]
##for df in dfs:
##        find_common(df)

ca_perc = find_common(cl_ca)
norm_perc = find_common(cl_n)





        
    
    

