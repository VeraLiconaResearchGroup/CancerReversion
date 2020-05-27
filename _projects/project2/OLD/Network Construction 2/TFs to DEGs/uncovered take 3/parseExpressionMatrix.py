# Get Expression Matrix for Pearson

import re
def main():
    expr = open('MDA231_expressionMatrix.txt').read().split('\n')
    uncovered = open('uncovered').read().split('\n')
    TFs = open('TFs_APIPA_9').read().split('\n')
    i = 0
    data = []

    for node in uncovered:
        for line in expr:
            row = line.split('\t')
            if row[0]==node:
                print(line)
                j +=1
    for node in TFs:
        for line in expr:
            row= line.split('\t')
            if row[0]==node:
                print(line)
                j +=1
    print(j)
            
main()
