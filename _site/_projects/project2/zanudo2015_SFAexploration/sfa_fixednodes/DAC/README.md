DAC
====

## Description
This folder contains the results of calculating the DAC between the RONs between attractors simulated by SFA with fixed motif interventions from intial states leading to Apoptosis and Leukemia attractors in the Boolean model.

## Folder Architecture

**DAC_A_L1_all.txt** contains the DAC between all of the Apoptosis attractors and the attractors simulated from states in the basin of the Leukemia1 boolean attractor. 

**DAC_A_L1_rons.\*** contains the DAC between the RONs of all of the Apoptosis attractors and the attractors simulated from states in the basin of the Leukemia1 boolean attractor. 

**DAC_A_L2_all.txt** contains the DAC between all of the Apoptosis attractors and the attractors simulated from states in the basin of the Leukemia2 boolean attractor. 

**DAC_A_L2_rons.\*** contains the DAC between the RONs of all of the Apoptosis attractors and the attractors simulated from states in the basin of the Leukemia2 boolean attractor. 

**Hamming_distace_no0.xlsx** contains the summary of results of hamming distance between the DAC of RONs with non-zero DAC between SFA attractors and that between Boolean attractors at different tolerance levels.

**hamming.xlsx** shows the number of comparisons with each hamming distance for comparisons of apoptosis attractors against attractors from states in the basin of Leukemia1 and Leukemia2.

**RON0_dist_\*.pdf** shows the distribution of the predicted DAC amoung all comparisons of apoptosis attractors versus either attractors simualted from the states in the basin of Leukemia1 attractor (L1) or Leukemia2 attractor (L2) in order to determine if there is a pattern in how we are mis-predicted the DACs that should be zero.

**ron0_dist.R** script to generate **RON0_dist_\*.pdf**.