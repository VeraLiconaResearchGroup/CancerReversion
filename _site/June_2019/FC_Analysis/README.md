# FC_Analysis
The FC node set of a network is composed of the source nodes (nodes without incoming edges) and of the feedback vertex set problem (FVS) of the network. The FVS problem for a directed graph consists on finding minimal sets of vertices that intersect all cycles of the graph.
The code in this repository has been modified from [Zanudo et al., 2016](https://www.pnas.org/content/114/28/7234)

- FVS_search_10_python.py, FVS.py: code provided by Zanudo et al., 2016 to run FVS module, for other requirements for this code see the [Github repository](https://github.com/yanggangthu/FVS_python)
- 231_FVS_calculation.py: code to calculate FVS for MDA-MB-231 vs MCF10A intracellular signaling network. Requires input of network edges as 'source_node target_node'
- 231_FVS_output.txt: output of 231_FVS_calculation code. each line contains 1 FVS result from 231_FVS_calculation.py
