Network_Analysis
=========

## Description

This folder contains all scripts and files necessary to identify and prioritize putative reversion targets. Run the shell scripts in the following order to run the complete pipeline. User inputs are defined at the start of each shell script, editing their values is sufficient to run the script as desired.

** Shell Script**|**Purpose**
:-----:|:-----:
s1\_estimate\_ref\_attrs.sh|Estimate attractors from normalized expression data of experimental replicates using SFA to be used as references of the cancerous and normal phenotype.
s2\_mds\_ref\_attrs.sh|Run non-metric MDS with sammon mapping on reference attractors and plot the results in 2 dimensions.
s3\_kmeans\_ref\_attrs.sh|Run k-means on the reference attractor to identify the number of clusters for training set in knn. Can also run kmeans on the reduced dimensions from MDS.
s4\_generate\_basal\_perts.sh|Generate random perturbations of the FVS nodes and calculate what the activity level of a knock-in perturbation should be set to for each FVS node.
s5\_virtual\_screening.sh|Run virtual screenings of perturbations of FVS nodes applied to each of the experimental replicates as an initial condition.
s6\_knn.sh|Classify attractors simulated by virtual screenings using knn with the reference attractors as the training set.
s7a\_compare\_datasets.sh|Compare knn classifications of each dataset (Logss, DAC, Both, and discrete versions) of attractors from virtual screenings.
s7b\_compare\_num\_neighbors.sh|Compare classifications of virtual screening attractors by knn with different numbers of neighbors.
s7c\_compare\_replicates.sh|Compare knn classifications of virtual screening attractors from different initial states.
s8\_get\_fvs\_direction.sh| Find the frequency of the perturbation orientation of each FVS node in a subset of successful perturbations.

There are also shell scripts for some exploratory analyses, which are not necessary for the main pipeline:

** Shell Script**|**Purpose**
:-----:|:-----:
mds\_perturbations.sh|Run MDS on the attractors from virtual screenings.
kmeans\_perturbations.sh|Run k-means clustering on the attractors from virtual screenings.
knn\_test\_flip.sh|Cassify attractors from virtual screenings by knn with the reference attractors simulated from initial states with the expression values of CTNNB1 and GSK3B switched between the cancerous and normal cell lines.

## Folder Architecture

**attrs_from_disc** Contains attractors estimated from discrete inital conditions. This is from preliminary analysis and was not included in the final analysis.

**reference_attrs** Contains datasets of reference attractors and results of mds and k-means clustering on datasets of reference attractors at various values of k.

**Attractor_sd.txt** Contains the standard deviation between expression values of each network node amoung MDA-MB-231 experimental replicates and MCF10A expeerimental replicates.

**FVS_attractor_state.txt** Contains the activity level of FVS nodes at the attractor state.

**FVS_fc_pval.txt** Contains the log2 fold change and p-value from DESeq2 analysis for the FVS nodes.

**images** contains images output from the analysis.

**inputfiles** contains necessary input files to run the analysis.

**scripts** contains scripts needed to run the analysis

**test_flip** contains the basal states and resultant attractors for the test run with basal expression values for CTNNB1 and GSK3B flipped between cancerous and normal initial conditions.

**test_RNAseq2** consists of results from differential expression applied to RNAseq count data from a second source.

**virtual screening** Contains results from virtual screenings and knn classifications of FVS node perturbations.