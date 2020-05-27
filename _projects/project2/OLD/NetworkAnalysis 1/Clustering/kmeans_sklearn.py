import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
##import seaborn as sns
from sklearn.decomposition import PCA

def main():
    df=pd.read_csv('attractors_discrete.txt', delim_whitespace=True)
    df_tr = df.drop('name',axis=1)
    pca = PCA(2)
    pca.fit(df_tr) 
    pca_data = pd.DataFrame(pca.transform(df_tr))
    print(pca_data)
    kmeans = KMeans(n_clusters=6, random_state=0).fit(pca_data)
    labels = kmeans.labels_
    df_tr['clusters'] = labels
    print(df_tr)
main()
