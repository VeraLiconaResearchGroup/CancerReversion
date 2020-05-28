---
layout: post
title: "Identifying Functionally Related Genes"
date: "2019-06-19"
author: maddie
tags:
 - project02
 - static_network
 - RNAseq
 - CNV
 - Cytoscape 2
 - BiNOM
---

# Objective
While traditional network construction methods use the most differentially expressed genes as the basis for their network, our approach to building the static network starts with [functionally related genes](https://waset.org/publications/307/categorization-and-estimation-of-relative-connectivity-of-genes-from-meta-often-network). These genes may not necessarily be the *most* differentially expressed in the set (they must be expressed in the cell), but form  a functional core of genes. This poses a problem  because highly differentially expressed genes tend to be downstream of trascription factors and other regulators that may not exhibit large changes in activity. Hence, traditional methods may exclude upstream elements that play an important role in regulation of differentially expressed genes. We will use the Cytoscape plugin BiNOM with the Human Protein Reference Database (HPRD) to identify these functional relationships amoung differentially expressed genes.

## Filtering Expressed Genes
[RNA-seq data](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-018-4533-0) was used to calculate [differential gene expression](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/tree/dev/_projects/project2/Differential_Expression) between our Claudin Low cell line of interest, MDA-MB-231, and our control normal-like breast cell line, MCF10A.  
We are using the list of unfiltered DEGs as the list of all [12359 expressed genes](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Network%20Components/FunDEGs/FunDEGs_rankDEGs_zscore_12359) in MDA-MB-231 because if they have a calculated fold change, they had enough reads to be considered expressed.

Filtering via CNV loss data from [canSAR](https://cansar.icr.ac.uk/cansar/cell-lines/MDA-MB-231/copy_number_variation/loss/ ) webpage. If the gene is listed as having a CNV loss, we removed it from the list of genes.

However, we found that the list of expressed genes didn't include any genes with CNV loss because list of genes in CNloss file are either not in the raw data, or have zeros for all runs.
- ex: DAZ, USP9Y, IFNA5 have zeros for all 8 reads in [raw data.](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Network_Components/data2.csv)

 
<div style="text-align:center" markdown="1">

![alt text]({{ site.baseurl }}\_assets\images_proj2\Venn_allgenes_vs_CNloss.png)

</div>

## Calculating z-scores
After filtering the list of expressed genes for **FDR<0.05** and **P-value<0.001**, we ranked the remaining 4652 genes from [highest to lowest z-score](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Network_Components/FunDEGs_ranked_Zscore/FunDEGs_rankDEGs_zscore_pvalFDR_4652).

The Z-score was calculated according to the equation below where $e_{ca}$ is the average expression of a gene in the cancerous cell line, $\mu_N$ is the average expression of the same gene in the normal cell line, and $\sigma_N$ is the standard deviation of the 4 gene expression measurements in the normal cell line. The absolute value of the Z-score was used when ranking lists.

<p align="center">
	$Z = \frac{e_{ca}-\mu_N}{\sigma_N}$
</p>

This method was taken from [Rathi et al., 2015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4160810/). The Z-score reflects the cancerous expression level compared to the distribution of normal samples, and is related to the probability that the expression in the tumor is from the same distribution as is in the normal tissue.

The R code used to calculate the Z-scores is shown below:

```R
# Read in expression data for all expressed genes (all DEGs) filtered by CNL
## Note: In this case, none of our genes had CNL
data2 <- read.csv("data2.csv")

#Create data table with only normalized data for MCF10a
df <- data2 %>% select(Gene_Symbol, N_MCF10A_1, N_MCF10A_2, N_MCF10A_3, N_MCF10A_4)
df$SD<- apply(df[,-1], 1, sd)
df$mean <- data2$MCF10A.mean

#Create new data table with all info from data2 as well as z-scores
df1 <- data2
df1$sd_mcf10a <- df$SD
df1$zscore <- (df1$MDA_MB.231.mean-df1$MCF10A.mean)/df1$sd_mcf10a
df1$abs_zscore <- abs(df1$zscore)
```

## First Order Connectivity

We ran the First Order Connectivity analysis on the DEGs ranked by z-score using BiNOM. 

<div style="text-align:center" markdown="1">
![FOC analysis]({{ site.baseurl }}\_assets\images_proj2\FOC_analysis.png)
</div>

The first 650 differentially expressed genes ranked by z-score produces a largest connected component of 83.

We also ran the First Order Connectivity analusis on the DEGs rankde by adjusted p-value (FDR).
<div style="text-align:center" markdown="1">
![FOC analysis pval]({{ site.baseurl }}\_assets\images_proj2\FOC_analysis_pval.png)
</div>

The first 700 differentially expressed genes ranked by p-value produces a largest connected component of 64.

**Conclusions:** Use the First 650 DEGs ranked by z-score to identify the set of First Order FunDEGs because the score is higher and the largest connected component is larger.

There are 4 house keeping genes in the largest connected component created by this analysis. One of these is VIM, which is an important marker of EMT in claudin low TNBC, so we removed all HKG but VIM, resulting in a final [First Order FunDEG LCC](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Network_Components/FunDEGs_ranked_Zscore/FunDEGs_FOC_LCC_noHKG_80) of 80 genes.

## Second Order Connectivity

We then ran second order connectivity analysis from BiNOM on the set of First Order FunDEGs. This produced a SOC set of 378 genes that was reduced to a LCC of [316](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Network_Components/FunDEGs_ranked_Zscore/FunDEGs_SOC_exprnoHKG_316.txt) genes after removing house keeping genes and those genes without protein OR gene data.

## Weighted Sums

### Compiling Lists

When calculating weighted sums, we will compare the list of differentially expressed genes, first order connectivity largest component, and second order connectivity largest component to the following three lists:
1. [Breast Cancer Disease Ontology](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Network_Components/breast_DO.txt) genes associated to breast cancer DO term from [DOLite](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2687947/) in [GeneAnswers](http://www.bioconductor.org/packages/2.5/bioc/html/GeneAnswers.html) R package
2. Only the genes from list 2 associated with [EMT and innate immune reseponse](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Network_Components/EMT_innateimmune.txt) as these hallmarks are claudin-low specific
3. [CL specific genes](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Network_Components/CL_genes.txt) as identified in [literature](http://cancerres.aacrjournals.org/content/77/9/2213)

### Calculating Weighted Sums
```{r}
weightedsums<-data.frame(gene_set = NA, number_genes = NA, HOC= NA, breastDO= NA, CLgenes=NA, sum=NA)
class(weightedsums$sum)<-'numeric'

varlist<-list(rankedDEGs$X1,FOC$X1,SOC$X1)
for (i in varlist){
  ilen<-length(i)
  x<-length(intersect(i,HOC$X1))/ilen
  y<-length(intersect(i,breastDO$X1))/ilen
  z<-0
  SUM<-((1/3)*x)+((1/3)*y)+((1/3)*z)
  weightedsums[nrow(weightedsums)+1,] = list(NA,ilen,x,y,z,SUM)
}
weightedsums<-weightedsums[-1,]
weightedsums[2,1]<-'DEG'
weightedsums[3,1]<-'FOC'
weightedsums[4,1]<-'SOC'


g1 <- ggplot(data= weightedsums, aes(x = gene_set, y =sum)) +
		geom_bar(stat="identity", aes(fill = gene_set)) +
		ggtitle("Weighted Sums") + xlab("Gene list") +
		ylab("Weighted Sum") + theme(legend.position = "none")
```

![weighted sums]({{ site.baseurl }}\_assets\images_proj2\weightedsums_plusTABLE.png)

Clearly, the set of SOC genes has the highest weighted sum. The claudin-low related genes in this list are CAV1, CDC20, DSP, ERBB2, KRT8, PTTG1, and VIM. It is interesting to notice that FOXA1 and GATA3 are not in the SOC or FOC set but are in the list of DEGs.


**Conclusion:** Run TRANSFAC and TF analysis in IPA with the [SOC](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project2/Network_Components/FunDEGs_ranked_Zscore/FunDEGs_SOC_exprnoHKG_316.txt) list of 316 genes because it has the highest wieghted sums.