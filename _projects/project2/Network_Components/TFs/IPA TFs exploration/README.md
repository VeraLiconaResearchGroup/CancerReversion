IPA TFs exploration
=========

## Description
This folder contains files used to examine if the addition of TFs from IPA can increase coverage of Second Order FunDEGs.

## Folder Architecture

**uncoveredSOC1** contains 244 Second Order FunDEGs that did not have known interactions with the 7 network TFs

**TFs_IPA_alltissues_andbreastCA_69 Genes Ensembl** contains 69 TFs from IPA

**additionalTFs_expressed_36** Consists of 36 expressed TFs that could be added to the network

**additionalCovered_61** Consists of 61 Second Order FunDEGs that those 36 TFs cover

**check_coverage.py** Is a script to identify which Second Order FunDEGs are covered through the addition of TFs.