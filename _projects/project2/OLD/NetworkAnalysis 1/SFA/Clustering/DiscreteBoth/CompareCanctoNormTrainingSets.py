# Determine if attractors in the same cluster have similar values for their nodes

cancerous = open("cancerousTrain.txt").read().split('\n')
normal = open("normalTrain.txt").read().split('\n')
names = cancerous[0].split('\t')

def find_common(df):
    percent = {}
    for n in range(len(names[1:])):
        one = 0
        none = 0
        zero = 0
        i = 1
        while i < len(df):
            row  = df[i].split('\t')
            if row[n+1] == '1':
                one +=1
            elif row[n+1] == '-1':
                none += 1
            elif row[n+1] == '0':
                zero += 1
            i += 1
        fone = round(one/(len(df)-1),3)
        fnone = round(none/(len(df)-1), 3)
        fzero = round(zero/(len(df)-1), 3)
        percent[names[n+1]] = ['Ones:', fone, 'Neg ones:', fnone, 'Zeros:', fzero]
    return percent

ca = find_common(cancerous)
print(ca)
outputfile = open('cancerTrain_stats', 'w+')
outputfile.write('gene\tOnes\tNegOnes\tZeros\n')
for key, value in ca.items():
        outputfile.write(key)
        outputfile.write('\t')
        m = 1
        while m < len(value):
                outputfile.write(str(value[m]))
                outputfile.write('\t')
                m += 2
        outputfile.write('\n')
outputfile.close()

norm = find_common(normal)
outputfile = open('normalTrain_stats', 'w+')
outputfile.write('gene\tOnes\tNegOnes\tZeros\n')
for key, value in norm.items():
        outputfile.write(key)
        outputfile.write('\t')
        m = 1
        while m < len(value):
                outputfile.write(str(value[m]))
                outputfile.write('\t')
                m += 2
        outputfile.write('\n')
outputfile.close()

        
    
    

