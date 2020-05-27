# Round DFs
import pandas as pd
tols = [2,3,4,5,6,8,10,12]
inds = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'L1', 'L2']

for tol in tols:
    for ind in inds:
        name = 'tol'+str(tol) + '/sfa_' + ind + '_states.txt'
        df = pd.read_csv(name, delim_whitespace = True, index_col = ['name'])
        df = df.round(tol-1)
        if ind == 'A1':
            apop = df.copy(deep = True)
        elif ind[0] == 'A':
            apop =  pd.concat([apop, df], axis= 0)
        df.to_csv(name, sep  = ' ')
    apop.to_csv('tol'+str(tol) + '/sfa_Apop_states_all.txt', sep = ' ')

