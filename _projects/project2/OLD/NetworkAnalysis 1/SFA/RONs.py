# DAC

import re

def main():
    data = open("FC_all").read().split('\n')
    RON = open("candidateRONs").read().split('\n')

    n = 0
    for line in data:
        row = line.split('\t')
        for node in RON:
            if row[0] == node:
                print(line)
                n +=1

    print(n)
main()
