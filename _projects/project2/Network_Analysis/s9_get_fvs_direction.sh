#!/bin/bash
#SBATCH --job-name=mds
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 10
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --mail-type=END
#SBATCH --mem=20G
#SBATCH --mail-user=madeleine.gastonguay@uconn.edu
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err

echo `hostname`

module load python/3.6.3

python3 ./scripts/mds.py 'insilico_screening/MDAMB231_1/FVS_12/Stim_2' 'perturb_both.txt' 'ref_attrs_both.txt' 'k5'
