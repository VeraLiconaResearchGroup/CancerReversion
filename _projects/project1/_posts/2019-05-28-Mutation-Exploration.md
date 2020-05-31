---
layout: post
title: "Mutation Exploration"
date: "2019-05-28"
author: lauren, maddie
tags:
 - project01
 - static_network
 - VEP
 - mutations
---
# Order of Attack
- [x] Define our Inputs
- [x] Define VEP
- [x] venn COSMIC mutations with gene expression data
- [x] Venn 48 expressed with protein Data
- [x] Data Dig pt 1
	- [x] look into 10/33 no gene expression, no protein mutated genes
  - [x] look into 10/29 where we don't have protein Data
- [x] characterize GOF and LOF
  - [x] Really make sure definition of LOF means **zero** function to the protein
          - **It Doesn't**
- [x] Bulk TRANSPATH
  - [x] on 48 expressed
  - [x] on 19 with protein
- [x] Map experimental data onto TRANSPATH results
- [x] Discuss


# Goal
The Goal of this experiment is to determine a systematic and as automated as possible way to incorporate mutational data into our network building. We will characterize the 231 mutations using VEP, filter them for expression in our tumor samples, and then use TRANSPATH as our pathway database. After obtaining results, we will map expression onto the TRANSPATH pathways to observe enrichment or lack thereof in the mutated genes.

## Inputs
COSMIC mutations in VCF format.

## VEP
[VEP](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0974-4) determines the effect of your variants (SNPs, insertions, deletions, CNVs or structural variants) on genes, transcripts, and protein sequence, as well as regulatory regions.

Using VEP in GeneXplain, we identified [879 mutations](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/geneXplain_backup/old/231_SNV_COSMIC%20table.txt) from the VCF file. We then filtered these mutations to those that cause missense, deletion, splice site changes, or frameshift changes, leaving [370 mutations](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/geneXplain_backup/old/231SNV_COSMIC%20table%20filtered_framemisssplicedel.txt). This corresponds to [81 genes](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/geneXplain_backup/old/231SNV_COSMIC%20table%20filtered_framemisssplicedel%20Ensembl.txt).

**Note:** When filtering by mutation you should also include stop_gained and "NMD" mutations! (learned this the hard way)

## Mutations vs Gene Expression Data

<div style="text-align:center" markdown="1">
![alt text]({{ site.baseurl }}\_assets\images\cosmicgenes_vs_allgenes.PNG)
</div>

## Expressed vs protein Data
<div style="text-align:center" markdown="1">
![alt text]({{ site.baseurl }}\_assets\images\expressedcosmic_vs_proteins.PNG)
</div>

## Data Dig
#### <u>Sample of no gene expression, no protein, mutated genes</u>
ABCA4
- p.D1204N: recycling of retinoid pigment in eye. Known mutant gene in breast cancer, does not affect any pathways

- KLK9 p.G15W: protease. known mutant gene in breast cancer, does not affect any pathways

LGSN
- p.G427C:ay act as a component of the cytoskeleton or as a chaperone for the reorganization of intermediate filament proteins during terminal differentiation in the lens. known mutant gene in breast cancer, does not affect any pathways

LRRK2
- p.I2330S: Positively regulates autophagy through a calcium-dependent activation of the CaMKK/AMPK signaling pathway.
known mutant gene in breast cancer, does not affect any pathways

MAGEB3
- p.D234N: Melanoma-associated antigen B3. known mutant gene in breast cancer, does not affect any pathways  

NLRP11
- p.V149L: regulates caspases in the proinflammatory signal transduction pathway and, based on studies of other members of the NLRP gene family with similar domain structure, is predicted to form part of the multiprotein inflammasome complex

OR51D1
- Olfactory receptors interact with odorant molecules in the nose, to initiate a neuronal response that triggers the perception of a smell  

PCDH15
- cadherin; mutations lead to hearing loss  

TSPO2
- cholesterol binding  

TTLL9
- ligase activity

#### <u>Sample of the expressed but no protein mutated genes</u>
ALPK2
- kinase

ATP8B2
  - phospholipid transferring ATPase

CRTC3
- part of CREB regulated transcription coactivator gene family
- induce mitochondrial biogenesis and attenuate catecholamine signaling in adipose tissue

GAS8
- regulator of ciliary/flagellar motility

HAUS3
-  plays a key role in cytokinesis and mitosis
LONP1
- p.R542Q: protein mediates the selective degradation of misfolded, unassembled or oxidatively damaged polypeptides in the mitochondrial matrix.

LRIG2
- p.H628R: epidermal growth factor signaling, resulting in increased proliferation, glioma cells.

MSH3
- p.G896R,p.G887R: mismatch repair. bad in Endometrial cancer and FAP

PROM2
- p.H334Y: neutral mutation

ZBTB1
- p.D351V: DNA repair and is an upstream regulator of translesion DNA synthesis.


#### Characterization of GOF and LOF

According to the Jackson Laboratory,  
$\quad$ A [**gain-of-function**](http://www.informatics.jax.org/glossary/gain-of-function) mutation is characterized as "a type of mutation in which the altered gene product possesses a new molecular function or a new pattern of gene expression. Gain-of-function mutations are almost always Dominant or Semidominant."  
$\quad$ A [**loss-of-function**](http://www.informatics.jax.org/glossary/loss-of-function) mutation is characterized as "a type of mutation in which the altered gene product lacks the molecular function of the wild-type gene."


### TRANSPATH Results
**TRANSPATH Pipeline:** Find master regulators in networks, step 10, with context genes (all expressed genes)



