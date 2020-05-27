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


def main():
#####Input files and user specifications###########
##    kmeans_folder = 'kmeans_new' # output folder for kmeans results specified in batch script
##    k = int(sys.argv[1])
    for k in range(2,16):

    ###############################
    ##    df=pd.read_csv('../boolnet_attractors.txt',delim_whitespace=True, index_col='name') #please specify table to read in
        df = pd.read_csv('mds_boolnet_attr_3.txt', delim_whitespace = True, index_col = ['name'])
        
        kmeans = MiniBatchKMeans(n_clusters=k,random_state=0,n_init=10000).fit(df)
        labels = kmeans.labels_
        
        df['clusters'] = labels
        df2 = pd.DataFrame(index=df.index)
        df2['clusters'] = labels                                            
        df2.to_csv('kmeans_attr/kmeans_attr'+str(k)+'.txt', sep=' ')
        with open('kmeans_attr/inertia_attr.txt','a') as f:
            f.write(str(k)+'\t'+str(kmeans.inertia_)+'\n')
        #origDisp = kmeans.inertia_
        #Sum_of_squared_distances.append(origDisp)
        # gap = np.log(np.mean(refDisps)) - np.log(origDisp)
        # gapdf.loc[k,'gap'] = gap

        #sumdf = gapdf.copy(deep=True)
        #sumdf.columns = ["Sum_of_Squared"]
        #sumdf.loc[k, "Sum_of_Squared"] = origDisp

        #print(k)
        #print("Sum of squares: ", Sum_of_squared_distances)
        # print("gap statistic:", gap)

        # with open(kmeans_folder+"/gapstat.txt", 'a') as f:
        #     gapdf.to_csv(f, header=f.tell()==0, sep = " ")
        
main()

