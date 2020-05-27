#!/bin/bash
#SBATCH --job-name=kmeans
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err
#SBATCH --time=20-00:00:00
#SBATCH --mem-per-cpu=2G   # memory per CPU core
#SBATCH -n 12 
#SBATCH -c 1 

echo `hostname`

module load python/3.6.3

# This shell script runs 3_kmeans_reference.py to apply unsupervised kmeans clustering to different dataset of the reference attractors
# The script runs kmeans with k values from 2 to the number of reference attractors on the specified dataset

# Make directory for results of kmeans on each dataset
mkdir -p reference_attrs/kmeans_logss
mkdir -p reference_attrs/kmeans_DAC
mkdir -p reference_attrs/kmeans_both
mkdir -p reference_attrs/kmeans_logss_disc
mkdir -p reference_attrs/kmeans_DAC_disc
mkdir -p reference_attrs/kmeans_both_disc
mkdir -p reference_attrs/kmeans_mds_logss
mkdir -p reference_attrs/kmeans_mds_DAC
mkdir -p reference_attrs/kmeans_mds_both
mkdir -p reference_attrs/kmeans_mds_logss_disc
mkdir -p reference_attrs/kmeans_mds_DAC_disc
mkdir -p reference_attrs/kmeans_mds_both_disc

# Run kmeans on each dataset. kmeans classifications at each k found in reference_attrs/kmeans_<dataset> folder 
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_logss 0 &
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_DAC 1 &
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_both 2 &
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_logss_disc 3 &
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_DAC_disc 4 &
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_both_disc 5 &
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_mds_logss 6 &
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_mds_DAC 7 &
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_mds_both 8 &
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_mds_logss_disc 9 &
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_mds_DAC_disc 10 &
srun -N 1 -n 1 python3 ./scripts/3_kmeans_reference.py kmeans_mds_both_disc 11 &
wait

