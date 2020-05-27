# Find attractors always clustered with 10A and 231
# Input = Dataframe with attractors as each row, and columns being the different clustering
# methods used. Each entry is the cluster assignment for each attractor in each clustering method

file = open("cluster_assignments_discrete.txt").read().split('\n')
##file = open("Cluster Both Discrete/test_cluster").read().split('\n')
cancerous = []
normal = []

a231 = file[1].split(' ')[1:]
a10a = file[2].split(' ')[1:]

for line in file:
    row = line.split(' ')
    n = 0
    m = 0
    for i in range(len(row[1:])):
        if row[1:][i] == a231[i]:
            n += 1
    if n == len(row[1:]):
        cancerous.append(row[0])
    for i in range(len(row[1:])):
        if row[1:][i] == a10a[i]:
            m += 1
    if m == len(row[1:]):
        normal.append(row[0])
    
##    print(cancerous)
##    print(normal)

overlap = []
for at in cancerous:
    if at in normal:
        overlap.append(at)

print("cancerous: ", len(cancerous))
print("normal: ", len(normal))
print("OVERLAP: ", len(overlap), overlap)
    


    
