---
layout: post
title: "Identifying Functionally Related Proteins"
date: "2019-05-06"
author: lauren, maddie
tags:
 - project01
 - static_network
---
# Objective
While the application of BiNOM on the HPRD is valuable when using DEG data, it may be even more useful and representative of what's occurring in the cell using the [ranked proteomics data](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project1/231_protein_ranked_7744).

## Comparison of RNA-Seq and Protein Data
<div style="text-align:center" markdown="1">
![alt text]({{ site.baseurl }}\_assets\images\Venn_protein_allgenes.png)  
</div>

Discrepancies between the genes vs proteins is explained biologically: proteins are more stable than RNA, so the RNA could have been destructed, but the protein remains. 

  - How do we handle discrepancies between RNASeq and protein data? Should we be looking at chromatin data (as long as it's in an open region, the protein should be present)?

## Comparison of Open Chromatin Regions and Protein Data
<div style="text-align:center" markdown="1">
![alt text]({{ site.baseurl }}\_assets\images\Venn_proteins_vs_openchromatinregions.png)
</div>

  - How do we handle discrepencies between chromatin data and protein data? Why would a protein be present if its gene isn't in an open chromatin region?

# Construction of a Proteomic Network

## First Order Connectivity
We wanted to compare the difference between using the proteomic data and the gene expression data to construct the static network. The first step of this is to find functionally related proteins, which we did using the same method as for finding functionally related genes. Protein abundance data was ranked from highest intensity to lowest and the IDs were converted to Ensembl gene IDs. Then we mapped them into HPRD using the BiNOM extension of Cytoscape to determine first order connectivity.

<div style="text-align:center" markdown="1">
![alt text]({{ site.baseurl }}\_assets\images\FOC_analysis_protein.png)
</div>

 We determined the first order connectivity largest connected component (FOC LCC) generated from both the first 100 and 300 ranked proteins, corresponding to the first two peaks of the above graph. After removing housekeeping genes and then taking the resulting largest connected component, we have FOC LCCs of [32](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project1/protein_FOC_100_noHKG_LCC_32) and [161](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project1/protein_FOC_300_noHKG_LCC_161) proteins, respectively.

## Second Order Connectivity
We ran second order connectivity on both the 32 and 161 protein FOC LCCs. After comparing to the expressed proteins and removing housekeeping genes, we were left with SOC lists of [97](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project1/protein_SOC_expressed_noHKG_97) and [466](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project1/protein_SOC_expressed_noHKG_466) proteins from the FOC lists of 32 and 161, respectively. The removal of non-expressed proteins and HKG did not disrupt the largest connected component of the SOC proteins.

## Weighted Sums
We ran [weighted sums](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project1/weighted_sums_proteins.Rmd) by slightly altering the script from the gene lists to be specific to the protein lists.
We compared the protein lists to the same three lists as in the [identification of functionally related genes]({{ site.baseurl }}{% post_url 2019-04-08-functionally-related-genes %}):

1. [Breast Cancer Disease Ontology](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project1/breast_DO.txt) genes associated to breast cancer DO term from [DOLite](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2687947/) in [GeneAnswers](http://www.bioconductor.org/packages/2.5/bioc/html/GeneAnswers.html) R package
2. The complete [hallmark of cancer list](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project1/HOC.txt) from the [atlas of cancer signalling network](https://acsn.curie.fr/ACSN2/ACSN2.html)
3. Only the genes from list 2 associated with [EMT and innate immune reseponse](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project1/EMT_innateimmune) as these hallmarks are claudin-low specific


### For the lists generated from the first 100 ranked proteins, we have:
![weighted sums for 100]({{ site.baseurl }}\_assets\images\weightedsums_prtn_100_plusTABLE.png)
### For the lists generated from the first 300 ranked proteins, we have:
![weighted sums for 300]({{ site.baseurl }}\_assets\images\weightedsums_prtn_300_plusTABLE.png)

From the images above, it is easy to see that the FOC list of 97 proteins generated from the first 100 ranked proteins has the best weighted sums.

# Comparison to Gene Expression Network
When comparing weighted sums, the SOC list of 75 genes generated from the gene expression data has a higher sum (0.3378) than does the best list from the protein data (0.3333).
![weighted sums for genes]({{ site.baseurl }}\_assets\images\weightedsums_plusTABLE.png)

Next, I compared the actual genes/proteins in each of these lists and found that they had nothing in common.

<div style="text-align:center" markdown="1">
![venn]({{ site.baseurl }}\_assets\images\protein_vs_gene_lists.png)
</div>
