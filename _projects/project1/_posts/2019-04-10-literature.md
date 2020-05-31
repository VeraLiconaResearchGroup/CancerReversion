---
layout: post
title: "Literature"
date: "2019-04-10"
author: maddie
tags:
 - project01
 - static_network
 - boolean_network
---
# About
This post contains links to interesting and relevant papers or data sources to look into.

# Look into?
[Principles and Strategies for Developing Network Models in Cancer](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3082135/pdf/nihms283558.pdf)

[On the Dependency of Cellular Protein Levels on mRNA Abundance](https://www.sciencedirect.com/science/article/pii/S0092867416302707?via%3Dihub)

[Cancer Attractors](https://www.sciencedirect.com/science/article/pii/S1084952109001499?via%3Dihub)

# Weighted Sums
[Innate Imune Response](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5669567/)
- not effective to target adaptive immunity

# Random
[CMA and TRANSPATH with feedback loop](https://link.springer.com/epdf/10.1186/s12859-019-2687-7?author_access_token=sVKkYS1vthjs4IRR996zWG_BpE1tBhCbnbw3BuzI2RPhTLlVAL5qq8LtDv8FankfDgVDIqk0LGtYnBvOyZmdZODwt45qEYsirKS_SU5CgtJn3M-l8KDgIgttz64tXmFosEIyOXhw9lVO4lK-ETDVhw%3D%3D)   

# Mutations
[Filtereing DEGs for CNV and methylation data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4160810/) 
  - First step before running BiNOM

Maddie:  
[10 pathways](https://www.cell.com/cell/pdf/S0092-8674(18)30359-3.pdf)  
  - Talks about interconnectedness of mutant Pathways
  - Not useful for learning how to deal with mutations

Lauren:  
[Comprehensive Characterization of Cancer Driver Genes and Mutations](https://www.cell.com/cell/pdf/S0092-8674(18)30237-X.pdf)  
[Typing tumors using pathways selected by somatic evolution](https://www.nature.com/articles/s41467-018-06464-y.pdf)  
[MUFFINN](https://www.inetbio.org/muffinn/tutorial.php)  

[Making CNV profiles](https://www.nature.com/articles/s41588-018-0179-8)

[Gain of and Loss of TF binding site mutations](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0174032)



# Proteomics networks
[Signaling networks via Proteomics](https://www.nature.com/articles/nrm2900)
   - Label-free MS is good when precise determination of ratios is not required
    - doesn't require experimental manipulation
  - protein data is useful to directly determine the effects of perturbations in terms of protein abundance
  - talks about the advantages of protein signaling networks but doesn't tell you methodology

[Pathway and Network Analysis of Cancer Genomes](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4717906/)
  - " The activating effect of a mutation in a transmembrane receptor can be masked by inactivation of a downstream effector of the same signaling pathway."
  - "CONEXIC assumes that copy number gains and losses alter gene expression. It employs a Bayesian Network algorithm to find significantly altered genes regulating modules of differentially expressed genes."
  - "[PARADIGM] uses factor graphs to assign weights to each molecular interaction and to integrate the effects of multiple simultaneous alterations (e.g. copy number changes, simple somatic mutations, expression changes)"

# Boolean Network
[Overview](https://onlinelibrary.wiley.com/doi/epdf/10.1002/wsbm.1273)
[network structure to logical molecule](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4990565/)
[logical modelling summary](https://www.frontiersin.org/articles/10.3389/fgene.2016.00094/full)
[Maximum Number of fixed points in Boolean Network](https://link.springer.com/article/10.1007/s11538-008-9304-7)

### Train with static Data
[Sharan](https://europepmc.org/backend/ptpmcrender.fcgi?accid=PMC3590894&blobtype=pdf)
[Almudevar](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3215431/pdf/sagmb1727.pdf)
[Zhu](https://www.nature.com/articles/srep23078.pdf)
[Guziolowski](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3753570/pdf/btt393.pdf)
[Videla](https://arxiv.org/pdf/1210.0690.pdf)
[Mitsos](https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1000591&type=printable)

### Time series Data
[Razzaq](https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1006538&type=printable)
[Thesis](https://tel.archives-ouvertes.fr/tel-02021019/document/)
[Dorier](https://bmcbioinformatics.biomedcentral.com/track/pdf/10.1186/s12859-016-1287-z)
[231 example](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2932856/pdf/nihms-221294.pdf)


#CL realted Genes
[patient study classifying subtypes](http://cancerres.aacrjournals.org/content/77/9/2213)

# DATA
## MDA-MB-231
[RNA-seq](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-018-4533-0)
  - [GSE96860](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE96860)
[ChIP-seq](http://www.oncotarget.com/index.php?journal=oncotarget&page=article&op=view&path[]=6922&pubmed-linkout=1)
  - [GSE69377](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE69377)
[Proteomics](https://www.sciencedirect.com/science/article/pii/S2211124715003411?via%3Dihub)
  - [PRDB004167](https://www.proteomicsdb.org/#projects/4167/3085)
[Bisulfite](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2013-14-10-r110)
  - [GSE42944](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi)
[Mutational Data](https://cancer.sanger.ac.uk/cell_lines/sample/overview?id=905960)
  - SNV and CNV
[Phosphoproteomics](https://onlinelibrary.wiley.com/doi/epdf/10.1002/elps.201300586)
  - [PXD000948](http://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD000948)
Perturbation

## BT-549
RNA-seq
ChIP-seq
[Proteomics](https://www.sciencedirect.com/science/article/pii/S2211124715003411?via%3Dihub)
  - [PRDB004167](https://www.proteomicsdb.org/#projects/4167/3085)
[Bisulfite](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2013-14-10-r110)
  - [GSE42944](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi)
[Mutational Data](https://cancer.sanger.ac.uk/cell_lines/sample/overview?id=905951)
  - SNV and CNV
Phosphoproteomics
Perturabtion

## MCF10A
RNA-seq (see above two sources)
[ChIP-seq](http://www.oncotarget.com/index.php?journal=oncotarget&page=article&op=view&path[]=6922&pubmed-linkout=1)
  - [GSE69377](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE69377)
[Proteomics](https://www.sciencedirect.com/science/article/pii/S2211124715003411?via%3Dihub)
  - [PRDB004167](https://www.proteomicsdb.org/#projects/4167/3085)
[Bisulfite](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2013-14-10-r110)
  - [GSE42944](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi)