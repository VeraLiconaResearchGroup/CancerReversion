---
layout: post
title: "In Silico Screenings"
author: maddie
date: "2019-09-16"
tags:
 - project2
 - static_network
---

## Objective
Run *in silico* screenings on concerted perturbations of FVS nodes to predict their effect on the long-term behavior of the system.

**Source nodes:** MAPK6, ZBTB17, HDAC3, PRPF4, MAPK1
- PLK1, FOXM1 in feedback loop with eachother!
- RELA in self- feedback loop

## Literature Search FC Nodes
### EGFR
- receptor
- it's inhibition can revert teh HMT-3522 mammary epethelial cell line (TNBC) to a normal, growth-arrested state.
- doesn't make a difference in MDA-MB-231 when perturbed alone [[2975573](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2975573/)]
- its inhibition has been effective in non-small cell lung cancer and colorectal cancer
- small molecule tyrosine kinase inhibitors (TKIs) and monoclonal antibodies (mAbs) [[5004067](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5004067/)]

### MAPK1
- when perturbed with ITGB1, it reverted MDA-MB-231 [[2975573](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2975573/)]
- pirfenidone inhibits MAPK12 which decreases the number of cancer stem cells ([source](https://stemcellsjournals.onlinelibrary.wiley.com/doi/epdf/10.1002/stem.2068))

### HDAC3
- **entinostat** is an HDAC inhibitor and has been shown to reverse EMT in MDAMB231
- HDAC inhibitors are a new class of anitcancer agents
- doesn't require permanent changes in DNA sequence [source](    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5611517/
    https://onlinelibrary.wiley.com/doi/pdf/10.1002/jcp.22574
    https://link.springer.com/article/10.1007/s10549-018-4815-x
    http://www.oncotarget.com/index.php?journal=oncotarget&page=article&op=view&path[]=23169&path[]=73050)

### MAPK6 (ERK3)
- unstable protein rapidly degraded by the ubiquitin proteasome pathway
- physiological function unclear (as of 2016)
- ERK3 overxpressing MDA-MB-231 cells have increased cell migration speed
- activity regulated thgough cellular abundance
- significant portion localizes at the periphery of cells at the plasma membrane
- ERK3 expression levels positively correlated with substratum adhesion
- ERK3 drives morphology changes in cells
- ERK3 required to reduce spread area and prevent hyper-elongation of cells
- cells depleted of ERK3 didn't have a different migration speed than the control cells
    - it's inhibition doesn't impede cell migration
- used **shRNA** to target it

[source](https://www.researchgate.net/publication/284274541_A_novel_role_for_atypical_MAPK_kinase_ERK3_in_regulating_breast_cancer_cell_morphology_and_migration) (All experiments done in MDAMB231)


### RELA
- inactivation (by preventing phosphorylation) can reverse EMT
- **Zoledronic acid** is a bisphosphonate that targets RELA and reverses EMT and decreases self renewal in MDAMB231 ([source](https://mct.aacrjournals.org/content/molcanther/12/7/1356.full.pdf))

### PLK1
- **BI-2536**, a selective inhibitor for PLK1, triggered apoptosis in MDA-MB-231 and other TNBC cell lines
- PLK1 drives transition from G2/M so inhibiting it causes a fatal error in mitosis ([source](https://www.nature.com/articles/s41374-019-0247-4.pdf?origin=ppub))
- correlation between high levels of PLK1 and poor outcome
- PLK1 inhibitors can inhibit other PLK family members and lead to off-target effects
- design **siRNA** to target just PLK1
- siRNA inhibition of PLK1 leads to apoptosis ([source](https://mct.aacrjournals.org/content/16/4/763.long))


### FOXM1
- inhibition leads to apopotosis in 231 ([source](https://ascopubs.org/doi/abs/10.1200/jco.2013.31.15_suppl.e22063))
- FOXM1 complex a potential target ([source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6315782/pdf/cancers-10-00525.pdf))
- FOXM1 inhibition suppressed MDA-MB-231 tumorigenesis *in vivo*
- **Thiostrepton** is a specific inhibitor of FOXM1
    - increases cell death in MDA-MB-231
- its inhibition decreases proliferation
- its inhibition may inhibit EMT
- thiostrepton cannot comepletely inhibit tumor growth *in vivo*
-  "There are a number of different aspects of the
inhibitory effects of Thiostrepton. Metabolic pathways were
considerably enriched among the pathways. Notably, tumor
metabolism is associated with the tumor microenvironment
and tumor progression " ([source](https://www.spandidos-publications.com/ijo/54/1/87))


Nothing relating PRPF4 and ZBTB17 to  CL TNBC.


## In Silico Screening Results

We ran *in silico* screenings by generating all possible perturbations (0, 1, or -1) of the FC nodes (3^8 = 6561). Then we estimated the attractors resulting from these perturbations applied to the basal state of MDA-MB-231. We applied k-nearest neighbors classifier, using the 100,000 randomly simulated attractors as a training set and labels from k-means clustering of the 100,000 attractors, to classify the attractors resulting from *in silico* screenings. 

Below are the results of knn classification of the attractors from *in silico* with 19 nearest neighbors (optimal number) using kmeans clustering with 3 centroids:

![insilico]({{ site.baseurl }}\_assets\images_proj2\insilico_prelim.png)

An example of a potentially successful perturbation of 3 nodes that resulted in an attractor clustering in the same cluster as the attractor simulated from the basal state of MCF10A:
1. Inhibition of: EGFR, HDAC3, and MAPK6