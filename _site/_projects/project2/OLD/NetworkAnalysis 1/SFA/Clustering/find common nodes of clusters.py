# Determine if attractors in the same cluster have similar values for their nodes

clusters = open("clustering_disc.txt").read().split('\n')
names = clusters[0].split('\t')

c1 = []
c2 = []
c3 = []

for line in clusters:
        row = line.split('\t')
        if row[1] == '1':
            c1.append(line)
        elif row[1] == '2':
            c2.append(line)
        elif row[1] == '3':
            c3.append(line)
            
dfs = [c1, c2, c3]

print(len(c3))

def find_common(df):
    percent = {}
    for n in range(len(names[2:])):
        one = 0
        none = 0
        zero = 0
        i = 2
        while i <= len(df)-1:
            row  = df[i].split('\t')
            if row[n+2] == '1':
                one +=1
            elif row[n+2] == '-1':
                none += 1
            elif row[n+2] == '0':
                zero += 1
            i += 1
        fone = round(one/(len(df)-2),3)
        fnone = round(none/(len(df)-2), 3)
        fzero = round(zero/(len(df)-2), 3)
        percent[names[n+2]] = ['Ones:', fone, 'Neg ones:', fnone, 'Zeros:', fzero]
    return percent





        
    
    

