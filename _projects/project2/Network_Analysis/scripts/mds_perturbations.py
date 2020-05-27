#------------------------------------------
# mds_perturbations.py runs metric mds on the attractors from virtual screeenings for 2 - 10 dimensions
#
# Requires user specification of the dataset of reference attractors and attractors from virtual screeenings to use
# and the path to the location of virtual screenings
#
# INPUTS:
# 1. Dataset of reference attractors
# 2. Dataset of attractors from virtual screenings
#
# OUTPUTS:
# 1. Stress of mds applied with 2 to 10 dimensions
# 2. mds_dataset_2dim.txt: Coordinates with 2 dimensions
# 3. mds_dataset_3dim.txt: Coordinates with 3 dimensions
#------------------------------------------

import pandas as pd
import sklearn.neighbors
import os
import sys
import numpy as np
from sklearn import manifold

############### Inputs ###############
folder = sys.argv[1] #Folder containing data from virtual screenings
dataset  = sys.argv[2] #Dataset on which to run mds
#####################################

#Read in results of virtual screenings
data = pd.read_csv(os.path.join(folder, 'perturb_'+ dataset + '.txt'), delim_whitespace = True, index_col = ["name"])

#Read in reference attractors
ref = pd.read_csv(os.path.join('inputfiles', 'ref_attrs_'+ dataset + '.txt'), delim_whitespace = True)

#Combine reference attractors and virtual screening attractors
data = pd.concat([ref, data], sort = True)

#Calculate euclidean distance between attractors
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
A = dist.pairwise(data)

seed = np.random.RandomState(seed=3)

stress = {}
for k in range(2, 11):
    #Run MDS with dimensions from 2 to 10
    mds = manifold.MDS(n_components=k, max_iter=3000, eps=1e-9, random_state=seed, dissimilarity="precomputed", n_jobs= -1)
    #record stress value
    stress[str(k)] = mds.fit(A).stress_
    if k == 2: #Write out dimensions
        pos = mds.fit(A).embedding_
        out = pd.DataFrame(pos, index = data.index, columns = ["PC1", "PC2"])
        out.to_csv(os.path.join(folder, 'mds',"mds_" + dataset + "_" + str(k) + "dim.txt"), sep= ' ')
    if k == 3: #Write out dimensions
        pos = mds.fit(A).embedding_
        out = pd.DataFrame(pos, index = data.index, columns = ["PC1", "PC2", "PC3"])
        out.to_csv(os.path.join(folder, 'mds',"mds_" + dataset + "_" + str(k) + "dim.txt"), sep= ' ')

print(stress)

#Write out file with stress at each dimension
stress = pd.DataFrame.from_dict(stress, orient = 'index', columns = ['Stress'])
stress.to_csv(os.path.join(folder,'mds', "mds_" + dataset + "_stress"+ str(i)+".txt"), sep= " ")
