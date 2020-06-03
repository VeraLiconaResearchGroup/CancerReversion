MDAMB231_1/FVS_12
=========
## Description
Results from Virtual Screeenings of perturbations of FVS_12 applied to the initial condition MDAMB231_1.

## Folder Architecture

**knn\_*dataset*.tar.gz** contains results of knn applied to the dataset (logss, DAC, both, and discrete versions) at k values from 2 to 8 using eucliden distance.

**knn\_*dataset*_hamming.tar.gz** contains results of knn applied to the dataset (logss, DAC, both, and discrete versions) at k values from 2 to 8 using hamming distance as a distance metric.

**perturb\_*dataset*.tar.gz** contains the estimated SFA attractors of the 100,000 FVS perturations.

**test_flip** contains the classification of attractors from virtual screenings using the reference attractors simulated from basal states with the values for CTNNB1 and GSK3B swapped between MCF10A and MDA-MB-231.
