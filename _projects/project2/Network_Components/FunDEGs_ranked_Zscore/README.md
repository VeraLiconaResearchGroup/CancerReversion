FunDEGs Ranked by Z-score
===========

###  Description  
FunDEGs are functionally related differentially expressed genes that make up the first layer of the signaling network. The results in this folder are from OFTEN analysis applied to DEGs ranked by psuedo z-score.

### Folder Architecture  

**231_expressed_zscore_filtered_4652.csv** is a csv file including including FPKM and normalized values for each RNAseq replicate of MCF10A and MDAMB231, as well as base mean, log fold change, pvalue, and  z-score produced from differential expression analysis. It only includes DEGs with a p-value less than 0.001, and ranked from highest z-score to lowest.

**Calculate_Zscore.Rmd** is the R script used to calculate the differential expression z-score column in the above two columns.

**FunDEGs_FOC_LCC_noHKG_80** is the list of 80 first order connectivity LCC genes, after removing 3 housekeeping genes.

**FunDEGs_FOC_top650** Is the top 650 DEGs ranked by pseudo z-score to identify First Order FunDEGs

**FunDEGs_rankDEGs_zscore_12359** is a list of expressed genes in MDAMB231.

**FunDEGs_rankDEGs_zscore_pvalFDR_4652** is a list of 4652 DEGs with p-value < 0.001 and FDR < 0.05, ranked by z-score


**FunDEGs_SOC_exprnoHKG_316.txt** is  a list of  the 316 expressed genes from the SOC analysis, after removing housekeeping genes.

**weighted_sums.Rmd** is the R script used to calculate weighted sums of DEG, FOC, and SOC lists to chose the optimal list to move forward with.

**FirstOrder_FunDEG_analysis.xlsx** Contains the results from BiNOM and the graph used to select the optimal number of genes

**FunDEG_session.cys** Is the cytoscape 2 session for identifying First Order and Second Order FunDEGs

**IPAdata.txt** Is a file containing the necessary data for IPA analysis

**parseData.py** Is a script used to parse IPAdata.txt to only the First Order FunDEGs or the Second Order FunDEGs