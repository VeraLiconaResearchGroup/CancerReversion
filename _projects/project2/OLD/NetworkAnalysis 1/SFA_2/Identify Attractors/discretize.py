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
    return df

