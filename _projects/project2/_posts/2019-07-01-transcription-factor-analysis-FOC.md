---
layout: post
title: "Transcription Factor Analysis on First Order FunDEG set"
date: "2019-07-01"
author: maddie
tags:
 - project02
 - static_network
---
# Overview
After [constructing the network]({{ site.baseurl }}{% link _projects/project2/_posts/2019-06-26-network-construction.md %}) based on the 316 Second Order FunDEGs, I faced issues in finding edges between TFs and SOC genes. Specifcially, 244 SOC genes were not covered before using pearson correlation and even after going down to 0.5, I was left with 72 uncovered SOC genes and no way to cover them.   

I explored the TFs predicted by IPA that were not included in the intersection between IPA and geneXplain's analyze promoters. I looked at the targets of 36 expressed TFs that passed filtering criteria, and found that if they were all included in the network, less than 80 of the 244 uncovered SOC genes would be covered. Therefore, I decided we needed to take a different approach.  

We will reconstruct the network using the First Order FunDEGs as opposed to the Second Order FunDEGs. As can be seen below, the difference in weighted sums between the two lists is not large but there is a big difference in the number of genes in each list.

![weighted sums]({{ site.baseurl }}\_assets\images_proj2\weightedsums_plusTABLE.png)

By using the First order FunDEGs, we will lose 102 genes from the hallmarks of cancer, 5 claudin-low related genes, and 25 breast disease ontology genes. With the overlap, we will miss a total of 117 CL breast cancer related genes that are included in the Second order FunDEGs but not the First Order FunDEGs.

# Transcription Factor Analysis

I followed the same procedure as [last time]({{ site.baseurl }}{% link _projects/project2/_posts/2019-06-21-transcription-factor-analysis.md %}) using both GeneXplain and IPA. 

After taking the intersection between the expressed TFs in unmethylated regions and the results from IPA all tissues and breast cancer cell lines, I ran weighted sums on the resulting lists.

![weighted sums]({{ site.baseurl }}\_assets\images_proj2\TFs_weightedsums_graph_table_FOC.png)

Surprisingly, 4 of the 5 lists of TFs have the same weighted sum. I decided to move forward with the intersection with the list from promotor window size of [500](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Network_Components/TFs/FirstOrder_FunDEG_analysis/TFs_APIPA_0500.csv) because it includes the most TFs and therefore the most CL TNBC related TFs.

