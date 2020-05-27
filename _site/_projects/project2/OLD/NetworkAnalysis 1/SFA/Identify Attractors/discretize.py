# Discretize data

import csv

def discrete(df):

    for row in df:
        for i in range(len(row)):
            if i > 0:
                row[i] = float(row[i])
                if row[i] > 0:
                    row[i] = 1
                elif row[i] == 0:
                    row[i] = 0
                elif row[i] <0:
                    row[i] = -1
        
    with open('attractor_df_discrete.txt', 'w') as myfile:
        wr = csv.writer(myfile,quoting=csv.QUOTE_NONE,delimiter='\t')
        for row in df:
            wr.writerow(row)

