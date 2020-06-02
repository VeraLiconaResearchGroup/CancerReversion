virtual_screening
=========

## Description

Signal Flow Analysis (SFA) is originally described in [Lee and Cho, 2018](https://www.nature.com/articles/s41598-018-23643-5). The source code in this repository has been modified from [This Github repository](https://github.com/dwgoon/sfa). Here, we use SFA to estimate the effect of perturbations on the long term behavior of the network using only the topology of the network and identify perturbations that may trigger tumor reversion. The SFA algorithm calculates the steady state activity of the network with the following equation:

<img src="https://latex.codecogs.com/gif.latex?x_s=&space;(1-\alpha)(I-\alpha&space;W)^{-1}b" title="x_s= (1-\alpha)(I-\alpha W)^{-1}b" />

where <img src="https://latex.codecogs.com/gif.latex?x_s" title="x_s" /> is a matrix of the log of the activity of each network node at steady state, <img src="https://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /> is a hyper parameter, W is a matrix with the weight of links between network nodes, and b is a matrix with the basal activity of each network node.

This folder contains inputs and outputs of virtual screening and classification of attractors estimated from concerted perturbations of FVS nodes.

## Folder Architecture

**successful_perturbations.txt** Is a list of perturbations that triggered a shift to the goal cluster when applied to all four initial conditions of MDA-MB-231.

**MDAMB231_\*** Contains datasets of attractors resulting from perturbations of the FVS nodes applied to each initial condition of MDA-MB-231.

**basal_states.txt.tar.gz** Contains the basal states of FVS nodes in the 100,000 preturbations. -1 = knockd-out, 1 = knocked-in, and 0 = no change.

**perturbation_level_factor1.5.txt** Contains the knocked-in expression value for FVS nodes when knock-ins aree simulted as 1.5\*mean expression for MDA-MB-231

**perturbation_level_factor2.txt** Contains the knocked-in expression value for FVS nodes when knock-ins aree simulted as 2\*mean expression for MDA-MB-231

**perturbation_level_sd.txt** Contains the knocked-in expression value for FVS nodes when knock-ins aree simulted as mean + 3\*sd of expression for MDA-MB-231

**successful_perts_freq_orientation.txt** Contains the frequency of knock-ins, knock-outs, and no changes for each SFA in the 157 successful perturbations.

