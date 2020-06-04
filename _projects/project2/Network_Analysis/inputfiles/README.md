inputfiles
=========

## Description

This folder contains files needed to run the network analysis.

## Folder Architecture

**exprsesed_nodes_basal_231.txt** Contains the normalized RNAseq expression values for MDA-MB-231 used as initial conditions that FVS perturbations are applied to for virtual screening.

**FVS_12** Is FVS 12 from the OCSANA+ output that virtual screenings were done with.

**FVS_basal.txt** Is the normalized RNAseq expression data for the FVS nodes in each of the experimental replicates

**FVS_output** is all FVSes identifiede by OCSANA+


**medeian_231_attr.txt** is the median of all four MDA-MB-231 reference attractors used to calculate DAC.

**network_nodes_227.txt** is a list of all network nodes

**network_nodes_normalized_expresesion_replicates.txt**  is the normalized RNAseq expression data of all experimental replicates for all network nodes with gene expression data

**network.sif** is the final network in with edges as **source interaction target**, where interaction is either **activates** or **inactivates**.


**source_nodes.txt** are the source nodes of the network.
