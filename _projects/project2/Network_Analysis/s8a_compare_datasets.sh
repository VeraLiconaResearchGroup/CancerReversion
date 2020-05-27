#!/bin/bash
#SBATCH --job-name=comp_datasets
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --mem=4G
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err

echo `hostname`

# This shell script calls 8a_compare_datasets.py to compare classifications of different datasets of attractors 
# from virtual screenings of one initial state at one vlaue of k

################ User Inputs: ####################
# Specify the experimental replciate used as an inital state for virtual screenings
export initialState='MDAMB231_1'

# Specify the name of the perturbed FVS or FC set 
export FC='FVS_12'

# Specify the number of neighbors used for classification
export numneigh=3
###################################################


# Path to knn results
export pert_foler=virtual_screening/$initialState/$FC

module load python/3.6.3

#Run comparison
python3 ./scripts/8a_compare_datasets.py $pertfolder $numneigh
