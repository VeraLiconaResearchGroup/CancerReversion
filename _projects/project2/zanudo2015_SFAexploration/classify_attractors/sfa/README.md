sfa
======

## Description

This folder contains the results of classification by k-means of attractors simulated by SFA from 100,000 initial states. Attractors resulting from initial states in the basin of the Apoptosis (Leukemia) associated attractors of the Boolean model when classified by RONs are considered Apoptosis (Leukemia) associated attractors. 

## Folder Architecture

**apoptosis_basin.txt** contains intial states in the basin of Zanduo's apoptosis Boolean attractor.

**apoptosis_sfa_kmeans\*_<k>.txt** is a list of attractors in an apoptosis associated clustere when kmeans is applied to the specified dataset with the specified k value.

**classify_attractors_DAC_sfa.py** classifies SFA attractor based on the DAC of their readoutnodes.

**classify_attractors_newRONs** contains the results of **classify_attractors_DAC_sfa.py**: a list of apoptosis and leukemia associated attractors.

**cluster_report.py**  interprets the results from k-means to get an idea of the value of readout nodes of attractors that cluster together. It generates the files in the **cluster_reports** folder.

**cluster_reports** contains files with a breakdown of the clusters in which apoptosis and leukemia associated attractors (classified by their RONs) clustered in.  It also provides the percent of Leukemia or Apoptosis attractors that clustered in each cluster (Percent_of_attrs) as well as the percent of the cluster that is apoptosis  or leukemia associated attractors (Percent_of_cluster). Lastly, it lists any clusters that had apoptosis attractors but no leukemia attractors and any clusters with leukemia attractors but no apoptosis attractors to highlight if clusters that are uuniquely leukemia or apoptosis associated exist.

**hamming_DAC_A_\*.txt** is the hamming distance between the DAC of the original 19 RONs between the Leukemia and Apoptosis attractors of the Boolean model and the DAC of the original 19 RONs between attractors simulated by SFA from initial states in the basin of the Apotposis1 attractor and the Leukemia1 or Leukemia2 attractors.

**hamming_distance.py** is used to calculate the hamming distance.

**hamming_plots.R** is used to make boxplots of the distribution of hamming distances between the DAC of RONs of Boolean attractors and the DAC of RONs of SFA attractors.

**is_to_A_L_inBN.txt** is a file denoting which basin of attraction each of the 100,000 random initial states falls into in the Booelan model.

**kmeans_\*** contains results of kmeans with k values from 2-15 applied to either the logss values, the DAC against the Leukemia1 SFA attractor, the concatination of these two, or the DAC against the Apoptosis1 SFA attractor.

**leukemia_sfa_kmeans\*_<k>.txt** is a list of attractors in a leukemia associated cluster when kmeans is applied to the specified dataset with the specified k value.

**leukemia1_basin.txt** is a dataframe of attractors estimated by SFA from initial states in the basin of the Leukemia1 boolean attractor.

**leukemia2_basin.txt** is a dataframe of attractors estimated by SFA from initial states in the basin of the Leukemia2 boolean attractor.

**new_RONs_DACandHam2** contains the distribution of hamming distances with the new RONs.

**sfa_cluster_report.xlsx** shows the breakdown of apoptosis and leukemia associated attractors by cluster for kmeans results with the optimal k on each dataset.

**sfa_DAC_disc_vsAPOP.txt** is the discretized dataset of the DAC each SFA attractor when computed agaisnt the Apoptosis attractor.

**sfa_DAC_disc.txt** is the discretized dataset of the DAC each SFA attractor when computed agaisnt the Leukemia1 attractor.

**sfa_logss.txt.zip** is the log steady state values of the SFA attractors.