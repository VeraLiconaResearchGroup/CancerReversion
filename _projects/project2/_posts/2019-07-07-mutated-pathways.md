---
layout: post
title: "Investigating Mutational Pathways"
date: "2019-07-06"
author: maddie
tags:
 - project02
 - static_network
 - mutations
---

# Objective
Mutations play an important role in the development of cancer. The mutational profile of MDA-MB-231 is characterized using VEP and filtered for expression in our tumor sample.

## Inputs
COSMIC mutations in [VCF format](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project2/Mutations/231_SNV_COSMIC.vcf).

## VEP
[VEP](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0974-4) determines the effect of your variants (SNPs, insertions, deletions, CNVs or structural variants) on genes, transcripts, and protein sequence, as well as regulatory regions.

Using VEP in GeneXplain, we identified [879 mutations](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project2/Mutations/231_SNV_COSMIC%20table.txt) from the VCF file. We then filtered these mutations to those that cause missense, deletion, splice site changes, or frameshift changes, stop_gained, and NMD, leaving [388 mutations](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project2/Mutations/231_SNV_COSMIC%20table%20filtered%20strand%3D1.txt) in [60](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project2/Mutations/mutant_framshiftdel)  genes.


# TP53 mutation
**R280K**
[COSMIC](https://cancer.sanger.ac.uk/cosmic/mutation/overview?id=330620#pathway)


## Mevalonate Pathway
<div style="text-align:center" markdown="1">
![pathway]({{ site.baseurl }}\_assets\images\mevalonate_pathway.png)  
</div>

[wiki pathway](https://www.wikipathways.org/index.php/Pathway:WP3963)
- [upregulated by TP53 mutation](https://www.cell.com/fulltext/S0092-8674(11)01569-8)

<div style="text-align:center" markdown="1">
![pathway]({{ site.baseurl }}\_assets\images\TP53_SREBP.png)  
</div>
- TP53 [interacts with SREBP](https://www.nature.com/articles/nrc.2016.76) to upregulate the transcription of HMGCoA reductase and therefore increase activity of the mevalonate pathway
  - SREBP is expressed but does not have protein data
  - There is mRNA and/or protein data for all components of the mevalonate pathway except PMVK, MVD, and FDPS

## Chemokines
- [Chemokines act as motility factors regulated by mutant TP53](https://academic.oup.com/carcin/article/33/2/442/2463582)
- mutp53 increases ID4 which increases expression of chemokines **!! We don't have protein or mRNA data for it !!**
  - Only have mRNA for CXCL1, CXCL2, CXCL8, CXCL16, and CXCR4
- mutp53 inactivates p63 which typically decrease expression of chemokines
- **Conclusion:** Don't include pathway with ID4 in model because it's not present but we could possibly add the increased expression of chemokines as a [downstream effect of the Wnt pathway](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2727408/), which is downstream of the TGF$\beta$ pathway.

## Vitamin D Receptor Mediated Apoptosis
- [Mutant TP53 interacts functionally and physically with VDR](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2882298/pdf/nihms-207988.pdf) by interfering with the binding of VDR to nVDRE, enabling the relevant target genes to remain transcriptionally active
  - Turns vitamin D3 from death-promoting into protective
- VDR is expressed but no protein data
  - p-value is 0.09 so not included in DEGs
- mutp53 modifies VDR in a way that alters it's transcription program and increases resistance to apoptosis
> Specifically, mutp53 is tethered to chromosomal regions
containing VDRE elements, presumably through association with VDR, and to augment
transcription from promoters containing such elements.

- [mutp53 can interact functionally and physically with VDR](http://software.broadinstitute.org/gsea/msigdb/geneset_page.jsp?geneSetName=STAMBOLSKY_BOUND_BY_MUTATED_TP53)
  - Mutp53 is recruited to VDR-regulated genes and modulates their expression, augmenting the transactivation of some genes and relieving the repression of others.
  - Mutp53 increases the nuclear accumulation of VDR
  - Mutp53 converts vitamin D into an antiapoptotic agent.

## TGF$\beta$-induced metastasis

![TGFbeta pathway]({{ site.baseurl}}\_assets\images\TGFBeta_pathway.png)

- TGF$\beta$ works with oncogenic Ras and mutant-p53 to induce the assembly of a [mutant-p53/p63 protein complex](https://www.sciencedirect.com/science/article/pii/S0092867409000877?via%3Dihub)
- TGF$\beta$ is expressed but not in network
- wt TP53 response to TGF$\beta$ is tumor suppressant but the mutant response is malignant
- TGFb uses mutant-p53 to surpass the barrier that p63 raises against TGFb-induced malignant cell responses
- SMAD2 also involved
- [Cyclin G2 and Sharp-1](http://jcb.rupress.org/content/192/2/209.long) are targets of p63 and typically prevent cell migration, but p53 prevents p63 from interacting with them 
  - not expressed in our cell line
- overall pathway: TGFb –> Smad/mutantp53–| p63–| metastasis  
- Ras signaling promotes mutant-p53 phosphorylation and, in so doing, it is required for the formation of the mutant-p53/Smad complex

## Wnt Pathway is downstream of TGF$\beta$

![wnt signaling]({{ site.baseurl }}\_assets\images\Wnt_signaling.png)

[non canonical wnt5a pathway activated](https://link.springer.com/article/10.1007%2Fs10911-011-9205-5)


# BRAF mutation
[info](https://ckb.jax.org/geneVariant/show?geneVariantId=1791)

# MKi67 Mutation
No one knows what it does!

# Characterization

Ki67, E-cadherin, claudin-3, claudinin-4 and claudinin-7 low

- MKI67 is differentially expressed and there is protein present but it is not ranked high enough to be included in the FOC
  - In CL tumors Ki67 expression is low because cells are not proliferating as much, but in the cell lines the Ki67 expression is higher because they are growing
- CDH1 (E-cadherin) is expressed but doesn't have protein present
  - Not included in DEG even though it has a FC of 13, p-value 0.00005, and FDR of 0.0002 because it's **NOT IN AN OPEN CHROMATIN REGION**
- CLDN4 protein is present but it's not differentially expressed
- CLDN7 has mRNA data but no protein and it isn't differentially expressed
- CLDN4 and CLDN7 have fold changes of 218 and 25 respectively, both with p-values and FDRs of 0 but aren't in the list of DEGs because they're **NOT IN AN OPEN CHROMATIN REGION**
- CLDN3 has no mRNA or protein data
  - Not a bad thing because it's supposed to be low expression

## Claudins
[source](https://www.sciencedirect.com/science/article/pii/S0005273607004099?via%3Dihub)
- Claudins 1-10 are considered classic claudins because of the similarity of their sequences.
- May be able to polymerize (hexamers preferred oligomer for Claudin-4, smaller oligomer for Claudin-3)
-  Rely on scaffolding proteins ZO-1 and ZO-2 (gene names TJP1 and TJP2) for spatial organization of claudin-based strands in epithelial cells, both of which are expressed AND have proteins present but not in network
- Claudins have a short half life! (Claudin-4 is 4 hours)
- Claudins can be short-term regulated by phosphorylation catalyzed by MAPK, PKC, PKA (in claudin-3)
- Claudin-1 to -4 care phosphorylated by WNK4 (not expressed)
- "receptor tyrosine kinase EphA2 phosphorylates the PDZ-binding C-terminus of claudin-4, resulting in its dislocation from cell–cell contacts, due to reduced ZO-1 association"
  - EphA2 expressed and protein present but not in network
- Claudin-7 corms a paracellular cation pore for Na+
- Claudin-4 is a sealing claudin; it selectively decreases the paracellular cation permeability through tight junctions
- Heterophilic cis interactions for claudins-3 and -4

Check out [this](http://www.jbc.org/content/282/41/30005.full.pdf)
and [this](https://reader.elsevier.com/reader/sd/pii/S0005273607004099?token=CB209285961D715AD628A1EFC6D1BEA704E327FD704BBEA49A01C77FEC099EB6C4475D71B898527408A6F415DCA96027)
