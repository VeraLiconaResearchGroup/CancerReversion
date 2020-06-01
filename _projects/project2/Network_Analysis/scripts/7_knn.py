# -----------------------------------------------------------
# knn.py Runs k-nearest neighbors using reference attractors as training set to classify the results of virtual screenings
# 
# Requires user specification of the dataset to use, the number of clusters in training set, their labels, and the label of the goal cluster(s)
#
# INPUTS:
# 1. Reference Attractors
# 2. Dataframe of attractors from virtual screenings
#
# OUTPUTS:
# 1. knni.txt: Labels for each attractor when classified with i nearest neighbors
# 2. knni_goal.txt: Attractors classified in the goal cluster when using i nearest neighbors
# 3. knni_distance.txt: Distance between each attractor from virtual screenings and the attractors in the training set
# 4. knni_index.txt: The index of the nearest neighbors of each attractor ordered from closest to furthest
#-----------------------------------------------------------

import pandas as pd
import sklearn.neighbors as neighbors
from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import sys
import tables
import os
import re


dedef main():
    ############ inputs#################
    dataset = sys.argv[1] # Dataset for classification (logss, DAC, both, or disc versions)
    pert_folder = sys.argv[2] # Folder holding attractors from virtual screenings
    metric = sys.argv[3] # Distance metric (euclidean or hamming) for knn
    ncl = int(sys.argv[4]) # Number of clusters in training set

    ##################################
    if metric == 'minkowski':
        knn_folder = os.path.join(pert_folder, 'knn_' + dataset)
    elif metric == 'hamming':
        knn_folder = os.path.join(pert_folder, 'knn_' + dataset + '_hamming')

    reffile = 'ref_attrs_' + dataset + '.txt'
    ref = pd.read_csv(os.path.join("reference_attrs", reffile), delim_whitespace=True, index_col = 'name') # Read in reference attractors

    df_perturb = pd.read_csv(os.path.join(pert_folder, 'perturb_' + dataset + '.txt'), delim_whitespace = True, index_col = 'name') # Read in dataframe with attractors from virtual screenings

    # Specify the cluster labels and label of goal cluster based on the number of clusters in the training set
    if ncl == 2:
        labels = [name[:-2] for name in ref.index.tolist()]
        goal = ["MCF10A"]
    elif ncl == 4:
        labels = ["MCF10A_1", "MCF10A_2", "MCF10A_1", "MCF10A_2", "MDAMB231_1", "MDAMB231_2", "MDAMB231_1", "MDAMB231_2"]
        goal = ['MCF10A_1', 'MCF10A_2']

    for i in range(1,ref.shape[0]+1): # Test k-nearest neighbors with k = 1,2,3,... the number of attractors in training set
        knn=neighbors.KNeighborsClassifier(n_neighbors=i, n_jobs = -1, metric= metric) #n_jobs = -1 uses all processors, metric = distance matric
        knn.fit(ref,labels)
        perturb_lab=knn.predict(df_perturb) # predict clusters for attractors from virtual screenings
        A, B  = knn.kneighbors(df_perturb, i)
        A = pd.DataFrame(A, index = df_perturb.index) #Distance between the attractors from virtual screenings and each of the attractors in the training set
        B = pd.DataFrame(B, index = df_perturb.index) #Nearest neighbors of each attractor from virtual screenings in order of distance
        A.to_csv(os.path.join(knn_folder, 'knn' + str(i) + '_distance.txt'), sep = " ", index_label = ["name"])
        B.to_csv(os.path.join(knn_folder, 'knn' + str(i) + '_index.txt'), sep = " ", index_label = ['name'])

        # Create a dataframe of each attractor from virtual screenings and their classification from knn
        df2=pd.DataFrame(index=df_perturb.index) 
        df2['classification']=perturb_lab

        # write out knn results
        df2.to_csv(os.path.join(knn_folder, 'knn'+str(i)+'.txt'),sep=' ',index_label=["name"])
        df3 = df2.loc[df2.classification.isin(goal), :] # Create a dataframe containing only attractors classified in the goal cluster
        df3.to_csv(os.path.join(knn_folder, 'knn'+str(i)+'_goal.txt'),sep=' ',index_label=["name"])

    
main()
