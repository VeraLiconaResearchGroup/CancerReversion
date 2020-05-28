---
layout: post
title: "Exploration of the Uses and Applications of SFA"
date: "2020-01-28"
author: maddie
tags:
 - project02
 - static_network
---

## Objective
The purpose of this exploration was to identify the limitations and appropriate uses of SFA. We compared results of SFA applied to the signaling network of T-LGL Leukemia to the attractors of the Boolean model of T-LGL Leukemia from [Zanudo and Albert](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004193). Data from the exploration can be found [here](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/tree/dev/_projects/project2/zanudo2015_SFAexploration).

## Conclusions
We found that SFA can accurately associate attractors to phenotypes by computing the DAC between attractors from different conditions when simulated with fixed nodes. Thus, we expect it to be able to predict effect of perturbations of the FVS nodes on the long-term behavior of the network with reasonably good accuracy. We also concluded that SFA cannot be used the way we are currently using it to estimate the attractor landscape of the network. Further work will be done by Lauren to determine if there are modifications to its application that can produce more biologically relevant attractors. 

**See more details in the [writeup](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Writing/SFA_exploration.pdf)**
