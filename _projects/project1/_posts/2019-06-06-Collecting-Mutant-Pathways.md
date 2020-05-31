---
layout: post
title: "Curating Mutant Pathways"
date: "2019-06-06"
author: maddie, lauren
tags:
 - project01
 - static_network
 - mutations
---
# Objective
Collecting nodes involved in mutant pathways and determining their interactions. See [Investigating Mutational Pathways]({{ site.baseurl }}{ % link _projects/project1/_posts/2019-05-27-thinking-about-mutations.md % }) and [Investigating Phosphorylation Mutations]({{ site.baseurl }}{ % link _projects/project1/_posts/2019-05-15-ReKINect.md % }) for more details regarding the pathways.

# Interactions

**Mevalonate Pathway**

TP53 activates SREBF2  
SREBF2 activates HMGCR  
HMGCR activates MVK  
MVK activates PMVK  
PMVK activates MVD  
MVD activates FDPS  
FDPS activates RHOA  

**Vitamin D Receptor Mediated Apoptosis**

TP53 activates VDR  
VDR activates WNT  

**TGFB induced metastasis**

TP53 activates TP53:SMAD2  
SMAD2 activates TP53:SMAD2  
TP53:SMAD2 inactivates TP63  
TP63 activates CCNG2  
TP63 inactivates WNT5A  
WNT5A activates RHOA  


# Possible [Readout Nodes](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/PossibleReadoutNodes)

**Cell Migration/Proliferation**  
- WNT5A (leads to increased CXC chemokines)
- WNT
- RHOA


**Cell survival**  
- FDPS (mevalonate pathway products important for cell survival)

**EMT**  
