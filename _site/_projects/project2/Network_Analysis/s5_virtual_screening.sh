#!/bin/bash
#SBATCH --job-name=virtual_screening
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err
#SBATCH --time=20-00:00:00
#SBATCH --mem-per-cpu=2G   # memory per CPU core
#SBATCH -n 6
#SBATCH -c 1

echo `hostname`


# This shell script calls 5_virtual_screenings.py to estimate attractors from pre calculated perturbations of FVS nodes applied to initial states of the undesired phenotype.
# Basal states of perturbations are split into files of 20,000 and the resultant attractors are estimated simultaneously from each of these files. Once SFA has been completed for each file,
# the outputs of SFA applied to each set of basal states is combined into one dataframe of 100,000 attractors via 6_combine_sfa.py.

################ User Inputs: ##################
# Experimental condition to use as initial state and to which perturbations will be applied
export initialState="MDAMB231_1" #OR MDAMB231_2, MDAMB231_3, MDAMB231_4

# Name of file containing FVS or FC nodes
export FC='FVS_12'

# Factor used to calculate activation level for knock-in perturbations
export stim=2

# Prefix of experimental conditions of undesired phenotype for claculating DAC
export undesired='MDAMB231'

# File name for normalized RNAseq expression data for experimental replicates
export nexp='network_nodes_normalized_expression_replicates.txt'
########################################

echo $initialState
echo $FC
echo $stim

# Make folder to contain results from split basal state files
mkdir -p ./virtual_screening/$initialState/$FC/splitfiles

module load python/3.6.3

# Eatimate attractors with SFA
srun -N 1 -n 1 python3 ./scripts/5_virtual_screenings.py $FC $initialState 1 $stim $undesired $nexp 0 &
srun -N 1 -n 1 python3 ./scripts/5_virtual_screenings.py $FC $initialState 2 $stim $undesired $nexp 1 &
srun -N 1 -n 1 python3 ./scripts/5_virtual_screenings.py $FC $initialState 3 $stim $undesired $nexp 2 &
srun -N 1 -n 1 python3 ./scripts/5_virtual_screenings.py $FC $initialState 4 $stim $undesired $nexp 3 &
srun -N 1 -n 1 python3 ./scripts/5_virtual_screenings.py $FC $initialState 5 $stim $undesired $nexp 4 &
wait

# Combine split dataframes into a single dataframe for each dataset
srun -N 1 -n 1 python3 ./scripts/6_combine_sfa.py $FC $initialState logss_disc 0 &
srun -N 1 -n 1 python3 ./scripts/6_combine_sfa.py $FC $initialState DAC_disc 1 &
srun -N 1 -n 1 python3 ./scripts/6_combine_sfa.py $FC $initialState both_disc 2 &
srun -N 1 -n 1 python3 ./scripts/6_combine_sfa.py $FC $initialState logss 3 &
srun -N 1 -n 1 python3 ./scripts/6_combine_sfa.py $FC $initialState DAC 4 &
srun -N 1 -n 1 python3 ./scripts/6_combine_sfa.py $FC $initialState both 5 &
wait
