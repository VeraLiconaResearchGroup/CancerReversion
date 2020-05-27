MRs to TFs
==========

## Description

This folder contains input files, scripts, and output files necessary for processing edges between MRs and TFs.

## Folder Architecture

**edges_geneSymbol.csv** is an output of **transpathtogenesymbol.py** containing the unfiltered edge output of GeneXplain with gene symbols.

**edges_real.csv** is a file containing weather or not the interactions beteween nodes in **edges_geneSymbol.csv** is activating or inhibiting, and provides literature evidence. Duplicated edges are removed in this file.

**edges.csv** is the output of **read_SBML.py**, a script that process the SBML file from GeneXplain to produce a sif file of edges. It uses Transpath ID instead of gene symbols.

**MOs** Is a list of Transpath IDs for all the nodes between TFs and MRs. It is an input for **read_SMBL.py**

**MOs Gene symbol.txt** Is a table containing MOs for all of the nodes in the pathways between TFs and MRs, and their corresponding gene symbol. It is an input for **transpathtogenesymbol.py**

**MRs expressed (prtn only) viz all.xml** is the file downloaded from the GeneXplain network visualization. It is an  input for **read_SBML.py**

**MRstoTFs_expressed.sif** Is the final .sif file of singaling pathways between MRs and TFs inlcuding only nodes with either protein or gene expression data.

**read_SBML.py**  is the script used to process the .xml file from GeneXplain and produce a .sif file of edges.

**transpathtogenesymbol.py**  is a script used to convert the output of **read_SBML.py** into edges with gene symbols instead of transpath  IDs.

**Unexpressed_removed** Is a list of nodes included in the signaling pathways that do not have expression data and have therefore beeen removed.