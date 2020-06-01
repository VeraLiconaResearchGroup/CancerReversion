#!/bin/bash
#SBATCH --job-name=kmeans_perts
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err
#SBATCH --time=20-00:00:00
#SBATCH --mem-per-cpu=2G   # memory per CPU core
#SBATCH -n 14 # run 14 jobs
#SBATCH -c 1 # 1 cpu for each job

echo `hostname`

module load python/3.6.3

# This shell script calls kmeans_perutrbations,.py to run kmeans on the results of virtual screenings

########## User Inputs: #############
# Specify path to folder with virtual screening results
export folder='virtual_screening/MDAMB231_1/FVS_12'

#Specify the dataset of attractors from virtual screening to run kmeans om
export dataset='both_disc'
###################################

echo $dataset

mkdir -p $folder/kmeans_$dataset

# Run kmeans with 2 - 15 clusters
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 2 $folder $dataset 0 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 3 $folder $dataset 1 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 4 $folder $dataset 2 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 5 $folder $dataset 3 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 6 $folder $dataset 4 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 7 $folder $dataset 5 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 8 $folder $dataset 6 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 9 $folder $dataset 7 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 10 $folder $dataset 8 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 11 $folder $dataset 9 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 12 $folder $dataset 10 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 13 $folder $dataset 11 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 14 $folder $dataset 12 &
srun -N 1 -n 1 python3 ./scripts/kmeans_perturbations.py 15 $folder $dataset 13 &
wait

