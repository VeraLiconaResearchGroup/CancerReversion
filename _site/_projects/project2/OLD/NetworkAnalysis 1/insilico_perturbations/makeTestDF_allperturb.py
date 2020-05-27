#Make a dataframe of all insilico perturbation outcomes

def main():
    p = 6561

    test = []
    names = []

    for i in range(p):
        name = str(i+1).rjust(len(str(p)), '0')
        file = open('SFAoutputFC1/SFAoutput_full_FC1_' + name + '.txt').read().split('\n')
        attr = []
        names.append('perturb' + name)

        for n in range(len(file)):
            row = file[n].split('\t')
            if len(row)>1: #ignoring blank row at end of file
                if float(row[1]) > 0:
                    attr.append(1)
                elif float(row[1]) < 0:
                    attr.append(-1)
                elif float(row[1]) == 0:
                    attr.append(0)


        test.append(attr)

    outputfile = open('testSet_allPerturb.txt', 'w+')
    for j in range(len(test)):
        outputfile.write(names[j])
        outputfile.write('\t')
        for elem in test[j]:
            outputfile.write(str(elem))
            outputfile.write('\t')
        outputfile.write('\n')

    outputfile.close()

main()
