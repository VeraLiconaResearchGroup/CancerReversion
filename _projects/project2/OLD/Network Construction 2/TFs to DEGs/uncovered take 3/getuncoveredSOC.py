#Get uncovered SOC
import csv
import re
def main():
    run = 4
    inputfile = open('covered'+str(run)).read().split('\n')
    expr = open('MDA231_expressionMatrix.txt').read().split('\n')
    TFs = open('TFs_APIPA_9').read().split('\n')
    SOC = open('FunDEGs_FOC_LCC_noHKG_80').read().split('\n')
    outputfile=open('uncovered'+str(run),'w+')
    writer=csv.writer(outputfile, delimiter='\n')
    outputfile2=open('expm'+str(run),'w+')
    writer=csv.writer(outputfile2, delimiter='\n')

    n = 1
    covered = []
    for node in inputfile:
        covered.append(node)
        
    while n <run:
        file = open('covered'+str(n)).read().split('\n')
        for node in file:
            covered.append(node)
        n += 1

    uncovered = []
    i = 0
    for node in SOC:
        if node not in covered:
            i +=1
            uncovered.append(node)
    test = len(SOC)-i

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
