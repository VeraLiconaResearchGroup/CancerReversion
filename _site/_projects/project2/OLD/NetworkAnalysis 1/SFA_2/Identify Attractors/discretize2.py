# Discretize data
import csv
def main():
    file = open("attractor_df.txt").read().split('\n')

    outputfile=open('attractor_df_discrete.txt','w+')
    for line in file:
            row = line.split('\t')
            outputfile.write(row[0] + '\t')
##            print(row)
            for i in range(len(row)):
                if i > 0:
                    row[i] = float(row[i])
##                    print(row[i])
                    if row[i] > 0:
                        row[i] = 1
                        outputfile.write(str(row[i]) + '\t')
                    elif row[i] == 0:
                        row[i] = 0
                        outputfile.write(str(row[i]) + '\t')
                    elif row[i] <0:
                        row[i] = -1
                        outputfile.write(str(row[i]) + '\t')
            outputfile.write('\n')
    outputfile.close()

main()
