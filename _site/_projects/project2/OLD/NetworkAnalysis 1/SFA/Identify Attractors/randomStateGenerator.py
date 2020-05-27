# Generate Random Set of Basal Conditions

import random
import numpy as np
import re

def generateBasalState(num_nodes, num_conditions):
    sets = []
    while len(sets)  < num_conditions:
        temp = tuple(np.random.randint(0,2, size = num_nodes))
        sets.append(temp)
        sets = list(set(tuple(sets)))

    n = 1
    for ls in sets:
        ls = list(ls)
        outputfile=open('test/basal' + str(n).rjust(len(str(num_conditions)), '0') + '.txt','w+')
        n +=1
        for elem in ls:
            elem = str(elem)
            outputfile.write(elem)
            outputfile.write('\n')
        if n % 100 == 0:
            print(n)
    print("Basal Levels Generated")
                
