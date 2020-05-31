---
layout: post
title: "Identifying Functionally Related Genes"
date: "2019-04-08"
author: maddie
tags:
 - project01
 - static_network
---

## Filtering Expressed Genes
RNA-seq data from [here](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-018-4533-0)
We are using the list of unfiltered DEGs as the list of all [expressed genes](https://drive.google.com/file/d/1ihB95WGH6Qw9jnLh1zQKSOHgcaoHNePh/view?usp=sharing) in MDA-MB-231 because if they have a calculated fold change, they had enough reads to be considered expressed.

Filtering via CNV loss data from [canSAR](https://cansar.icr.ac.uk/cansar/cell-lines/MDA-MB-231/copy_number_variation/loss/ ) webpage. If the gene is listed as having a CNV loss, we removed it from the list of genes.

However, we found that the list of expressed genes didn't include any genes with CNV loss because list of genes in CNloss file are either not in the raw data, or have zeros for all runs.
- ex: DAZ, USP9Y, IFNA5 have zeros for all 8 reads in [raw data.](https://drive.google.com/file/d/1YR5rj8VQLB0Kun2ivURzbOR8ahXApBnH/view?usp=sharing)

We are also filtering by [methylation and acetylation data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4868673/). Inclusion criteria is that genes have both a methylation AND acetylation fold enhancement value whose absolute value is greater than or equal to 2. If this proves to be too stringent, we will use the absolute value of the methylation OR acetylation fold enhancement greater than or equal to 2.

This filtering resulted in [6783](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/expressed_openregions_6784.txt) *unique* genes.


<div style="text-align:center" markdown="1">

![alt text]({{ site.baseurl }}\_assets\images\Venn_allgenes_vs_chromatin_vs_CNloss.png)

</div>

## Calculating z-scores
After filtering the list of expressed genes for FDR<0.05 and P-value<0.001, we will try two ways of ranked DEGs when running BiNOM:
1. From [lowest to highest p-value](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/rankedDEGs_FDR05_Pval001.txt)


2. From [highest to lowest z-score](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/rankedDEGs_FDR05_Pval001_rankedzscore.txt)

The Z-score was calculated according to the equation below where $e_{ca}$ is the average expression of a gene in the cancerous cell line, $\mu_N$ is the average expression of the same gene in the normal cell line, and $\sigma_N$ is the standard deviation of the 4 gene expression measurements in the normal cell line. The absolute value of the Z-score was used when ranking lists.

<p align="center">
	$Z = \frac{e_{ca}-\mu_N}{\sigma_N}$
</p>

This method was taken from [Rathi et al., 2015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4160810/). The Z-score reflects the cancerous expression level compared to the distribution of normal samples, and is related to the probability that the expression in the tumor is from the same distribution as is in the normal tissue.

The R code used to calculate the Z-scores is shown below:

```R
df1 <- read.csv("231_expressed_openchromatin_6783.csv")
#Create data table with only normalized data for MCF10a
df <- df1[,c(3,21:24)]

df$SD<- apply(df[,-1], 1, sd)
df1$sd_mcf10a <- df$SD

df1$zscore <- (df1$MDA_MB.231.mean-df1$MCF10A.mean)/df1$sd_mcf10a
```

## First Order Connectivity

### Ranked by P-value

![P-Value_FOC]({{ site.baseurl }}\_assets\images\FOC_analysis_pval.png)

### Ranked by Z-score

![Zscore_FOC]({{ site.baseurl }}\_assets\images\FOC_analysis_zscore.png)


**Conclusion:** Move forward with the list of [differentially expressed genes ranked by z-score](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/rankedDEGs_FDR05_Pval001_rankedzscore.txt). This produces a largest connected component of [30 genes](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/FOC_LCC).

## Second Order Connectivity

Moving forward with list of first [250 differentially expressed genes](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/rankedDEGs_FDR05_Pval001_rankedzscore_top250.txt) ranked by z-score.

After filtering second order connectivity results for those that are expressed in our data, removing house keeping genes, and then taking the largest connected component, we are left with a list of [75 genes](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/SOC_LCC_expr_nohkg).

## Weighted Sums

### Compiling Lists

When calculating weighted sums, we will compare the list of differentially expressed genes, first order connectivity largest component, and second order connectivity largest component to the following three lists:
1. [Breast Cancer Disease Ontology](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/breast_DO.txt) genes associated to breast cancer DO term from [DOLite](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2687947/) in [GeneAnswers](http://www.bioconductor.org/packages/2.5/bioc/html/GeneAnswers.html) R package
2. The complete [hallmark of cancer list](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/HOC.txt) from the [atlas of cancer signalling network](https://acsn.curie.fr/ACSN2/ACSN2.html)
3. Only the genes from list 2 associated with [EMT and innate immune reseponse](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/EMT_innateimmune) as these hallmarks are claudin-low specific

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
![weighted sums]({{ site.baseurl }}\_assets\images\weightedsums_plusTABLE.png)

**Conclusion:** Run TRANSFAC and TF analysis in IPA with the [SOC](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/SOC_LCC_expr_nohkg) list of 75 genes because it has the highest [weighted sum](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/weightedsums_fegm.txt).
