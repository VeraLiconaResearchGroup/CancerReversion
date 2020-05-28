---
layout: post
title: "Upstream Regulator Analysis on First Order FunDEG TFs"
date: "2019-07-02"
author: maddie
tags:
    - project02
    - static_network
    - VEP
    - mutations
    - proteomics
---

## Objective
Identify upstream moleucles regulating the 9 TFs in the network.

## Analysis
The analysis was done using geneXplain TRANSPATH in two different ways, as described [last time]({{ site.baseurl }}{% post_url 2019-06-21-upstream-regulator-search %}).

## Results
Running the analysis at a step size of 10 and then comparing to the union of gene and protein expression data covered all TFs but resulted in a network that was too large to visualize. However, comparing to just protein data as we did last time was a more manageable size and did visualize. I decided to try smaller step sizes to see how small I could go with still covering all 9 TFs and found that only a step size of 9 or 10 covered all the TFs. However, MRs that covered all the TFs at these steps were included in the results of the MR search with a smaller step size, but not all TFs were included in their hits. We hypothesize that this is because the proteins in these pathways are not highly expressed so using the workflow with weighting avoided them at a smaller step size.  

We decided on the list of 81 MRs with either **gene or protein expression** generated from running TRANSPATH with a step size of 9.

## Filtering by protein data
After looking at the results from filtering MRs for those with either gene or protein data present, we decided we needed a more stringent filter. Therefore, we decided to filter the MRs from step 9 for only those with protein present. This left us with [50](http://platform.genexplain.com/bioumlweb/#de=data/Projects/SalazarCortes%20DataAnalysis/Data/Gastonguay/MDAMB231_TAKE2/Network%20Components/MRs/FOC/MRs_context_weighting_step9_signed/MRs%20expressed%20(prtn%20only)%20Genes%20Ensembl) MRs.

3 nodes in the TRANSPATH pathways were mutated: TP53, BRAF, and LRRK2. Additionally, 6 nodes weren't expressed, one of which was LRRK2. I removed all of the unexpressed nodes except for SP1 because it would have created a source node from one of the TFs: ZBTB17.  

## Mutations

After visualizing with step size of 9, we have four mutations in the network:
 - TP53 (R280K)
 - BRAF (G464V)
 - TAB2 (Q249*)
 - LRRK2 (I2323S, I2330S)

We know the effects of both TP53 and BRAF so they will be added to the network manually see [Mutated Pathways Post]()

**Question:** How do we deal with TP53 loss-of-function?
TP53 (activates) DUSP4  
TP53 (activates) MDM2  
TP53 (activates) NOTCH1  
TP53 (inactivates) AURKA  
TP53 (inactivates) CDC25A  

Removing it would make DUSP4 a source node. (DUSP4 activates MAPK1)

The only one of these mutations that is nonsense is TAB2, which is a master regulator regulating MAP3K7. Removing it will not create a source node.

The LRRK2 mutation was included in the [ReKINect output](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Mutations/VEP_runs/ReKINectOutput.txt) from the last time I constructed the network. However, it doesn't hit a phosphorylation site or domain, and there is no literature regarding the mutatio nn's effect so I cannot determine it's function.

I then moved forward to [network construction]({{ site.baseurl }}{% post_url 2019-07-08-network-construction-firstorder %}) with this new MR to TF network.