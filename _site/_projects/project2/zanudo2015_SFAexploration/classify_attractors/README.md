classify_attractors
=======

## Description

This folder contains results of classification of attractors simulated from 100,000 randomly generated initial states both by SFA and Boolnet. Classification is done based on the DAC of readout nodes and unsupervised k-means clustering. The results were then compared.

## Folder Architecture

**boolnet** contains the results from the Boolean model.

**sfa** contains the results from attractors simulated with SFA.

**classification_comparisons.\*** compares the overlap of classifications of the attractors resulting from each of the 100,000 between SFA and Boolean predictions as well as classification method.

**compare_classifications.R** is the R script to generate **classification_comparisons.txt**.

**is_to_attr_2.txt** Denotes which basin of attraction each of the 100,000 initial states falls into.


