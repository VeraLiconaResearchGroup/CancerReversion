#------------------------------------------
# kmeans_reference.py runs kmeans on the attractors estimated from experimental initial conditions with SFA with various values of k
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
from sklearn.decomposition import PCA
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics import pairwise_distances
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
import sys
import os


def main():
    ############### INPUTS:###############
    dataset = sys.argv[1] #Dataset on which to run kmeans (logss, DAC, both, discrete versions, mds)
    ######################################

    dirname = os.path.dirname('reference_attrs/')
    df = pd.read_csv(os.path.join(dirname, 'ref_attrs_' + dataset + '.txt'), delim_whitespace=True, index_col = ["name"]) #read in dataframe of reference attractors
    Sum_of_squared_distances = {} #Initialize sum of squared distancese
    n = df.shape[0]
    out_folder = os.path.join(dirname, 'kmeans_'+dataset) #Folder to write out results to
    
    for k in range(2,n+1): #kmeans with k values from 2 to the number of reference attractors
        kmeans = KMeans(n_clusters=k,random_state=0,n_init=10000).fit(df)
        labels = kmeans.labels_
        Sum_of_squared_distances[str(k)] = kmeans.inertia_
        
        df2 = pd.DataFrame(index=df.index) #Create dataframe with cluster assignments for each reference attractor
        df2['clusters'] = labels                                            
        df2.to_csv(os.path.join(out_folder, 'kmeans'+str(k)+'.txt'), sep=' ') 

    sil = pandas.DataFrame.from_dict(Sum_of_squared_distances, orient = "index") #Create dataframe with sum of squared distances at each k value
    sil.to_csv(os.path.join(out_folder, "silhouette.txt"), sep = " ", index_label = "name") 

    #create silhouette plot for sum of squared distances
    plt.plot(range(2,n), Sum_of_squared_distances.values(), 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    plt.savefig(os.path.join(out_folder,  'silhouette.png')
    
       
main()

