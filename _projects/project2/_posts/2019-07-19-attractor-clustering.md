---
layout: post
title: "Clustering Attractors"
author: maddie
date: "2019-07-19"
tags:
 - project2
 - static_network
---

# Objective
Identify those attractors with cancerous-like and normal-like phenotypes through clustering methods.

## Generation of Data

I generated 1,000 random initial states and ran signal flow to get the 1,000 corresponding attractors. From this I constructed 6 datasets:

<ol type="A">
<li>The raw values produced by signal flow rounded to three decimal places</li>
<li>The values produced by signal flow "discretized" so that positive values are 1, negative values are -1, and 0 values remain 0</li>
<li>The direction of activity change for each attractor calculated by the difference between the raw signal flow data for MDA-MB-231 and each attractor</li>
<li>The "discretized" values of the above dataset</li>
<li>The combination of datasets 1 and 3</li>
<li>The combination of datasets 2 and 4</li>
</ol>

## Clustering Analysis

For each of the datasets listed above, I ran several different clustering methods on them.

1. Principle Component Analysis
2. Multi-dimensional Scaling
3. Hierarchical
    - dendrogram and heatmap
4. K-means
    - After a silhouette and elbow plot

### Notes
Goodness of fit for MDS was so bad (<5% for each of first two components) that I didn't bother looking at what the first two components were. The issue I was having with KNN is that I can an only do KNN with 2 nearest neighbors using this data because we only have two values in the training set.

![knn]({{ site.baseurl }}\_assets\images_proj2\knn.png)

# Identifying attractors that cluster together
Even though I did different clustering methods on different datasets, I only looked at those with "descritized" values because the magnitude doesn't matter! Of these, I decided to use the dataset with the combo of DAC and raw because the hierarchical and kmeans clustering looked good. I identifed approximately 240 attractors that always cluster with MDA-MB-231 and approximately 445 attractors that always cluster with MCF10A whether you use hierarchical or kmeans with 2 or 3 clusters. This leaves about 320 other attractors, representing neither a cancerous or normal phenotype.

## Readout nodes in those clusters  
**FYN, HUWE1, MAPK13** were 1 in 99% of the cancerous attractors whereas in the normal attrctors, there was about a 50/50 split between 1s and -1s for these readout nodes. CDC20 was a 1 in 75% of the normal attractors but it was also a 1 in 62% of cancerous attractors - are these frequencies different enough to distinguish the attractors? Two of the other readout nodes: STAT3 and SNAI1 were a 1 in 100% (STAT3) and 96% (SNAI1) of both the cancerous attractors and normal attractors. (aka they had the same frequency in the normal and cancerous attractors)  Lastly, CCNG2 and GSK3B were split pretty evenly between 1s and -1s in both the cancerous and normal attractors meaning they aren't good readout nodes.

## New Readout Nodes?

**Genes that are expressed in at least 70% of the "cancerous" attractors and less than 70% of the time in "normal" attractors:**
- FBLN1
- FYN
- HUWE1
- LRP1
- LTBP3
- MAPT
- MOCOS
- PIAS3
- TAF12
- TBL1X
- SKIL
- MAPK13
- CXXC5
- RASGRF1
- BIRC6
- DNAJB2
- SHC1
- SH3YL1
- CHEK2
- CTNNB1
- ITGB8
- RHOD

**Genes that are expressed in at least 70% of the "normal" attractors and less than 70% of the time in "cancerous" attractors:**
- AURKA
- HMGB2
- BUB1
- KAT2A
- LIMK2
- ROCK1
- SRPK1
- TAF1B
- TPR
- CKAP5
- S100A2
- HMGA2
- SNRPA
- FGF13
- FOXM1
- TACC1
- JUN
- MAD2L2
- RPS6KA1
- TCF3
- CDC20

# Knn Take 2
I decided to try Knn with the clusters that always cluster with 231 or with 10A as the training set for cancerous and normal, and some of the results from our perturbation analysis as the test case. If we do this, we can compare to more than 2 neighbors, and effectively classify the perturbations as either cancerous or normal.


# Going to do this with 100,000 attractors

TO DO:

1. Determine which dataset is the best to cluster with
2. Pull out cluster assignments for that dataset and the different clustering methods
3. Determine the attractors that always cluster with 231 or 10A
	- via cluster_patterns.py script
	- input: dataframe from 2 with attractors as rows and clustering methods as columns
4. Next, determine if the nodes in these clusters have similar expression patterns
	- via ExploreNodesinClusters.py script
	- input: dataframe of atttractors with attrs as rows and nodes as columns
5. Determine possible readout nodes that are uniform in one cluster but not the other
	- via the NewPossibleRONs.py script
	

## Problem: Size issue with Hclust function  
```
Error in hclust(dist(scale(all_T)), method = "complete") : 
  size cannot be NA nor exceed 65536
Execution halted
```

From what I've read, hierarchical clustering does not scale well to large data sets because it approaces O(n^2) in runtime and O(n^3) in memory complexity. Also, since I am clustering 100,000 attractors, I am creating a 100,000 x 100,000 distance matrix, which is too large for R.
