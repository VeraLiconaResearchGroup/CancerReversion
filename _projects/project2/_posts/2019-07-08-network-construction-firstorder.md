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

We will assemble the network built from the set of First Order FunDEGs.

## MRs to TFs    
Just as when we [constructed the network using the Second Order FunDEGs]({{ site.baseurl }}{% link _projects/project2/_posts/2019-06-26-network-construction.md %}), the GeneXplain Visualization of the pathways between MRs with protein data and the TFs was processed with the [`read_SBML.py`](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Network_Construction/MRs%20to%20TFs/read_SBML.py) script. Interactions that did not have a clear activation or inhibition in the xml file were literature searched to determine if the interaction is activating or inhiting.

## TFs to FunDEGs  

I gathered edges from IPA, omnipath, and pearson correlation to assemble a network of 231 nodes (29 source) and 580 edges. After running FVS and getting a smallest set of 15 nodes, I decided this was too unmanageable and decided to **construct the network using master regulators from a smaller step size.**  

## Scaling back  

The smallest step size to cover 8 of the 9 TFs was a step size of 7, so I constructed the network using those MRs. After comparing to protein data, I was left with 4 MRs. There were no mutated nodes in the pathways between the MRs and the TFs, and I removed the single unexpressed node, making MAPK1 a source node. The addition of mutTP53-related pathways also generated a source node of SMAD2, and of course ZBTB17 is a source node because it's not covered by any of the MRs. This left me with a [network](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/OLD/Network%20Construction%202/Network_full.sif) of **116 nodes, 6 of which are source nodes, and 259 edges**. I did not include the pathways affected by mutBRAF, because our mutation overactivates MEK and ERK, and we have neither of those in the network.  

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