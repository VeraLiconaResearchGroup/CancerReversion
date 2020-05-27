# Generate Random Set of Basal Conditions
import random
import numpy as np
import re
import sys
import time
import pandas as pd

interval = [0,1] #list of possible number coniditions to generate

def getRand(num_nodes, num_conditions):
    sets = []
    while len(sets)  < num_conditions:
        temp = tuple(np.random.randint(interval[0],interval[-1]+1, size = num_nodes))
        sets.append(temp)
        if len(sets) == num_conditions:
            sets = list(set(tuple(sets)))
    return(sets)

            
def generateBasalState(nodes,num_nodes, num_conditions, m, out_folder):
    # Determine decomposition of n into smaller sets of nodes
    n1 = num_nodes//m # Number of times m goes into n
    n2= num_nodes%m # Remainder of n divided by m

    # Generate lists of lists of random states of size n1 and n2
    ndivm = getRand(m, len(interval)**m)
    nmodm = getRand(n2, len(interval)**n2)

    # Initialize a list of initial states that must be combined. Length should be n1+1
    init = []
    for i in range(n1):
        init.append(ndivm)
    if n2>0:
        init.append(nmodm)


    if num_conditions < len(interval)**num_nodes:
        print('Generating ', num_conditions, ' Basal States')
        final = []
        while len(final) < num_conditions:
            thing = []
            for k in range(len(init)):
                thing = thing + list(random.choice(init[k]))
            final.append(tuple(thing))

            if len(final) == num_conditions:
                final = list(set(tuple(final)))

    else:
        print('Generating All Possible Basal States')
        # Initialize a list to hold all list combinations as we add lists one by one
        iterate = [init[0]] # Start with first list in init
        init.pop(0) # No loger need this list in init. If only one list in init, we're done.

        #Goal: Combine lists of basal states of size n1 and n2 until we get a list of basal states of size num_nodes
        while len(init) > 0: # Repeat this until there's nothing left in init
            ls = iterate[0]
            temp = []
            for thing in ls: #for every item in the first list of basal states of size n1 in init
                for elem in init[0]: #for every item in the second list of basal states of size n1 or n2 in init
                    temp.append(thing + elem) #add the items together to get a list of size n1+n1 or n1+n2 and add this to our temporary list
            iterate.append(temp) #append the temp list to our iterate list. We will add the elements of the next list in init to the elements of this list
            iterate.pop(0) # No longer need the list of basal states of size n1
            init.pop(0)

        final = iterate[-1]
        print(len(final))

    assert num_conditions == len(final), "Error: incorrect number of conditions generated"
    assert len(final[0]) == num_nodes, "Error: incorrect number of nodes"
    print(num_conditions, ' Basal States Generated')
    print('Writing Results...')

    basal_states = pd.DataFrame(index=nodes)
    for ls in final:
        basal_states['Perturb_' + str(final.index(ls)+1).rjust(len(str(num_conditions)), '0')] = list(ls)
    basal_states.to_csv(out_folder + 'basal_states.txt', sep=' ',index_label="name")
    return basal_states

