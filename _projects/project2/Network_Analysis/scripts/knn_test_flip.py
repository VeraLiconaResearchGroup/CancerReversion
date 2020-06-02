# -----------------------------------------------------------
# knn_test_flip.py Runs k-nearest neighbors using reference attractors with bassal values for GSK2B and CTNNB1 swapped between normal and cancerous samples as training set
# to classify the results of virtual screenings
# 
# Requires user specification of the dataset to use, the number of clusters in training set, their labels, and the label of the goal cluster(s)
#
# INPUTS:
# 1. Reference Attractors simulated from altered basal states (in test_flip folder)
# 2. Dataframe of attractors from virtual screenings
#
# OUTPUTS: (in pert_folder/test_flip)
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


def main():
    ############ inputs#################
    dataset = sys.argv[1]
    pert_folder = sys.argv[2]
    metric = sys.argv[3]
    ncl = int(sys.argv[4])
    ##################################
    if metric == 'euclidean':
        knn_folder = 'knn_'+dataset
    elif metric == 'hamming':
        knn_folder = 'knn_'+dataset+ "_" + metric
    reffile = 'ref_attrs_' + dataset + '.txt'
    ref = pd.read_csv(os.path.join("test_flip", reffile), delim_whitespace=True, index_col = 'name')

    # Read in same perturbations classified with original training set
    df_perturb = pd.read_csv(os.path.join(pert_folder, 'perturb_' + dataset + '.txt'), delim_whitespace = True, index_col = 'name')    

    # Specify the cluster labels and label of goal cluster based on the number of clusters in the training set
    if ncl == 2:
        labels = [name[:-2] for name in ref.index.tolist()]
        goal = ["MCF10A"]
    elif ncl == 4:
        labels = ["MCF10A_1", "MCF10A_2", "MCF10A_1", "MCF10A_2", "MDAMB231_1", "MDAMB231_2", "MDAMB231_1", "MDAMB231_2"]
        goal = ['MCF10A_1', 'MCF10A_2']

    for i in range(1,ref.shape[0]+1): # Test k-nearest neighbors with k = 1,2,3,... the number of attractors in training set
        knn=neighbors.KNeighborsClassifier(n_neighbors=i, n_jobs = -1, metric= metric)
        knn.fit(ref,labels)  #do knn with attractor landscape
        print(knn.effective_metric_)
        perturb_lab=knn.predict(df_perturb) # predict clusters for perturbations
##        print(i, ':', perturb_lab)
        A, B  = knn.kneighbors(df_perturb, i)
        A = pd.DataFrame(A, index = df_perturb.index)
        B = pd.DataFrame(B, index = df_perturb.index)
        A.to_csv(os.path.join(pert_folder,"test_flip", knn_folder, 'knn' + str(i) + '_distance.txt'), sep = " ", index_label = ["name"])
        B.to_csv(os.path.join(pert_folder,"test_flip", knn_folder,'knn' + str(i) + '_index.txt'), sep = " ", index_label = ['name'])

        
        df2=pd.DataFrame(index=df_perturb.index) 
        df2['classification']=perturb_lab

        # write out knn results
        df2.to_csv(os.path.join(pert_folder, "test_flip", knn_folder,'knn'+str(i)+'.txt'),sep=' ',index_label=["name"])
        df3 = df2.loc[df2.classification.isin(goal), :]
        df3.to_csv(os.path.join(pert_folder,"test_flip",knn_folder, 'knn'+str(i)+'_goal.txt'),sep=' ',index_label=["name"])

    
main()
