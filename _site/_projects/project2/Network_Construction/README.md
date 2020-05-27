Network_Construction
==========

## Description

This folder contains input files, scripts, and output files necessary for processing edges of the network.

## Folder Architecture

**step9.cys** is the cytoscape 3 session file used to put together the layers of the network.

**networknodes_227** is a list of the 227 netowrk nodes.

**network.sif** is a .sif file of thee final network

**mutTP53 pathways.sif** is a .sif file containing pathways non canonically activateed by R280K mut TP53.

**avg_expr_all** Contains average expression of network nodes for MDA-MB-231 and MCF10A

**acsn** Contains nodes in the Atlas of Cancer Signaling Network

**network_weighted_sums.Rmd** Is a script that compares the network nodes to lists of CL TNBC related genes and the ACSN

**TFs to DEGs** Contains files necessary for edges between TFs and FunDEGs.

**MRs to TFs** Contains files necessary for edges between MRs and TFs.