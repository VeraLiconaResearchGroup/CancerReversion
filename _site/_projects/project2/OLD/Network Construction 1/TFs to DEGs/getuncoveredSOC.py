#Get uncovered SOC

import re
def main():
    inputfile = open('Covered_SOC8').read().split('\n')
    SOC = open('FunDEGs_SOC_exprnoHKG_316.txt').read().split('\n')
    
    i = 0
    for node in SOC:
        if node not in inputfile:
            i +=1
            print(node)
    print(i, ';', 316-i)
main()
