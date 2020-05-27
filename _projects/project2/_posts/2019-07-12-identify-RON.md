---
layout: post
title: "Identifying Readout Nodes"
date: "2019-07-12"
author: maddie
tags:
    - project2
    - static_network
---

# Objective
Identify nodes in the network that are markers of TNBC tumorigenesis such as EMT, proliferation, and migration that can be used to determine the phenotype associated with an attractor.

## Characteristic Phenotypes:
>A number of groups have further characterized this new tumor subtype and shown that CL tumors account for 7–14% of all invasive breast cancers, are enriched for genes associated with **epithelial to mesenchymal transition (EMT)**, **immune cell infiltration**, **IFNγ activation**, **mammary stem cells**/breast tumor initiating cells and typically demonstrate high levels of genomic instability. [(Dias, 2017)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5207440/)

>Claudin-low tumors are characterized by the low to absent expression of luminal differentiation markers, **high enrichment for epithelial-to-mesenchymal transition markers, immune response genes and cancer stem cell-like features**...  
>Despite the apparent similarity to basal-like tumors, claudin-low tumors as a group **did not show high expression of proliferation genes** and thus are likely slower-cycling tumors...  
>Molecular characterization of the claudin-low subtype reveals that these tumors are significantly **enriched in EMT and stem cell-like features while showing a low expression of luminal and proliferation-associated genes** [(Prat, 2010)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3096954/)

>The **proliferation** gene cluster, which is usually highly expressed by poor outcome subtypes such as Basal‐like, HER2‐enriched and Luminal B tumors, is **expressed at low levels in almost all Claudin‐low samples**, although it does not reach the low levels observed in the Luminal A or Normal Breast‐like groups. This data suggests that Claudin‐low tumors might be slow cycling tumors....   
>However, Claudin‐low cell lines are still highly enriched with genes involved in wound/inflammatory responses compared to the other cell lines [(Prat, 2011)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5528267/)

<!--- 
## EMT

1) Regulators
 - CTNNB1
 - TCF3
 - SNAI1
 - HMGA2
 - FOS
 - FN1
 - MAPK13 ?

2) Cell-Cell-adhesion:
 - CTNNB1
 - FYN

## Innate Immune

Immuno-stimulatory cytokine pathway:
 - STAT3
 - IL4R

NK activating receptors:
 - FYN

Integrins:
 - FN1

Immunostimulatory core pathways:
 - ROCK1
 - GSK3B
 - JUN

REcruitment of immune cells:
 - FN1

Immunosuppressive core pathways:
 - CTNNB1
 - PIAS1
 - MAPK13

Immunosuppressive MiRNA and TF:
 - CTNNB1
 - FOS

Immuno-suppressive cytokine pathways:
 - STAT3
 - IL4R

 
## Proliferation

Cell Survival:
  - GSK3B
  - JUN
  - FOS
  - ROCK1
  - PIAS1
  - HUWE1
  - SNAI1
  - TCF3
  - STAT3
  - IGFR1
  - FGF13
  - MAPK13
 --->

## After a Literature Search

### Our readout nodes will be:

1. STAT3 (all 3)
2. SNAI1 (EMT, Stemness)
3. MAPK13 (Proliferation, EMT)
4. FYN (EMT)
5. CCNG2 (EMT)

The other nodes were excluded because their observed expression in both our attractor states and our differential expression data were opposite of what would be predicted based on literature, or because they would not be good readout nodes. Literature evidence is found [here](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project2/OLD/NetworkAnalysis%201/SFA_2/candidateRONs.xlsx).

<!---
CTNNB1 should be up but it's down  
TCF3 should be up but is down [23090119]  
FGF13 should be up but is down  
FOS should be up but it's down   
HMGA2 should be up but it's down (http://grantome.com/grant/NIH/R21-CA179735-01)    
JUN should be up but it's down  
ROCK1 should be up but it's down [27203208]



PIAS1 only has one edge going in and one going out 
Furhtermore, while beta catenin and TCF3 are related to TNBC tumorigenesis, their expression levels may not be indicative of the phenotype, meaning they wouldn't be good readout nodes. [25658419]
--->