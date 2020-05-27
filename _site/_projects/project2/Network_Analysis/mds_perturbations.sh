#!/bin/bash
#SBATCH --job-name=mds_perts
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 10
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --mem=200G
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err

echo `hostname`

# This shell script calls mds_perturbations.py to calculate MDS on the results of virtual screenings

############ User Inputs: #############
# Specify path to folder with virtual screening results
export folder='virtual_screening/MDAMB231_1/FVS_12'

# Specify dataset to apply mds to
export dataset='logss'
#####################################

module load python/3.6.3

# Make output folder for results
mkdir -p $folder/mds

#run mds
python3 ./scripts/mds.py $folder $dataset
