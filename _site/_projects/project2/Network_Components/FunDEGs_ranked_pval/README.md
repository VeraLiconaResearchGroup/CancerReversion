FunDEGs Ranked by p-value
===========

###  Description  
FunDEGs are functionally related differentially expressed genes that make up the first layer of the signaling network. The results in this folder are from OFTEN analysis applied to DEGs ranked by p-value.

### Folder Architecture  

**231_all_expressed_genes_andprtn** Contains all genes and proteins with expression data in MDAMB231

**DEG_rankpval_top700** Is the top 700 DEGs ranked by pval

**DEGs_rankedPval_4652.txt** Contains DEGs with pval < 0.001 and FDR < 0.05, ranked by pval

**find_expressed.py** Filters Second Order FunDEGs to remove unexpressed genes

**FOC_64** Contains 64 First Order FunDEGs

**FOC_pval.xlsx** Shows the results from BiNOM and the graph used to identify the optimal number of genes

**SOC_pval_276** 276 Second Ordere FunDEGs before filtering unexpressed genes

**SOC_pval_expressed_210** 210 Second Order FunDEGs with expression data

**SOC_pval_LCC_204** Largest Connected Component of Second Order FunDEGs when unexpressed and housekeeping genes are removed

**weighted_sums.Rmd** is the R script used to calculate weighted sums of DEG, FOC, and SOC lists to chose the optimal list to move forward with.

**weightedsums\*** are the results of weighted sums

**ranked_bhpval** is a folder containing results from the same analysis applied to DEGs ranked by adjusted p-value (FDR)