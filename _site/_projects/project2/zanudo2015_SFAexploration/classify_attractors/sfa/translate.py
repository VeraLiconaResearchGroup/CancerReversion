import pandas as pd

data = 'ss'
folder = "kmeans_ss"
k = 8

ref = pd.read_csv('is_to_A_L_inBN.txt', delim_whitespace = True, index_col = ['Initial_state'])
kmeans = pd.read_csv(folder + '/kmeans_' + data + '_' + str(k) + '.txt', delim_whitespace = True, index_col = ['name'])

cl_count = pd.DataFrame(kmeans.clusters.value_counts())
cl_count.index.name = 'cluster'
cl_count.columns = ['cluster_size']

ds = ['Apoptosis', 'Leukemia1', 'Leukemia2']
leuk = ["is_017422" ,"is_046854" ,"is_047021", "is_050934" ,"is_072068" ,"is_072078", "is_077678", "is_085952", "is_095194"]
apop = pd.read_csv('307_good_apop_DAC.txt', delim_whitespace = True, index_col = ['x'])

ls = [apop.index.tolist(),leuk, leuk]
with open('cluster_report_kmeans_' + data + '_' + str(k) + '_TEST2.txt', 'w') as f:
    for n in range(len(ds)):
        d = ds[n]
        l = ls[n]
##        ref2 = ref[ref.label == d ]
        ref2 = ref.loc[l,:]
        kmeans_sub = kmeans.loc[ref2.index,]
        f.write(d + ' Clusters: ')
        f.write('\n')
        f.write(str(set(kmeans_sub.clusters)))
        f.write('\n'*2)
        df = pd.DataFrame(kmeans_sub.clusters.value_counts())
        df.index.name = 'Cluster'
        df.columns = ['Number_of_attrs']
        df['Percent_of_attrs'] = round(df.Number_of_attrs/sum(df.Number_of_attrs)*100, 2)
        df['Percent_of_cluster'] = round(df.Number_of_attrs/cl_count.cluster_size*100, 2)
        df.to_csv(f, sep = ' ')
        f.write('\n'*2)



