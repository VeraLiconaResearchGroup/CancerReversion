virtual_screening
=========

## Description

This folder contains inputs and outputs of virtual screening and classification of attractors estimated from concerted perturbations of FVS nodes.


### <i>in silico</i>\_screening
SFA can originally be described in [Lee and Cho, 2018](https://www.nature.com/articles/s41598-018-23643-5). The source code in this repository has been modified from [This Github repository](https://github.com/dwgoon/sfa)
- SFA_FCperturbations.py: code to predict signal propagation, modified to perform in silico screenings of FC perturbations. This code requires an input network, a set of readout nodes, their steady state value at a given attractor, the network nodes, their basal values, and the FC nodes. The code will compute steady state attractor from the network nodes' basal values + FC perturbation (inhibitions or activations) that satisfies that a user set number of readout nodes are flipped in steady state value from the input (negative to positive, vice versa). The code will output 1) the FC perturbation 2) the steady state values of the readout nodes, 3) the steady state values of all network nodes. This code will be updated to automate the process, and setting the threshold for a successful perturbation pattern. The steady state values are computed as in the following equation:
```x_s=αWx_s+(1−α)b(1−α)(I−αW)−1b
```
$\text{S}_1(N) = \sum_{p=1}^N \text{E}(p)$

where x_s is the log of the activity of node x at the steady state.

- SFAoutput_ron_FC1_2.txt: output of FC perturbation with readout nodes' steady state values, and the computed direction of activity change (DAC) between the perturbation steady state value and input steady state value. The DAC is the difference between these two described values, which is analogous to a logFC.



## Folder Architecture

**successful_perturbations.txt** Is a list of perturbations that triggered a shift to the goal cluster when applied to all four initial conditions of MDA-MB-231.

**MDAMB231_\*** Contains datasets of attractors resulting from perturbations of the FVS nodes applied to each initial condition of MDA-MB-231.

**basal_states.txt.tar.gz** Contains the basal states of FVS nodes in the 100,000 preturbations. -1 = knockd-out, 1 = knocked-in, and 0 = no change.

**perturbation_level_factor1.5.txt** Contains the knocked-in expression value for FVS nodes when knock-ins aree simulted as 1.5\*mean expression for MDA-MB-231

**perturbation_level_factor2.txt** Contains the knocked-in expression value for FVS nodes when knock-ins aree simulted as 2\*mean expression for MDA-MB-231

**perturbation_level_sd.txt** Contains the knocked-in expression value for FVS nodes when knock-ins aree simulted as mean + 3\*sd of expression for MDA-MB-231

**successful_perts_freq_orientation.txt** Contains the frequency of knock-ins, knock-outs, and no changes for each SFA in the 157 successful perturbations.

