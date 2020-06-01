#!/bin/bash
#SBATCH --job-name=knn
#SBATCH -n 9
#SBATCH -c 4
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --mem-per-cpu=3G
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err

echo `hostname`

# This shell script runs 7_7_knn.py to classify the attractors from virtual screenings of perturbations 
# applied to one initial state of the undesired phenotype using the reference attractors as the training set.


################ User Inputs: ###################
# Specify which experimental replicate perturbations were applied to
export initialState='MDAMB231_1'

# Specify name of FVS or FC set that was perturbed
export FC='FVS_12'

# Specify the number of clusters in the training set (either 2 or 4 for our data)
export ncl=4
###################################################

echo $initialState
echo $FC
echo $ncl

export pert_folder=virtual_screening/$initialState/$FC

# Make directories for output
mkdir -p $pert_folder/knn_logss
mkdir -p $pert_folder/knn_DAC
mkdir -p $pert_folder/knn_both
mkdir -p $pert_folder/knn_logss_disc
mkdir -p $pert_folder/knn_DAC_disc
mkdir -p $pert_folder/knn_both_disc
mkdir -p $pert_folder/knn_logss_disc_hamming
mkdir -p $pert_folder/knn_DAC_disc_hamming
mkdir -p $pert_folder/knn_both_disc_hamming

module load python/3.6.3

# Run knn on sepcfied dataset with specifid distance metric (minkowski or hamming)
srun -N 1 -n 1 python3 ./scripts/7_knn.py logss $pert_folder minkowski $ncl 0 &
srun -N 1 -n 1 python3 ./scripts/7_knn.py DAC $pert_folder minkowski $ncl 1 &
srun -N 1 -n 1 python3 ./scripts/7_knn.py both $pert_folder minkowski $ncl 2 &
srun -N 1 -n 1 python3 ./scripts/7_knn.py logss_disc $pert_folder hamming $ncl 3 &
srun -N 1 -n 1 python3 ./scripts/7_knn.py DAC_disc $pert_folder hamming $ncl 4 &
srun -N 1 -n 1 python3 ./scripts/7_knn.py both_disc $pert_folder hamming $ncl 5 &
srun -N 1 -n 1 python3 ./scripts/7_knn.py logss_disc $pert_folder minkowski $ncl 6 &
srun -N 1 -n 1 python3 ./scripts/7_knn.py DAC_disc $pert_folder minkowski $ncl 7 &
srun -N 1 -n 1 python3 ./scripts/7_knn.py both_disc $pert_folder minkowski $ncl 8 &
wait
