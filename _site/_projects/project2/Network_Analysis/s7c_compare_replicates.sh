#!/bin/bash
#SBATCH --job-name=compknn
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --mem=1G
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err

echo `hostname`

# This shell script calls 8c_compare_replicates.py to compare classifications of attractors from virtual screenings
# of perturbations applied to each experimental replicate for one value of k and one dataset

############### User Inputs: ##############
#Specify the folder containing knn results
export knn_folder='knn_logss'

#Specify the Number of neighbors used for training
export numneigh=3

#Specify the name of the perturbed FVS or FC set
export FC='FVS_12'
##########################################

module load python/3.6.3

# Run comparison. Resultant table will be in virtual_screening folder
python3 ./scripts/8c_compare_replicates.py $knn_folder $numneigh $FC
