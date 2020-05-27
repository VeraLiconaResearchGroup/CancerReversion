# Find attractors always clustered with 10A and 231


file = open("cluster_assignments.txt").read().split('\n')
cancerous = []
normal = []

for line in file:
    row = line.split(' ')
    if row[0] == "attractor_231":
        a231 = row[1:]
    elif row[0] == "attractor_10A":
        a10a = row[1:]

for line in file:
    row = line.split(' ')
    n = 0
    m = 0
    for i in range(len(row[1:])):
        if row[1:][i] == a231[i]:
            n += 1
    if n >= .9*len(row[1:]):
        cancerous.append(row[0])
    for i in range(len(row[1:])):
        if row[1:][i] == a10a[i]:
            m += 1
    if m >= .9*len(row[1:]):
        normal.append(row[0])
    
##    print(cancerous)
##    print(normal)

overlap = []
for at in cancerous:
    if at in normal:
        overlap.append(at)

print("cancerous: ", len(cancerous))
print("normal: ", len(normal))
print("OVERLAP: ", overlap)


    
