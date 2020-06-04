boolnet
=======

## Description

This folder contains results from the classification of attractors of the Boolean model simulated via the Boolnet R package. These attractors were first classified by the value of their RONs, and then clustered via unsupervised k-means clustering. The ability of k-means to separate apoptosis and leukemia associated attractors was gauged based on the RONs of attractors in each cluster.

## Folder Architecture

**apoptosis_attractors_boolnet.txt** is a dataframe of apoptosis associated attractors of the Boolean model classified by the value of their RONs.

**apoptosis_boolnet.txt** is a list of apoptosis associated attractors of the Boolean model classified by the value of their RONs.

**leukemia_attractors_boolnet.txt** is a dataframe of leukemia associated attractors of the Boolean model classified by the value of their RONs.

**leukemia_attractors_boolnet.txt** is a list of leukemia associated attractors of the Boolean model classified by the value of their RONs.

**other_attractors_boolnet.txt** is a dataframe of attractors of the Boolean model that are neither leukemia nor apoptosis associated when classified by the value of their RONs.

**other_attractors_boolnet.txt** is a list of attractors of the Boolean model that are neither leukemia nor apoptosis associated when classified by the value of their RONs.

**cluster_report.py** interprets the results from k-means to get an idea of the value of readout nodes of attractors that cluster together. It generates the files in the **cluster_reports** folder.

**kmeans_\*** contains the results of k-means on either the attractor value (\_ss), DAC against the Leukemia1 attractor (\_DAC), or concatination of these datasets (\_both) for the 877 attractors of the boolean model at k values ranging from 2 to 15. It also includes the silouhette plot to determine the optimal k.

**cluster_reports** contains files with a breakdown of the clusters in which apoptosis and leukemia associated attractors (classified by their RONs) clustered in.  It also provides the percent of Leukemia or Apoptosis attractors that clustered in each cluster (Percent_of_attrs) as well as the percent of the cluster that is apoptosis  or leukemia associated attractors (Percent_of_cluster). Lastly, it lists any clusters that had apoptosis attractors but no leukemia attractors and any clusters with leukemia attractors but no apoptosis attractors to highlight if clusters that are uuniquely leukemia or apoptosis associated exist.