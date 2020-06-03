zanduo2015_SFAexploration
=========

## Description

This folder contains files, scripts, and results from the SFA exploration to determine the limitations and appropiate uses of Signal Flow Analysis.

## Folder Architecture

**100000_il15_stim_ON_s2_cd45_tax_pdgf_OFF.txt** contains the attractors of the Boolean network when simulated with 100000 initial states with IL15 and Stimuli1 ON, stimuli2, CD45 TAX, and PDGF OFF, all other nodes randomly intiailized.

**100000_il15_stim_ON.txt** contains the attractors of the Boolean network when simulated with 100000 initial states with IL15 and Stimuli1 ON, and all other nodes randomly initialized. 

**100000.txt** contains 887 attractors of the Boolean network when simulated with 100000 random initial states.

**allDACs.py** Is a script to calculate pairwise DAC between attractors estimated with SFA from initial conditions in the basin of Leukemia and Apoptosis attractors of the Boolean model.

**apoptosis_attractors.txt** Are apoptosis attractors from the Boolean model classified according to the DAC of the readout nodes.

**apoptosis5.txt** Contains intial conditions that lead to the apoptosis attractor achieved by fixing nodes in apoptosis intervention 5 when simulated wtih the Boolean model.

**atttractors.txt** ...

**bn_a_attr.txt** Contains the apoptosis attractor of the Boolean model identified by zanudo.

**bn_l1_attr.txt** Contains the Leukemia1 attractor of the Boolean model identified by zanudo.

**boolean_simulation_random_initializations.Rmd** Is a R markdown document where 100,000 pre generated random states are used as initializations and the resultant attractors simulated with the Boolean model.

**boolean_simulation.Rmd** Simulates attractors of the boolean network with stable motif nodes fixed as described in Zanudo et al.

**boolnet_A_L_attractors.txt** Leukemia and Apoptosis quasi-attractors of the Boolean model.


**boolnet_attractors_RONS.\*** Attractor values of readout nodes (RONs) for 877 attractors simulated from 100,000 random initial conditions with the Boolean model.

**boolnet_attractors.txt** 877 quasi-attractors simulated from the 100,000 random initial conditions with the Boolean model.

**boolnet_DAC.\*** Contains the DAC of each of the 877 attractors of the Boolean model compared to the Leukemia1 attractor.

**boolnet3.R** Is a draft script for simulating the network with fixed nodes.

**classify_attractors** Results of classifying attractors from the Boolean model and SFA via kmeans and DAC of RONs.

**classify_attractors_DAC_boolnet.py**  Classify attractors of the Boolean model using the DAC of RONs.

**classify_attractors_DAC_boolnet.py**  Classify SFA attractors using the DAC of RONs.

**Clustering_test** Is a folder containing results of kmeans on the Boolean attractors.

**DAC_results_L1A** is a folder of pairwise DAC between SFA attractors estimated from initial states in the basin of the Leukemia1 attractor in the Booelan model. It also contains the Hamming Distance between the DAC of RONs for each combination and the DAC of the RONs of the Leukemia and Apoptosis attractors of the Boolean model.

**DAC_results_L2A** is a folder of pairwise DAC between SFA attractors estimated from initial states in the basin of the Leukemia12attractor in the Booelan model. It also contains the Hamming Distance between the DAC of RONs for each combination and the DAC of the RONs of the Leukemia and Apoptosis attractors of the Boolean model.

**discreeTest** is a folder with results of discreeTest on SFA attractors.

**exploring_literature.Rmd** is a script that identifies the attractors of the reduced networks of Zanduo Saadatpour.

**generatee_is_matrix.py** is a script to randomly generate 100,000 initial states for simulating with SFA and the Boolean model.

**get_attractors.py** Reads the output of Boolnet and generates a dataframe of attractors.

**get_basin.Rmd** Is a script to find which initial states lead to each attractor of the Boolean model.

**get_quasi_attractors.py** Reads the output of Boolnet and generates a dataframe of quasi-attractors.

