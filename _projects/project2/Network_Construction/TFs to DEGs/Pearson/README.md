Pearson
======

## Description

This folder contains files needed to run Pearson Correlation at different confidence levels. It was run five times (0.99, 0.95, 0.9, 0.85, 0.80)

## Folder Architecture


**covered\*** Contains a list of FunDEGs that have been covered by edges at each correlation level. Input for **getuncovered.py**

**expm\*** Is the expression matrix for MDA-MB-231 for uncovered nodes at each run. Output of **getuncovered.py**

**FunDEGs_FOC_LCC_noHKG_80** Conatains First Order FunDEGs. Input for **getuncovered.py**

**getuncovered.py** Identifies which FunDEGs do not have TF regulators and produces an expression matrix for those genes to re-run Pearson correlation

**MDA231_expressionMatrix.txt** Is a matrix with expression data of MDA-MB-231 for network nodes. Input for **getuncovered.py**

**TFs_APIPA_9**  Is a list of network TFs. Input for **getuncovered.py**

**uncovered\*** Contains a list of FunDEGs that do not have known TF regulators at each run. Output of **getuncovered.py**
