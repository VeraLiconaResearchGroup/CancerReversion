scripts
=========

## Description

This folder contains all scripts necessary to identify and prioritize putative reversion targets. The scripts should be run in the following order:

| Script  | INPUTS  | OUTPUTS |
| ----------------| -------------------------  | ------------------------- |
| 1_estimate_reference_attractors.py  |  1. The intracellular signaling network in .sif format<br>2. A dataframe of normalized RNAseq expression data for all experimental conditions (rows = nodes, columns = attractors) |   1. ref_attrs_logss.txt: a dataframe containing the log steady state values of each network node for all simulated attractors <br>  2. ref_attrs_logss_disc.txt: a dataframe containing the discretized log steady state values of each network node for all simulated attractors<br>  3. ref_attrs_DAC.txt: a dataframe containing the calculated direction of activity change (DAC) values f each network node for all simulated attractors<br>  the calculated DAC is the (specified attractor state value)- (simulated attractor state value).<br>  4. ref_attrs_DAC_disc.txt: a dataframe containing the discretized calculated direction of activity change (DAC) values of each network node for all simulated attractors<br>  5. ref_attrs_both.txt: a dataframe containing the log steady state values AND DAC values of each network node for all simulated attractors<br>  6. ref_attrs_both_disc.txt: a dataframe containing the discretized log steady state values and discretized DAC values of each network node for all simulated attractors  |
| 2_mds_reference.R |  Each reference dataframe |   1. dataframe with first two dimensions<br>  2. scree plots with mds stress<br>  3. plots of first two dimensions of reference attractors   |
| 3_kmeans_reference.py | Dataset of reference attractors |   1. Cluster labels for each reference attractor at each value of k<br>  2. Dataframe with sum of squared differences at each k value<br>  3. Silhouette plot to determine optimal k  |
| 4a_generate_basal_states.py | Number of perturbation combinations to generate, Number of FVS nodes to perturb, and Output location for perturbations  | dataframe of unique combinations of 0, 1, -1  |
| 4b_calculate_activation.py  |   1. list of FVS nodes<br>  2. Normalized expression values from experimental conditions |   1. dataframe with activation level of each FVS node |
| 5_virtual_screenings.py |   1. Network.sif<br>  2. List of FVS nodes<br>  3. Randomly generated perturbations of FVS set<br>  4. Activation values for FVS nodes   |   1. attr_logss.txt: a dataframe containing the log steady state values of each network node for all simulated attractors <br>  2. attr_logss_disc.txt: a dataframe containing the discretized log steady state values of each network node for all simulated attractors<br>  3. attr_DAC.txt: a dataframe containing the calculated direction of activity change (DAC) values f each network node for all simulated attractors<br>  the calculated DAC is the (specified attractor state value)- (simulated attractor state value).<br>  4. attr_DAC_disc.txt: a dataframe containing the discretized calculated direction of activity change (DAC) values of each network node for all simulated attractors<br>  5. attr_both.txt: a dataframe containing the log steady state values AND DAC values of each network node for all simulated attractors<br>  6. attr_both_disc.txt: a dataframe containing the discretized log steady state values and discretized DAC values of each network node for all simulated attractors |
| 6_combine_sfa.py  |   1. Split files from SFA (perturb_dataseti.txt)  |   1. A single file with all attractors from virtual screenings  |
| 7_knn.py  |   1. Reference Attractors<br>  2. Dataframe of attractors from virtual screenings |   1. knni.txt: Labels for each attractor when classified with i nearest neighbors<br>  2. knni_goal.txt: Attractors classified in the goal cluster when using i nearest neighbors<br>  3. knni_distance.txt: Distance between each attractor from virtual screenings and the attractors in the training set<br>  4. knni_index.txt: The index of the nearest neighbors of each attractor ordered from closest to furthest |
| 8a_compare_datasets.py  | logss, DAC, both, logss_disc, DAC_disc, both_disc datasets from virtual screenings  |   1. knn_comp_i.txt: A file with the number of datasets classified each perturbation as normal<br>  2. A table showing the size of the intersection between classification of attractors in the goal cluster between datasets  |
| 8b_compare_num_neigh.py | Files with attractors classified in the goal cluster for k values 1-8 |  A table showing the size of the intersection between classification of attractors in the goal cluster between different values of k  |
| 8c_compare_replicates.py  | Classifications of attractors from virtual screenings applied to each experimental replicate of MDA-MB-231  |   1. A table showing the numbr of perturbations resulting in attractors in the goal cluster from eeach of the initial conditions<br>  2. A table showing the size of the intersection between classification of attractors in the goal cluster between initializations<br>  3. A list of perturbations resulting in attractors in the normal cluster from all four initial conditions  |
| 9_fvs_direction.py  |   1. Basal states of randomly generated perturbations of FVS nodes<br>  2. A list of perturbations resulting in attractors in the goal cluster<br>  3. A list of FVS nodes | A file with the frequency of each perturbation orientation (knocked-in, knocked-out, or no change) for the perturbations resulting in attractors in the goal cluster  |

The folder also contains scripts for auxiliary analyses:

| Script  | Purpose |
| ------- | ------- |
| convert_ID.R | Converts enseml ID to Gene Sybmol for RNAseq expression data from second sourcee. |
| differential_expression.R | Calculates differential expression with RNAseq expression data from second source. |
| examine_activation_levels.R | Creates figures to compare activation levels to expression levels of other network nodes. |
| examine_attractors.py | Calculates the standard deviation of the expression of each node in the cancerous and normal attractors and returns the attractor values of the FVS nodes. |
| feedback_loops.py | Attempts to identify FVS nodes in negative feedback loops but needs editing. |
| generate_basal_states_lockedNodes.py | Generates a pre-defineed number of perturbations of the FVS nodes with some nodes "locked" in a specific orientation in all perturbations. |
| kmeans_perturbations.py | Runs kmeans on the results of virtual screenings. |
| mds_perturbations.py | Runs multi dimensional scaling on the results of virtual screenings. |
| reference_attractors_flipped.py | Simulates reference attractors for the test analysis where the initial conditions for GSK3B and CTNNB1 are swapped in the normal and cancerous cell lines. |
| sfa_heatmaps.R | Generates heatmaps of the log steady state attractors of virtual screenings and the experimental RNAseq data. |
