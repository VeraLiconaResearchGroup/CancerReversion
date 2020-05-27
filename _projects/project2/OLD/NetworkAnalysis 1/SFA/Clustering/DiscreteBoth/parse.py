# make dataframes of the attractors that always cluster with 231 and always cluster witj 10A
import csv

def main():

    ca = open('cancerous_cluster').read().split('\n')
    norm = open('normal_cluster').read().split('\n')
    attrs = open('attractors.txt').read().split('\n')

    cancerous = []
    normal = []
    test = []
    
    for line in attrs:
        row = line.split('\t')
        if row[0] in ca:
            cancerous.append(line)
        elif row[0] in norm:
            normal.append(line)
        else:
            test.append(line)

    outputfile=open('cancerousTrain.txt','w+')

    outputfile.write(attrs[0])
    outputfile.write('\n')
    for line in cancerous:
        outputfile.write(line)
        outputfile.write('\n')

    outputfile=open('normalTrain.txt','w+')

    outputfile.write(attrs[0])
    outputfile.write('\n')
    for line in normal:
        outputfile.write(line)
        outputfile.write('\n')


    outputfile=open('Test.txt','w+')

    for line in test:
        outputfile.write(line)
        outputfile.write('\n')

        
    outputfile.close()

main()

    
    
