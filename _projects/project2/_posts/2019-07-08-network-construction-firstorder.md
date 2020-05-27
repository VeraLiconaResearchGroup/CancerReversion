---
layout: post
title: "Network Construction for First Order FunDEGs"
date: "2019-07-08"
author: maddie
tags:
 - project02
 - static_network
---

# Objective

Assemble the network in Cytoscape!

## MRs to TFs    
See [Upstream Rgulator Search]({{ site.baseurl }}{% post_url 2019-07-02-upstream-regulator-search-FOC %}) for more details about the pathways between the MRs and TFs. After running these workflows at different step sizes, the smallest size that produced MRs covering all 9 TFs was a step size of 9. These MRs were filtered for a **p-value < 0.05**, **Z-score > 1.5**, and by protein data, leaving us with [50](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project2/Network_Components/MRs/MRs%20expressed%20(prtn%20only)%20Genes%20Ensembl.txt) MRs.

## TFs to FunDEGs  

I gathered edges from IPA, omnipath, and pearson correlation to assemble a network of 231 nodes (29 source) and 580 edges. After running FVS and getting a smallest set of 15 nodes, I decided this was too unmanageable and decided to construct the network using master regulators from a smaller step size.  

## Scaling back  

The smallest step size to cover 8 of the 9 TFs was a step size of 7, so I reconstructed the network using those MRs. After comparing to protein data, I was left with 4 MRs. There were no mutated nodes in the pathways between the MRs and the TFs, and I removed the single unexpressed node, making MAPK1 a source node. The addition of mutTP53-related pathways also generated a source node of SMAD2, and of course ZBTB17 is a source node because it's not covered by any of the MRs. This left me with a network of **116 nodes, 6 of which are source nodes, and 255 edges**. I did not include the pathways affected by mutBRAF, because our mutation overactivates MEK and ERK, and we have neither of those in the network.  

### TFs to FunDEGs
**IPA:** 47  
**Omnipath (confidence a and b):** 10  
**Pearson .99:** 76  
**Pearson .95:** 49  
**Pearson .90:** 16  
**Pearson .85:** 1  
**Pearson .80:** 1  

After collecting these edges, there were 3 FunDEGs I couldn't glue but their removal would not disrupt the FunDEG largest connected component, and there is no literature linking them to TNBC, so I excluded them from the network.

The network consists of 15 Breast Disease Ontology related genes, 4 Claudin-low related genes, and 43 genes related to EMT or innate immune response.