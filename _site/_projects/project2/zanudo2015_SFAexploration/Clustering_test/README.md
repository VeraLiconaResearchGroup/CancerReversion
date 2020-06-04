Clustering_test
==========

## Description
This folder contains results of clustering and MDS applied to the attractors of the Boolean model as a preliminary test.

## Folder Architecture

**boolnet_attractors_noX.txt** contains the 877 attractors of the Boolean model, with oscillating nodes (typically denoted by X) randomly assigned a 0 or 1 because k-means requires numeric entries.

**boolnet_DAC_noX.txt** contains the DAC of the 877 attractors of the Boolean model computed against the Leukemia1 attractor, with oscillating nodes (typically denoted by X) randomly assigned a 0 or 1 because k-means requires numeric entries.

**boolnet_both_noX.txt** contains the concatination of the above two datasets.

**kmeans_\*** contains the results of k-means with k values from 2 to 15 on all three datasets. Folders ending in **\_2d** contain the results of k-means applied to the result of MDS with 2 dimensions on the attractors.

**kmeans.py** script for kmeans.

**mds_boolnet_\*\_2.txt** is the result of MDS with 2 dimensions using sammon mapping on the hamming distance between entries in the speecific dataset of attractors of the boolean model.

**mds_boolnet_\*\_3.txt** is the result of MDS with 3 dimensions using sammon mapping on the hamming distance between entries in the speecific dataset of attractors of the boolean model.

**mds_kmeans_\*_boolnet.pdf** contains graphs of the results of MDS with 2 dimensions on the specified dataset of attractors, colored by the results of k-means clustering at different values of k to determine if k-means is accurately grouping attractors associated to the same phenotype.

**mds.R** is the script used to calculate MDS on each dataset.

**mds2.R** is the script that does further analysis on the results of mds.

**PCA.R** runs principal component analysis on the attractors of the Boolean model.

**viz_mds_kmeans.R** generates **mds_kmeans_\*_boolnet.pdf**.