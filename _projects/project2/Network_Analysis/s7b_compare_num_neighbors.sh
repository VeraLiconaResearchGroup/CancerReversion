#!/bin/bash
#SBATCH --job-name=compnn
#SBATCH -n 9
#SBATCH -c 1
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --mem=1G
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err

echo `hostname`

# This shell scropt calls 8b_compare_num_neigh.py to compare classifications of one dataset of 
# virtual screenings across different numbers of neighbors used for classification

########## User Inputs: ##############
# Specify which experimental replicate to wich perturbations were applied
export initialState='MDAMB231_1'

# Specify which FVS or FC set was perturbed
export FC='FVS_12'
########################################

echo $initialState

module load python/3.6.3

# Compare classifications for all knn analysis simultanousely 
srun -N 1 -n 1 python3 ./scripts/8b_compare_num_neigh.py knn_logss $initialState $FC  0 &
srun -N 1 -n 1 python3 ./scripts/8b_compare_num_neigh.py knn_DAC $initialState $FC  1 &
srun -N 1 -n 1 python3 ./scripts/8b_compare_num_neigh.py knn_both $initialState $FC  2 &
srun -N 1 -n 1 python3 ./scripts/8b_compare_num_neigh.py knn_logss_disc $initialState $FC  3 &
srun -N 1 -n 1 python3 ./scripts/8b_compare_num_neigh.py knn_DAC_disc $initialState $FC  4 &
srun -N 1 -n 1 python3 ./scripts/8b_compare_num_neigh.py knn_both_disc $initialState $FC  5 &
srun -N 1 -n 1 python3 ./scripts/8b_compare_num_neigh.py knn_logss_disc_hamming $initialState $FC  6 &
srun -N 1 -n 1 python3 ./scripts/8b_compare_num_neigh.py knn_DAC_disc_hamming $initialState $FC  7 &
srun -N 1 -n 1 python3 ./scripts/8b_compare_num_neigh.py knn_both_disc_hamming $initialState $FC  8 &

wait