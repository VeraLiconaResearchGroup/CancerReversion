import pandas as pd
import numpy as np

data = 'DAC'
folder = "kmeans_DAC"

for k in range(2,16):
    kmeans = pd.read_csv(folder + '/kmeans_'+ data + '_' + str(k) + '.txt', delim_whitespace = True, index_col = ['name'])

    cl_count = pd.DataFrame(kmeans.clusters.value_counts())
    cl_count.index.name = 'cluster'
    cl_count.columns = ['cluster_size']

    leuk = open('classify_attractors_newRONs/leukemia_sfaDAC.txt').read().split('\n')
    apop = open('classify_attractors_newRONs/apoptosis_sfaDAC.txt').read().split('\n')
    ls = [apop,leuk]
    ds = ['apoptosis', 'leukemia']
    clusts = {}

    with open('classify_attractors_newRONs/cluster_reports/cluster_report_kmeans_' + data + '_' + str(k) +'.txt', 'w') as f:
        for n in range(len(ds)):
            d = ds[n]
            l = ls[n]
    ##        ref2 = ref[ref.label == d ]
    ##        ref2 = ref.loc[l,:]
            kmeans_sub = kmeans.loc[l,]
            f.write(d + ' Clusters: ')
            f.write('\n')
            clusts[d] = list(set(kmeans_sub.clusters))
            f.write(str(set(kmeans_sub.clusters)))
            f.write('\n'*2)
            df = pd.DataFrame(kmeans_sub.clusters.value_counts())
            df.index.name = 'Cluster'
            df.columns = ['Number_of_attrs']
            df['Percent_of_attrs'] = round(df.Number_of_attrs/sum(df.Number_of_attrs)*100, 2)
            df['Percent_of_cluster'] = round(df.Number_of_attrs/cl_count.cluster_size*100, 2)
            df.to_csv(f, sep = ' ')
            f.write('\n'*2)

        au = np.setdiff1d(clusts['apoptosis'], clusts['leukemia'],assume_unique = True).tolist()
        lu = np.setdiff1d(clusts['leukemia'],clusts['apoptosis'],assume_unique = True).tolist()
        f.write('Unique Apop Clusters:\n')
        f.write(str(au))
        f.write('\n')
        f.write('Unique Leuk Clusters:\n')
        f.write(str(lu))
    if len(au) >= 1 & len(lu) >=1:
        print(k)


