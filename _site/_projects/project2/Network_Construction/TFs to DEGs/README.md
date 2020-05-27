TFs to DEGs
======

## Description

This folder contains files used to identify TF-FunDEG interactions.

## Folder Architecture

**convertTFBS.Rmd** Takes output from GeneXplain TF analysis and generates a list of TFs that bind to FunDEGs

**IPAedges.sif** Contains TF-FunDEG interactions pulled from IPA

**omnipath edges default edge.csv** contains output from omnipath 

**omnipath_edeges.sif** Contains edges from omnipath in .sif format

**Pearson.sif** Contains edges obtained by Pearson Correlation analysis on expression data

**TF_toDEG_table.csv** is the output of **convertTFBS.Rmd** where TF is the sitemodelID of the TF, symbol is the TF, and gene is the FunDEG of interest

**TFBS_9_pulldown.\*** is downloaded from GeneXplain and contains information about TFBSes. It is an input for **conveertTFBS.Rmd**

**TFs_TFID** Contains site IDs for TFs from GeneXplain. It is an input for **convertTFBS.Rmd**.

**TFs_toTFID.csv** Contains Gene symbols for each TF and the corresponding site ID. It is an input for **convertTFBS.Rmd**.

**Pearson** Is a folder containing files needed to run Pearson correlation

**TF_to_FunDEG.sif** Contains all edges between TFs and FunDEGs.



