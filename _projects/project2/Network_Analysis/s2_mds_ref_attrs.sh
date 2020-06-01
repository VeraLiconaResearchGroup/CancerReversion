#!/bin/bash
#SBATCH --job-name=mds_ref
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --mem=20G
#SBATCH -o out/%x_%j.out
#SBATCH -e error/%x_%j.err

echo `hostname`

module load R/3.6.3

# This shell script runs 2_mds_reference.R to apply multidimensional scaling to every dataset of reference attractors and visualize the data in 2 dimensions.

# MDS with 2 dimension output can be found at reference_attrs/ref_attrs_mds_<dataset>
# Plots of the reference attractors can be found in the images folder: mds_reference_attractors.pdf

mkdir ./images

Rscript --vanilla scripts/2_mds_reference.R
