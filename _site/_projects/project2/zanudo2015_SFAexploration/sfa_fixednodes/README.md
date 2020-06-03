sfa_fixednodes
========

## Description

This folder contains the attractors simulated from initial conditions in the basin of Zanudo's 6 Apoptosis and 2 Leukemia attractors of the Boolean model, while fixing the corresponding stable motif intervention nodes.

**Motif Label**|**Stable Motif Intervention**
:-----:|:-----:
L1|Ceramide = OFF, SPHK1 = ON 
L2|Ceramide = OFF, PDGFR = ON 
A1|TBET = ON, Ceramide = ON, RAS = ON
A2|TBET = ON, Ceramide = ON, GRB2 = ON 
A3|TBET = ON, Ceramide = ON, IL2RB = ON 
A4|TBET = ON, Ceramide = ON, IL2RBT = ON 
A5|TBET = ON, Ceramide = ON, ERK = ON
A6|TBET = ON, Ceramide = ON, MEK = ON, PI3K = ON 

## Folder Architecture

**\*_initial.txt** contains the initial states in the basin of each attractor in the Boolean model.

**allDACs.py** calculates pairwise DAC between attractors simulated by SFA between each of the initial conditions in the basin of the Apoptosis and Leukemia attractors.

**Distribution_of_fixed_sfa_logss.pdf** shows the distribution of log steady state values for each readout node estimated by SFA.

**get_ref.py** generates dataframes of reference attractors for use in kmeans clustering of the attractor landscape. 

**logss_fixednode_dist.R** is the R script to generate **Distribution_of_fixed_sfa_logss.pdf**.

**nodes_to_fix** is the index of each node that must be fixed and its orientation for each initial condition.

**sfa_\*_states.txt** is the output of SFA applied to each state in **\*_initial.txt**, with the corresponding stable motif nodes fixed.

**sfa_Apop_all.txt** is a dataframe of all attractors simulated from initial conditions in the basin of all apoptosis attractors.

**sfa_ref_\*.txt** are files of reference attractors for k-means clustering.

**SFA1.py** is the script used to simulate attractors with SFA.

**Tolerance_FixedNodes** Contains the DAC between the attractors estimated with different tolerance levels for SFA from the 6 apoptosis initial conditions and two Leukemia initial conditions described by Zanudo with stable motif nodes fixed.
