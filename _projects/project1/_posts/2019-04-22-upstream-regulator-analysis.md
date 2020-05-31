---
layout: post
title: "Upstream Regulator Analysis"
date: "2019-04-22"
author: maddie
tags:
 - project01
 - static_network
---

## TRANSPATH: Master Regulators with Context Genes and Weighting

*Note: We edited this workflow by removing an option to weight the input transcription factors.*

First, we converted the IDs of the proteins we had data for from [Lawrence et.al](https://www.sciencedirect.com/science/article/pii/S2211124715003411?via%3Dihub) to gene Ensembl IDs and compared them to our SOC genes. This yielded 52 genes that had protein data, meaning the other 23 SOC genes will have a weight of 0 when running TRANSPATH. This data was provided as [quantitative mass spec data](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/MDAMB231_1_PepQuant.csv) with [replicates](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/MDAMB231_2_PepQuant.csv). We used the [intensity counts](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/ProteinIntensity_raw.xlsx) of both replicatets normalized by total proteome intensity for each sample and by the number of theoretically observable peptides for the protein when weighting the data.

![Protein and genes]({{ site.baseurl }}\_assets\images\Venn_protien_SOC.png)

We used the list of SOC genes converted to transpath peptides and added a column for average intensity from the protein data. This column was used to weight edges to direct signal flow towards nodes with higher protein intensity and away from those with low or none. We first ran the workflow with a step size of 10.

We ran this workflow on both the list of 8 TFs from all tissues and the list of 3 TFs from breast tissues. The master regulators genereated from the first list covered all 8 TFs as well as around 20 downstream genes whereas the MRs generated from the second list only covered 2 of the 3 TFs and about 7 downstream genes. 
 
After examining the genes included in the list of TFs from all tissues, they are related to EMT and other hallmarks associated with CL breast cancer, so we decided to move forward with that list.


## TRANSPATH: Master Regulators in Mutated Network

Next, we ran TRANSPATH with this mutational workflow in geneXplain, which gives only pathways not including mutations. We used mutational data from [COSMIC Complete Mutation Data](https://cancer.sanger.ac.uk/cosmic/download) specific to MDA-MB-231. 
- Need to run SNP-matching on the COSMIC data before putting it into the workflow.

We will move forward with the master regulators in the intersection of the weighted TRANSPATH workflow and the mutational TRANSPATH workflow so we don't include mutated pathways in the static network.


## TAKE TWO: 5/14/19

We tested three TRASPATH pathways:
1. Context genes with mutations
	- Need to run SNP matching to go from rsID to gene ID and produce a track of SNPs
	- Need to run VEP and use the result as the input for the mutational data
2. Context genes with weighting and mutations
	- Deal with mutational data the same way described above
	- Context gene file needs a column with the weights (SOC_noHKG_75_proteinabundance)
3. Context genes with weighting and mutations minus the intersection
	- Deals with mutational data the same as above 
	- Doesn't require the MRs to be expressed in the context genes (SOC)