**hamming_distance.py** Calculates the Hamming Distance between the DAC of RONs for each combination of SFA attractor and the DAC of the RONs of the Leukemia and Apoptosis attractors of the Boolean model.

**images** contains figures generated from the analysis.

**initial_states_Leuk_Apop.txt** Consists of initial states used to simulate Apoptosis and Leukemia attractors with the Boolean model.

**inital_states.txt** consists of 100,000 random initializations for the model.

**inputfiles** consists the network and reference attractors.

**is_attrs_bn.txt** Is a dataframe that matches initial states to their Boolean attractors.

**is_bn_map.txt** Is a dataframe that matches initial states to their Boolean attractors and their phenotype according to readout nodes of the attractor. The Phenotype2 column marks states in the basin of the Apoptosis attractor from zanudo as apoptosis and states in the basin of either Leukemai attractor from Zanudo as Leukemia. Other states that lead to different apoptosis and leukemia attractors are marked as other in this column.

**is_to_A_L_inBN.txt** is a map of initial states that lead to Zanudo's apoptosis and leukemia attractors and their corresponding phenotype.

**kmeans.xlsx** contains the number of SFA and Boolean attractors classified as Leukemia and Apoptosis by kmeans.

**Leuk_Apop_RONs.xlsx** contains the quasi-attractors from Leukemia and Apoptosis initial conditions identified in Zanudo et al. and a separate table with the values of the RONs.

**leukemia_attractors.txt** Is a dataframe of Leukemia attractors of the Boolean model classified by the DAC of the RONs and the acitivty level of the RONs at the attractor state.

**leukemia.txt** Is a list of Leukemia attractors of the Boolean model classified by the DAC of the RONs.

**leukemia1.txt** Is a dataframe of all states in the basin of the Leukemia1 attractor in the Boolean model.

**leukemia2.txt** Is a dataframe of all states in the basin of the Leukemia2 attractor in the Boolean model.

**megaDAC.py** Calculates the DAC of each SFA attractor against all 95 SFA attractors simulated from initial states in the basin of the Boolean model.

**other_attractors.txt** RON values of attractors that are neither Leukemia nor Apoptosis associated.

**other.txt** is a list of attractors that are neither Leukemia nor Apoptosis associated according to RONs.

**quasi_DAC_RONs.xlsx** Contains results of DAC analysis in RONs.

**SFA experimentation on Zañudo 2015.ppt** contains results from the start of the analysis.

**sfa_A_L.csv** Contains the estimated SFA attractors from the Leukemia and Apoptosis intial conditions.

**sfa_apoptosis.txt** SFA attractors simulated from states in the basin of the Apoptosis attractor in the Boolean model.

**sfa_apoptosis5.txt** SFA attractors simulated from states in the basin of Apoptosis5 attractor in the Boolean model.

**sfa_fixednodes** contains results of the analysis run with fixed interventions.

**sfa_heatmaps.R** makes heatmaps of SFA attractors.

**sfa_leukemia1.txt** SFA attractors simulated from states in the basin of Leukemia1 attractor in the Boolean model.

**sfa_leukemia2.txt** SFA attractors simulated from states in the basin of Leukemia2 attractor in the Boolean model.

**sfa_ref.txt** SFA attractors arbitrarily chosen as reference attractors of the Leukemia and Apoptosis phentoype.

**SFA1.py** Is the script used to estimate attractors with SFA.

**sub_network.bn** Is a reduced network for T-LGL from Zanudo.

**sub_network2.bn** Is a reduced network for T-LGL from Saadatpour et al.

**Tolerance Exploration** Contains the DAC between the attractors estimated with different tolerance levels for SFA from the initial conditions of apoptosis1 and Leukemia1. (Outdated: see sfa_fixednodes/Tolerance_fixednodes for final analysis.)

**zanudo_boolean.bn** The T-LGL Boolean netework from Zanudo et al.

**zanudo2.pptx** is the final power point presentation for this analysis.









