---
layout: post
title: "Mutation Exploration Part 2"
date: "2019-05-29"
author: lauren, maddie
tags:
 - project01
 - static_network
 - mutations
 - GeneXplain
---
# Order of Attack
- [x] Data Dig pt 3
  - [x] Investigate 19 mutated genes that have protein data
- [x] Run Shortest Paths in GeneXplain
- [x] Run Master Regulator search with context genes as proteins
- [ ] Discuss


# Goal
The Goal of this experiment is to determine if we can find the pathways of mutant TP53 in GeneXplain

## Data Dig pt 3

We investigated the 19 mutations that we had mutational data and protein present for. The only mutated proteins related to TNBC are MKi67, BRAF, and TP53. The other 16 mutated proteins have no effect on TNBC tumorigenesis.  

There is no information surrounding what the MKi67 mutation does. From our ReKINect run, we know that the BRAF mutation causes overactive kinase signaling with MEK. The effects of the TP53 mutation are discussed at length in the investigating mutational pathways post.

## Shortest Paths
We ran shortest paths from tp53 (MO000019548) to the first targets of the 3 pathways directly upregulated by mutp53:  
- VDR (vitamin d receptor pathway)  
- TP63 and SMAD2 (TGF$\beta$ pathway)  
- SREBF1 (Mevalonate Pathway)  

We visualized the results from this and looked to see if there were direct interactions between TP53 and any of the four targets. While in some cases there were indirect paths connected the two, GeneXplain did not provide a direct link from TP53 to any of the targets. This is to be expected as these are noncanonical pathways specific to our R280K TP53 mutation.

## TRANSPATH
We ran TRANSPATH with all proteins as context instead of the usual SOC set. This run produced ~175 MR that covered all 8 TFs. 
