---
layout: post
title: "Network Analysis 1"
date: "2019-07-11"
author: maddie
tags:
 - project2
 - static_network
---

# Objectives
The objective of Network Analysis is to identify and prioritize putative reversion targets. This is done using Feedback Vertex Set (FVS) Control, a sturcture-based attractor-based control method for non-linear systems. Then, a topological estimation of signal flow is done with Signal Flow Analysis (SFA) to estimate attractors of the network. The details below are from preliminary analyses.

# FVS

I [ran FVS](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/OLD/NetworkAnalysis%201/FVS_step7/FVS_run.py) on both the network constructed with MRs from a step size of 9 and on the network constructed with MRs from a step size of 7. The first network produced [several FVS sets](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/OLD/NetworkAnalysis%201/FVS_step9/231_FVS_output2.txt), ranging in size from 15 to 17 nodes, while the second produced [two FVS sets of 3 nodes each](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/OLD/NetworkAnalysis%201/FVS_step7/231_FVS_output2.txt). They are:

['EGFR', 'RELA', 'FOXM1']  

['PLK1', 'RELA', 'EGFR']


**Notes:** 
 - Inhibition of [PLK1](https://www.ncbi.nlm.nih.gov/pubmed/30996295) leads to increased apoptosis
 - Targeting [EGFR](https://www.ncbi.nlm.nih.gov/pubmed/30660004) increases apoptosis in MDA-MB-231
 - [FOXM1](https://www.ncbi.nlm.nih.gov/pubmed/30365046) is a critical regulatory gene in TNBC; its suppression can lead to decreased proliferation in MDA-MB-231
 - Inactivating [RELA](http://mct.aacrjournals.org/content/molcanther/12/7/1356.full.pdf) may reverse EMT

Considering the smaller size of the FVS set and the smaller number of source nodes (6 compared to 29), I will use the smaller network of 117 nodes moving forward.

# SFA

I ran [signal flow analysis](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/OLD/NetworkAnalysis%201/SFA/sfastart_attractors.py) to determine the attractors of the [MCF10A](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/OLD/NetworkAnalysis%201/SFA/attractor_10A.txt) and the [MDAMB231](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/OLD/NetworkAnalysis%201/SFA/attractor_231.txt) cell lines. Then I identified candidate readout nodes as those nodes whose expression flipped between the two attractors.  

In order to approximate the attractor landscape of the network, I wrote a script, [`randomStateGenerator.py`](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/OLD/NetworkAnalysis%201/SFA/Identify%20Attractors/randomStateGenerator.py), to produce k *unique* random sets of n zeroes and ones to use as initial states. In this case, **n = 114** (114 nodes with gene expression data), and I started with **k = 1000**.  

I then wrote [`SimulateAttractors.py`](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/OLD/NetworkAnalysis%201/SFA/Identify%20Attractors/SimulateAttractors.py) to take these 1000 basal level inputs and generate the corresponding attractors.

# Clustering  

In order to classify attractor states, I investigated the feasability of clustering the attractors. I first did this with a PCA plot, which did not prove helpful.

![PCA]({{ site.baseurl }}\_assets\images_proj2\pca_attractors.png)  

I next tried a heatmap of the 1000 attractors but that wasn't helpful either.

![heatmap]({{ site.baseurl }}\_assets\images_proj2\heatmap_attractors.png)


After reading the [2017 Quaranta paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5532541/), I found that they used the R package [*ConsensusClusterPlus*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2881355/) to cluster their attractors. This is an unsupervised clustering approach that tests different numbers of clusters (from 2 to 20 in this case) and can use different algorithms.

I ran this with 1000 reps, taking subsets of 80% of the nodes (features) and 80% of the attractors (items) and tested out on four different algorithms: hierarchical clustering, partitioning around medoids, k-means, and k-means upon distance matrices. I also tested different distance functions including pearson and spearman to determine if we could cluster our attractors. 


