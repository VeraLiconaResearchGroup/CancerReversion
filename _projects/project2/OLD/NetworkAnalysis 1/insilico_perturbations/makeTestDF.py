# Make test set with all perturbs we thought were succesfful because they flipped all 8 nodes

def main():
    file = open('perturbations of interest_FC1').read().split('\n')

    test = []
    
    for name in file:
        file2 = open('SFAoutputFC1/SFAoutput_full_FC1_' + str(name) + '.txt').read().split('\n')
        attr = []

        for n in range(len(file2)-1):
            row = file2[n].split('\t')
            if float(row[1]) > 0:
                attr.append(1)
            elif float(row[1]) < 0:
                attr.append(-1)
            elif float(row[1]) == 0:
                attr.append(0)

        test.append(attr)


    outputfile = open('testSet.txt', 'w+')
    for n in range(len(test)):
        outputfile.write('perturb' + str(file[n]))
        outputfile.write('\t')
        for elem in test[n]:
            outputfile.write(str(elem))
            outputfile.write('\t')
        outputfile.write('\n')

    outputfile.close()

main()
