#-------------------------------------------
# check_coverage.py is a script used to identify the targets of each transcription factor
#
# INPUTS:
# 1. uncoveredSOC1: Nodes that need a transcription factor
# 2. data.txt: File with IPA TFs and their targets
# 3. a.txt: a list of expressed TFs from IPA
#
# OUTPUTS:
# 1. A list of Second Order FunDEGs that are covered by the TFs
#-------------------------------------------
import re

def unique(list, thing):
    if thing not in list:
        list.append(thing)


def main():
    uncovered = open('uncoveredSOC1').read().split('\n')
    data = open('data.txt').read().split('\n')
    a = open('a.txt').read().split('\n')
    
    i = 0
    covered = []
    TF_new = []
    
    for node in a:
        for line in data:
            row = line.split('\t')
            if node == row[0]:
                targets = row[-1]
                targets = targets.split(',')
##              print(targets)
                for target in targets:
                    if target in uncovered:
                        unique(covered, target)
                        i += 1
                        unique(TF_new, node)


    print("TFs:", TF_new)
    print("targets:", covered)
    print(i)

main()
