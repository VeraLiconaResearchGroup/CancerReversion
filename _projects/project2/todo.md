---
layout: tasks
title : "To Do for Project Two"
category: project02
---

## Static Network Construction and Analysis Streamlined

- [x] Filter expressed genes for CNV loss
- [x] Calculate Z-score of each DEG
- [x] First Order Connectivity with BiNOM
	- Ranked by Z-score 
- [x] Second order Connectivity with BiNOM
	- filter by expressed (union of protein and gene expression data)
	- remove HKG
- [x] Weighted sums
	- Compare to ASCN EMT and innate imunity hallmarks of cancer
	- Compare to CL related genes list
	- Compare to breast cancer disease ontology
- [x] Run TRANSFAC on SOC largest connected component genes
- [x] Run TF analysis with IPA
- [x] Filter TFs with expression data and bisulfite data
- [x] GOBS and LOBS TF analysis 
- [x] Make sure TFs cover all downstream genes
- [x] Run TRANSPATH mutant pathways
	- [x] input LOF mutations
- [x] Run TRNASPATH with context genes and weighting
	- [x] Context = protein data + SOC genes weighted as 0
- [x] Literature search Mutations
- [x] Assemble network in Cytoscape and add omnipath and Pearson edges
- [x] Calculate FVS with OCSANA+
- [x] Run Signal Flow to from expermintal conditions to estimate reference attractors
- [x] Cluster Reference Attractors
- [x] Run virtual screenings
- [x] Classify Virtual Screenings Results with KNN

