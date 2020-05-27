import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
##import seaborn as sns
from sklearn.decomposition import PCA
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics import pairwise_distances
from sklearn.cluster import KMeans

def compute_inertia(a, X):
    W = [np.mean(pairwise_distances(X[a == c, :])) for c in np.unique(a)]
    return np.mean(W)

def compute_gap(clustering, data, k_max=5, n_references=5):
    if len(data.shape) == 1:
        data = data.reshape(-1, 1)
    reference = np.random.rand(*data.shape)
    reference_inertia = []
    for k in range(1, k_max+1):
        local_inertia = []
        for _ in range(n_references):
            clustering.n_clusters = k
            assignments = clustering.fit_predict(reference)
            local_inertia.append(compute_inertia(assignments, reference))
        reference_inertia.append(np.mean(local_inertia))
    
    ondata_inertia = []
    for k in range(1, k_max+1):
        clustering.n_clusters = k
        assignments = clustering.fit_predict(data)
        ondata_inertia.append(compute_inertia(assignments, data))
        
    gap = np.log(reference_inertia)-np.log(ondata_inertia)
    return gap, np.log(reference_inertia), np.log(ondata_inertia)



def main():

#### Read in data
    df=pd.read_csv('attractors_discrete.txt', delim_whitespace=True,index_col = ["name"])
    #df_tr = df.drop('name',axis=1)
    


### Plot sum of squares using sklearn command
##    Sum_of_squared_distances = [] #list of sum of squares values
##    K = range(1,5)
##    for k in K:
##        
##        km = KMeans(n_clusters=k)
##        km = km.fit(df)
##        Sum_of_squared_distances.append(km.inertia_)
##    plt.plot(K, Sum_of_squared_distances, 'bx-')
##    plt.xlabel('k')
##    plt.ylabel('Sum_of_squared_distances')
##    plt.title('Elbow Method For Optimal k')
##    plt.show()

### Plot sum of squares and gap statistic using glowing python
    gap, reference_inertia, ondata_inertia = compute_gap(KMeans(), df)

    #inertia
    plt.plot(range(1, k_max+1), reference_inertia,'-o', label='reference') 
    plt.plot(range(1, k_max+1), ondata_inertia,'-o', label='data')
    plt.xlabel('k')
    plt.ylabel('log(inertia)')
    plt.show()

    #gapstat
    plt.plot(range(1, k_max+1), gap, '-o')
    plt.ylabel('gap')
    plt.xlabel('k')

#### plot kmeans
####    kmeans = KMeans(n_clusters=4, random_state=0).fit(df_tr)
####    labels = kmeans.labels_
####    df_tr['clusters'] = labels
####    print(df_tr)
main()

