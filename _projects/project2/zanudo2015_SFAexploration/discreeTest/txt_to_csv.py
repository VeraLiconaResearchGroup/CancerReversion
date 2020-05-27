import pandas as pd

l = ['leuk1', 'leuk2','A1', 'A2', 'A3', 'A4', 'A5', 'A6']

for name in l:
    file = 'sfa_' + name + '_traj'
    df = pd.read_csv(file+'.txt',delim_whitespace = True, header = None)
    df.to_csv(file+'.csv', index = False, header = False)
