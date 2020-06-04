test_RNAseq2
=======

## Description

The results from classification of attractors from virtual screenings indicate the knock-in of GSK3B and CTNNB1 as
putative reversion interventions. This is contrary to prior evidence that GSK3B inhibition decreases EMT and Stemness and 
CTNNB1 inhibition has reversed EMT [[1](https://www.spandidos-publications.com/10.3892/or.2016.5311), [2](https://breast-cancer-research.biomedcentral.com/articles/10.1186/s13058-019-1125-0)].
We noticed that the normalized RNA-seq expression values of GSK3B and CTNNB1 are higher in the normal-like cell line replicates than in the cancerous
cell lines (MDAMB231/MCF10A log2 fold change = -1.85 and -1.82, respectively), and we wanted to determine if that expression pattern is standard in MDA-MB-231 and MCF10A expression patterns,
or if it is a unique characteristic of the data we are using. RNA-seq count tables for MDA-MB-231 and MCF10A were taken from [GSE75168](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE75168),
and differential expression analysis was conducted with [DESeq2](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-014-0550-8) to determine if this same trend is observed in the data from the second study.
We found that the log2 fold change values from this study showed the same trend for GSK3B (logfc = -1.13), but the opposite trend for CTNNB1 (logfc = 1.56).


1. Lin et al., Oncology Reports, 2016
2. Vijay et al., Breast Cancer Research, 2019
