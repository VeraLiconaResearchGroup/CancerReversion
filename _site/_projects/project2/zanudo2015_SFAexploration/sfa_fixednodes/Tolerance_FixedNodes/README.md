Tolerance_FixedNodes
===========

## Description
This analysis was done to determine if increasing the tolerance level for the convergence of SFA would produce more zero DAC between readout nodes because the output is reported to fewer significant digets. All initial states in the basin of Zanudo's Apoptosis and Leukemia Boolean attractors were used as initial conditions for SFA. Tolerance levels = 10^-2, 10^-3, 10^-4, 10^-5, 10^-6, 10^-8, 10^-10, 10^-12 and machine epsilon.

## Folder Architecture

**allDACs.py** computes the DAC between each of the Apoptosis attractors against each of the Leukemia attractors.

**hamming_distance.py** calculates the hamming distance between the DAC of RONs between attractors estimated by SFA and the Boolean attractors.

**nodes_to_fix** contains the index and value of each node that should be fixed for each initial condition when simulating with SFA.

**round.py** combines all outputs from the apoptosis attractors and rounds them to the same number of digits as the tolerance level. 

**SFA1.py** is the script used to simulate attractors. The sp.py file was modified manually accordimg to **nodes_to_fox** to fix specific nodes.

**tol\*** contains the attractors simulated by SFA from initial states in the basin of the Leukemia and Apoptosis attractors with the stable motif nodes fixed for each initial state (A1-A6, L1 and L2), the DAC of all apoptosis attractors compared to each of the leukemia attractors, and the hamming distance of the DAC of RONs with non-zero DACs compared to that between Leukemia and Apoptosis attractors of the Boolean model at each tolerance level.

**tolerance.xlsx** is a summary of the results showing the number and percentage of zero DACs recovered as tolerance increases, as well as the loss in accuracy at predicting the DAC of the other RONs.

