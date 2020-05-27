#!/bin/bash
#SBATCH --job-name=ref_attrs
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --mail-type=END
#SBATCH --mem=4G
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err

echo `hostname`

module load python/3.6.3

# This batch script runs 1_estimate_reference_attractors.py to estimate the attractors from normalized RNAseq expression data of experimental replicates using SFA

################## User Inputs: ##############
# Name of file containing noramalized expression data
export exp='network_nodes_normalized_expression_replicates.txt'

# Prefix of experimental data for undesired condition to compute DAC
export undesired="MDAMB231" 
###############################################

# Make folder for output files
mkdir 'reference_attrs'

# Run script
python3 ./scripts/1_estimate_reference_attractors.py $exp $undesired
