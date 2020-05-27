# Get Expression Matrix for Pearson

import re
def main():
    inputfile = open('MDA231_expressionMatrix.txt').read().split('\n')
    nodes = open('uncoveredSOC8').read().split('\n')
    TFs = open('TFs_APIPA_500_7.txt').read().split('\n')
    i = 0
    data = []

    for line in inputfile:
        row = line.split('\t')
        if row[0] in nodes:
            data.append(row[0])
            i += 1
            print(line)
        elif row[0] in TFs:
            data.append(row[0])
            i += 1
            print(line)
    print(i)

    print('No data:')
    for node in nodes:
        if node not in data:
            print(node)

main()
