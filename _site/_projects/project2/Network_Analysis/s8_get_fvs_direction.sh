#!/bin/bash
#SBATCH --job-name=fvs_dir
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --mem=20G
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err

echo `hostname`

# This shell script calls 9_fvs_direction.py to identify the perturbation orientation of each FVS nodes in a set of pre-defined perturbations

################# User Inputs ######################

# Specify the name of file containing list of perturbations of inteerest (assumed to be in virtual_screening folder)
export subset='successful_perturbations.txt'

# Specify name of perturbed FVS set
export FCname='FVS_12'
######################################################

module load python/3.6.3

python3 ./scripts/9_fvs_direction.py $subset $FCname


