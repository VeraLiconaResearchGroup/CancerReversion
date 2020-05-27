#-----------------------------------------------
# getuncovered.py Finds FunDEGs without a knocn TF regulator and generates the
# expression matrix of uncovered nodes + TFs to use in the next Paerson correlation run
#
# INPUTS:
# 1. A matrix of MDA-MB-231 expression data
# 2. A list of TFs
# 3. A list of FunDEGs
# 4. covered*: A list of FunDEGs with known TF regulators
#
# OUTPUTS:
# 1. uncovered*: A list of FunDEGs that still don't have a known TF regulator
# 2. expm*: An expression matrix for uncovered FunDEGs and TFs
#-----------------------------------------------

import csv
import re
def main():
    run = 4
    expr = open('MDA231_expressionMatrix.txt').read().split('\n')
    TFs = open('TFs_APIPA_9').read().split('\n')
    FunDEG = open('FunDEGs_FOC_LCC_noHKG_80').read().split('\n')
    
    outputfile=open('uncovered'+str(run),'w+')
    writer=csv.writer(outputfile, delimiter='\n')
    outputfile2=open('expm'+str(run),'w+')
    writer=csv.writer(outputfile2, delimiter='\n')

    n = 1
    covered = []
    while n <=run:
        file = open('covered'+str(n)).read().split('\n')
        for node in file:
            covered.append(node)
        n += 1

    uncovered = []
    i = 0
    for node in FunDEG:
        if node not in covered:
            i +=1
            uncovered.append(node)
    test = len(FunDEG)-i

    uncovered2 = '\n'.join(uncovered)
    outputfile.write(uncovered2)
    outputfile.close()

    j = 0
    matrix = []

    for node in uncovered:
        for line in expr:
            row = line.split('\t')
            if row[0]==node:
                matrix.append(line)
                j +=1
    for node in TFs:
        for line in expr:
            row= line.split('\t')
            if row[0]==node:
                matrix.append(line)
                j +=1
    print(j)

    matrix = '\n'.join(matrix)
    outputfile2.write(matrix)
    outputfile2.close()
   

main()
