OLD
==============================

### Description
This folder contains preliminary analysis that did not work or have been refined in the final pipeline.


### Folder Architecture

**Network Construction 1** Contains files used to construct the network using the Second Order FunDEGs as the first layer of the network. This resulted in too many FunDEGs without known interactions with TFs.

**Network Construction 2** Contains files used to construct the network using First Order FunDEGs as the first layer of the network, but results from MR search with step 7 for the last layer. This resulted in unrelasitically small FVS sets.

**Network Analysis 1** Contains virtual screenings applied to the network constructed with MRs from step 7 (results from **Network Construction 2**).

**Network Analysis 2** Was done using discretized intial conditions for the reference attractors and using the estimated attractor landscape to classify virtual screening results. The attractor landscape is not utilized in the final pipeline due to findings from the SFA exploration.
