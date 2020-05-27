import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
##import seaborn as sns
from sklearn.decomposition import PCA

def main():
    df=pd.read_csv('attractors_discrete.txt', delim_whitespace=True,index_col = ["name"])
    #df_tr = df.drop('name',axis=1)
    df_tr=df
##    pca = PCA(2)
##    pca.fit(df_tr) 
##    pca_data = pd.DataFrame(pca.transform(df_tr))
##    print(pca_data)
##    print(pca.explained_variance_ratio_)


    Sum_of_squared_distances = []
    K = range(1,15)
    for k in K:
        
        km = KMeans(n_clusters=k)
        km = km.fit(df_tr)
        Sum_of_squared_distances.append(km.inertia_)
    plt.plot(K, Sum_of_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    plt.show()
    kmeans = KMeans(n_clusters=3, random_state=0).fit(df_tr)
    labels = kmeans.labels_
    df_tr['clusters'] = labels
    print(df_tr)
main()
