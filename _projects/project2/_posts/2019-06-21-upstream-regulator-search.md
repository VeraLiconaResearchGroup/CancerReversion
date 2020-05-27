---
layout: post
title: "Master Regulator Search"
date: "2019-06-21"
author: maddie
tags:
 - project02
 - static_network
 - GeneXplain
 - VEP
 - mutations
 - proteomics
---

# Objective
Identify upstream molecules regulating our TFs.

## GeneXplain Mutated Network Workflow

*Note: Use the edited workflow with step size 10, using signed Transpath, calculating z-scores with a cut-off of 1.5, and without filtering*

This workflow will be used to identify master regulators in pathways that do not involve genes mutated such that protein is not produced. 

The full VCF was parsed to include only nonsense mutations according to the COSMIC database. This is because the mutant pathways workflow removes mutated nodes and we don't want to remove possible gain-of-function mutations. 

This workflow produced 61 MRs that are expressed in our dataset.

We will compare the results from this analysis with the results from a normal master regulator search. The difference between the two will be compared and mutational data will be analyzed where necessary.


## GeneXplain with Context and Weighting

I also ran the above workflow to identify MRs using the union of protein data and SOC genes as context, with average intensity as the weighting column. Those SOC genes with no protein data were weighted as 0. This workflow produced 68 MRs with either protein data or gene expression data covering all 7 TFs. The only mutant node in the pathways generated was TP53, which we have characterized well and know how to deal with it.

**Possibly use a different pathway from first TRANSPATH because TP53 GOF mutation means it loses it's normal function**


![TP53]({{ site.baseurl }}\_assets\images_proj2\tp53.png)

## Comparison of the two results

![venn]({{ site.baseurl }}\_assets\images_proj2\venn_mutMR_contextMR.png)