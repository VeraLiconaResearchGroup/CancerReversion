#------------------------------------------
# kmeans_perturbations.py runs kmeans on the attractors from virtual screeenings for a pre-definde k value
#
# Requires user specification of the dataset of reference attractors to use and the path to the file
#
# INPUTS:
# 1. Dataset of reference attractors
#
# OUTPUTS:
# 1. Cluster labels for each reference attractor at each value of k
# 2. Dataframe with sum of squared differences at each k value
# 3. Silhouette plot to determine optimal k
#------------------------------------------

import pandas as pd
from scipy import stats
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
##import seaborn as sns
from sklearn.decomposition import PCA
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics import pairwise_distances
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
import sys
import os

def main():
#####Input files and user specifications###########
    k = int(sys.argv[1]) #Specify the number of clusters
    folder = sys.argv[2] # Path to virtual screening results
    dataset = sys.argv[3]
    
##############################
    # Read in attractors from virtual screenings
    fpath = os.path.join(folder, "perturb_"+dataset+'.txt')
    df1=pd.read_csv(fpath ,delim_whitespace=True, index_col='name')

    # Read in reference attractors
    reffile = "ref_attrs_" + dataset + ".txt"
    ref = pd.read_csv(os.path.join("inputfiles", reffile), delim_whitespace=True, index_col='name')
    
    df = pd.concat([ref, df1], axis = 0)

    #Run Mini batch kmeans with k clusters
    kmeans = MiniBatchKMeans(n_clusters=k,random_state=0,n_init=10000).fit(df)
    labels = kmeans.labels_

    #Create dataframe with each attractor and the cluster the fall into
    df2 = pd.DataFrame(index=df.index)
    df2['clusters'] = labels
    df2.index.name = 'name'
    df2.to_csv(os.path.join(folder, 'kmeans_' + dataset , 'kmeans'+str(k)+'.txt'), sep=' ')

    #Add the sum of squared differences for this k value to a dataframe
    sumdf = pd.DataFrame(index = [k], columns = ['inertia'])
    sumdf.index.name = 'k'
    sumdf.loc[k,'inertia'] = kmeans.inertia_
    with open(os.path.join(folder, 'kmeans_' + dataset, 'inertia.txt'),'a') as f:
        sumdf.to_csv(f, header=f.tell()==0, sep = " ")
        
        
main()

