# Generate Random Set of Basal Conditions

import random
import numpy as np
import re

def main():

    num_nodes = 8 #number of nodes in FC set
    num_perturbations = 3**8 #Number of possible preturbations
    
    sets = []
    while len(sets)  < num_perturbations:
        temp = tuple(np.random.randint(-1,2, size = num_nodes))
        sets.append(temp)
        sets = list(set(tuple(sets)))
        
    n = 1
    for ls in sets:
        ls = list(ls)
        outputfile=open('FCbasal_perturbation/FC_perturbation_' + str(n).rjust(len(str(num_perturbations)), '0') + '.txt','w+')
        n +=1
        for elem in ls:
            elem = str(elem)
            outputfile.write(elem)
            outputfile.write('\n')
        if n % 100 == 0:
            print(n)
    print("Basal Levels Generated")

main()
                
