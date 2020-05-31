---
layout: post
title: "Network Construction"
date: "2019-06-06"
author: maddie, lauren
tags:
 - project01
 - static_network
---

# Objective
Assemble all the network components and add signed edges in Cytoscape 3.


<div style="text-align:center" markdown="1">
![network]({{ site.baseurl }}\_assets\images\network_image.png){:height="150%" width="150%"}

![network]({{ site.baseurl }}\_assets\images\network_organic.png)
</div>

## Network Specifications

- **198** nodes in the network
    - We don't have the signs of the edges for ARIH2
    - Supposedly interacts with CTF2I, NFYC, RELA, TCF7L2, TFAP4, but can't find any literature
- **28** source nodes
- **384** edges (wihtout ARIH2)


## Weigthed Sums for Network

We ran the network nodes through weighted sums to see their relevance to CL TNBC. Details regarding the lists we compare to can be found in [Identifying Functionally Related Genes]({{ site.baseurl }}{% post_url 2019-04-08-functionally-related-genes %})

![weighted sums]({{ site.baseurl }}\_assets\images\WeightedSums_network.png)

[Network intersection with HOC](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/network_int_HOC.txt)  
[Netowrk intersection with CL genes](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/network_int_CLgenes.txt)  
[Network intersection with Breast DO](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/network_int_breastDO.txt)  


# New Mutations in Network

**NF2**

Gene expression FC: -15  
Protein intensity: ~800

- nonsense mutation p.E231*
- typically inhibits MAPK pahtway with MEK and ERK
	- our nonsense mutation means that they will be activated
- We think we should remove NF2 from the network becasue the mutation causes the protein to be extremely truncated and nonfunctional 
	- then we'd only have 27 source nodes!
- geneXplain gives us the wrong sign


### After Network Modifications:  
We couldn't determine the nature of the interaction between our transcription factors and ARIH2, but we do know that it activates TP53 so we glued it into the network that way. We also removed NF2 from the network because of its loss of function mutation.  

After making this change, we now have:  
- **[197](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/network_nodes.txt)** nodes in the network 
    - because we removed NF2  
- **[28](https://github.com/VeraLiconaResearchGroup/CancerReversion/blob/master/_projects/project1/gene_network/sourcenodes.txt)** source nodes because we removed NF2 but added ARIH2  
- **387** edges  


# FVS set

We ran FVS with 50 iterations and got 6 FC sets:

['GTF2I', 'JUN', 'TCF7L2', 'CSNK2B', 'MYC', 'EP300', 'RELA']  
['JUN', 'CSNK2B', 'GSK3B', 'MYC', 'EP300', 'RELA']  
['JUN', 'TCF7L2', 'AKT', 'CSNK2B', 'MYC', 'GTF2I', 'RELA']  
['JUN', 'TCF7L2', 'CSNK2B', 'MYC', 'EP300', 'RELA']  
**['MYC', 'JUN', 'RELA', 'CSNK2B', 'AKT']**  
['RELA', 'JUN', 'TCF7L2', 'AKT', 'MYC', 'CSNK2B']  