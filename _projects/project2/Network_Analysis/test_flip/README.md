test_flip
======

## Description

The results from classification of attractors from virtual screenings indicate the knock-in of GSK3B and CTNNB1 as
putative reversion interventions. This is contrary to prior evidence that GSK3B inhibition decreases EMT and Stemness and 
CTNNB1 inhibition has reversed EMT [[1](https://www.spandidos-publications.com/10.3892/or.2016.5311), [2](https://breast-cancer-research.biomedcentral.com/articles/10.1186/s13058-019-1125-0)].
We noticed that the gene expression of CTNNN1 and GSK3B are higher in the normal-like cell line replicates than in the cancerous
cell-lines, so we simulated the attractors from initial states with expression values for GSK3B and CTNNB1 swapped between cancerous and noraml-like initial conditions.
Then, we used the new reference attractors as a training set for classification of virtual screenings and found that successful perturabtions
did not require the activation of CTNNB1 and GSK3B.

1. Lin et al., Oncology Reports, 2016
2. Vijay et al., Breast Cancer Research, 2019
