# Find potential new readout nodes

from ExploreNodesinClusters import *


#ca_perc is a dictionary detailing the percent of attractors in the cancerous cluster with 1s, 0s, and -1s for each node
#norm_perc is the same but for the normal cluster
ls = []
ls2 = []

ca_perc = find_common(cl_ca)
norm_perc = find_common(cl_n)

for key,val in ca_perc.items():
    val2 = norm_perc[key]
    if val[1] >= .7:
        ls.append(key)
    if val2[1] >=.7:
        ls2.append(key)

print(ls)
print(ls2)

print("Nodes expressed in 70% of cancer attractors but not normal:")
for node in ls:
	if node not in ls2:
		print(node)

print('\n')
print("Nodes expressed in 70% of normal attractors but not cancer:")
for node in ls2:
	if node not in ls:
		print(node)
