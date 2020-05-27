#!/bin/bash
#SBATCH --job-name=basal
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 4
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --time=20-00:00:00
#SBATCH --mem-per-cpu=1G   # memory per CPU core
#SBATCH -n 2 
#SBATCH -c 1 
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err

echo `hostname`

module load python/3.6.3

# This shell script calls 4a_generate_basal_states.py to generate random basal states for perturbations of the FVS nodes (1 = knocked-in, -1 = knocked-out, 0 = no change)
# It simultaneously calls 4b_calculate_activation.py to calculate the value for knock-in perturbations of FVS nodes as a factor * mean expression of the experimental data for initializations to which you are applying

############ User Inputs: ################

# Number of unique random perturbations to generate
export numpert=100000

# Number of FVS nodes that need random states
export numnodes=12

# File with list of FVS or FC nodes
export FC='FVS_12'

# Prefix for experimental replicates of undesired phenotype to which perturbations will be applied
export undesired='MDAMB231'

# Factor for calculating activation level 
export factor=2

# File with normalized RNAseq expression data for experimental replicates
export nexp='network_nodes_normalized_expression_replicates.txt'

############################################

mkdir ./virtual_screening

# Run Scripts

srun -N 1 -n 1 python3 ./scripts/4a_generate_basal_states.py $numpert $numnodes &
srun -N 1 -n 1 python3 ./scripts/4b_calculate_activation.py $FC $undesired $factor $nexp
