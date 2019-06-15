# Cancer Reversion: Computational Systems Biology Approaches
This repository contains the source code and preliminary results for our computational pipeline for tumor reversion

## Cancer reversion
 is the biological process by which tumorigenic cells lose all, or a significant part of, their malignant phenotype. The objective of this project is to develop and apply novel computational systems biology tools to identify molecular drivers of cancer reversion, their mechanisms of action and their clinical application.

## June_2019
This folder contains computations and results for June_2019 grant submission, with multi-omics data from cell lines MDA-MB-231 and MCF10A . There are two subfolders.

### FC_Analysis
This folder contains the results of FC FC_Analysis on the putative intracellular signaling network for MDA-MB-231.
The FC node set of a network is composed of the source nodes (nodes without incoming edges) and of the feedback vertex set problem (FVS) of the network. The FVS problem for a directed graph consists on finding minimal sets of vertices that intersect all cycles of the graph.
The code in this repository has been modified from [Zanudo et al., 2016](https://www.pnas.org/content/114/28/7234):
- FVS_search_10_python.py, FVS.py: code provided by Zanudo et al., 2016 to run FVS module, for other requirements for this code see the [Github repository](https://github.com/yanggangthu/FVS_python)
- 231_FVS_calculation.py: code to calculate FVS for MDA-MB-231 vs MCF10A intracellular signaling network. Requires input of network edges as 'source_node target_node'
- 231_FVS_output.txt: output of 231_FVS_calculation code. each line contains 1 FVS result from 231_FVS_calculation.py

### <i>in silico</i> Screenings
To trace the dynamics of a signaling network, we can deﬁne a ‘network state’ as a tuple of values of network components at a speciﬁc time point. When there is no change in the input signal of the network system, the network state will follow the inherent network dynamics determined by interactions between network components. Eventually, the network state will converge to a steady state called an attractor.  Using only the static network, we will perform a topological estimation of signal flow, Signal Flow Analysis (SFA), to perform systems’ simulations. SFA can originally be described in [Lee and Cho, 2018](https://www.nature.com/articles/s41598-018-23643-5), and source code found in [This Github repository](https://github.com/dwgoon/sfa)
