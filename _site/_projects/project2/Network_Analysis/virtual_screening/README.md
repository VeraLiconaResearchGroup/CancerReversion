virtual_screening
=========

## Description

This folder contains inputs and outputs of virtual screening and classification of attractors estimated from concerted perturbations of FVS nodes.

## Folder Architecture

**successful_perturbations.txt** Is a list of perturbations that triggered a shift to the goal cluster when applied to all four initial conditions of MDA-MB-231.

**MDAMB231_\*** Contains datasets of attractors resulting from perturbations of the FVS nodes applied to each initial condition of MDA-MB-231.

**basal_states.txt.tar.gz** Contains the basal states of FVS nodes in the 100,000 preturbations. -1 = knockd-out, 1 = knocked-in, and 0 = no change.

**perturbation_level_factor1.5.txt** Contains the knocked-in expression value for FVS nodes when knock-ins aree simulted as 1.5\*mean expression for MDA-MB-231

**perturbation_level_factor2.txt** Contains the knocked-in expression value for FVS nodes when knock-ins aree simulted as 2\*mean expression for MDA-MB-231

**perturbation_level_sd.txt** Contains the knocked-in expression value for FVS nodes when knock-ins aree simulted as mean + 3\*sd of expression for MDA-MB-231

**successful_perts_freq_orientation.txt** Contains the frequency of knock-ins, knock-outs, and no changes for each SFA in the 157 successful perturbations.

