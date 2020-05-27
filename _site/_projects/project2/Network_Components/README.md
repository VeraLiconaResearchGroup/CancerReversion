Network Components
==========

### Description  
This folder contains all the layers of the network along with the necessary related files to get them.

### Folder Architecture  

**FunDEGs** contains the files required to produce the list of ranked DEGs, FOC, and SOC. It also contains the R script needed to run weighted sums on these lists.

**TFs** contains the files required to produce a list of TFs that covers all the downstream SOC genes. It also includes the R script needed to run weighted sums on the lists produced from different step sizes. 

**breast_DO.txt** is one of the lists to compare to in weighted sums. It includes genes related to breast disease ontology according to [DOLite](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2687947/) in [GeneAnswers](http://www.bioconductor.org/packages/2.5/bioc/html/GeneAnswers.html) R package.

**EMT_innateimmune.txt** is another list to compare to in weighted sums. It includes hallmarks of cancer from the [atlas of cancer signalling network](https://acsn.curie.fr/ACSN2/ACSN2.html) related to EMT and innate immunity as those are characteristics of CL TNBC.

**CL_genes.txt** is the final list to compare to in weighted sums. It includes genes important to claudin low tumorigenesis as found in [literature](http://cancerres.aacrjournals.org/content/77/9/2213).

**normalized_replicates.txt** Contains normalized RNA-seq expression data of all expressed genes for each of the replicates

**normalized_average_expression.txt** Contains the average normalized RNA-seq expression data of all replicates of the normal-like and cancerous cell line

**networknodes_normalized_expression_replicates.txt** Contains normalized RNA-seq expression data of network nodes with gene expression data for each of the replicates

**expression_rep_disc_avg.txt** Contains normalized RNA-seq expression data of network nodes with gene expression data for each of the replicates, discretized using the mean across rows

**expression_rep_disc_med.txt** Contains normalized RNA-seq expression data of network nodes with gene expression data for each of the replicates, discretized using the median across rows

**compare_CLTNBC_contents.py** Finds the number of CL TNBC related genes that are in the Second Order FunDEGs but not the First Order FunDEGs

**data2.csv** is the results of the RNAseq differential expression analysis from Macrogen.

**expressed_HKG** is the expressed housekeeping genes