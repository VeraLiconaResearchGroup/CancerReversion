##########################
# mds.R takes all dataframes of reference dataframes (logss, DAC, both, disc) and computes multidimensional scaling with sammon mapping on each.
# INPUTS:
# 1. Each reference dataframe
# 
# OUTPUTS:
# 1. dataframe with first two dimensions
# 2. scree plots with mds stress
# 3. plots of first two dimensions of reference attractors 
##########################

setwd("~/Documents/GitHub/gastonguay_compsysmed_labnotebook/_projects/project2/Network_Analysis/reference_attrs")
# .libPaths('~/R_libs')
library(MASS)
library(tidyverse)
library(e1071)


theme_set(theme_bw(base_size=12) + theme(panel.grid = element_blank())) # set the default plot theme for the ggplot2 library

scree.plot = function(d, k, ds) { #Function to create scree plot of stress at each dimension
  stresses=sammon(d, k=k)$stress
  for(i in rev(seq(k-1)))
    stresses=append(stresses,sammon(d, k=i)$stress)
  plot(seq(k),rev(stresses), type="b", xaxp=c(1,k, k-1), ylab="Stress", xlab="Number of dimensions", main = paste('Scree Plot for MDS on Reference Attractors', ds))
}


ds <- c("logss", "DAC", "both", "logss_disc", "DAC_disc", "both_disc")

pdf('../images/TEEST_mds_reference_attractors.pdf') #Open pdf to capture scree plots and results of MDS

for(dataset in ds){
  ref <- read.table(paste('ref_attrs_', dataset, '.txt', sep = ""), header = T, row.names = 1)
  
  d <- dist(ref) # euclidean distances between the rows
  scree.plot(d,5, dataset) #Scree plot with stress values with dimensions 2-5
  fit <- sammon(d, k=2) #MDS scaling with sammon mapping and two dimensions on reference attractors
  
  plotdf <- fit$points %>%  as.data.frame()
  names(plotdf) <- paste("PC", 1:ncol(plotdf), sep = "")
  write.table(plotdf, paste("TEST_ref_attrs_mds_", dataset, ".txt", sep = ""), row.names = T, quote = F) #Write out results of MDS
  
  plotdf$phenotype <- c(rep("Normal-like",4), rep("Cancer", 4))
  
  print(ggplot(plotdf, aes(PC1, PC2)) + geom_point(aes(color = phenotype), cex = 3) + #Plot MDS results in 2 dimensions
          geom_text(data = plotdf[1:8,], label = rownames(plotdf[1:8,]), nudge_y = .1,  cex = 3) + 
          xlim(min(plotdf$PC1)-0.5, max(plotdf$PC1)+0.5) +
          ggtitle(paste('MDS on Reference Attractors', dataset)))
  
  if(grep("disc", dataset)){
    d <- hamming.distance(ref) #Run MDS on hamming distance between discrete databases
    fit <- sammon(d, k=2) #MDS scaling with sammon mapping and two dimensions on reference attractors
    scree.plot(d,5, dataset) #Scree plot with stress values with dimensions 2-5
    
    plotdf <- fit$points %>%  as.data.frame()
    names(plotdf) <- paste("PC", 1:ncol(plotdf), sep = "")
    write.table(plotdf, paste("TEST_ref_attrs_mds_hamming_", dataset, ".txt", sep = ""), row.names = T, quote = F) #Write out results of MDS
    
    plotdf$phenotype <- c(rep("Normal-like",4), rep("Cancer", 4))
    
    print(ggplot(plotdf, aes(PC1, PC2)) + geom_point(aes(color = phenotype), cex = 3) + #Plot MDS results in 2 dimensions
            geom_text(data = plotdf[1:8,], label = rownames(plotdf[1:8,]), nudge_y = .1,  cex = 3) + 
            xlim(min(plotdf$PC1)-0.5, max(plotdf$PC1)+0.5) +
            ggtitle(paste('MDS on Hamming Distance Between Reference Attractors', dataset)))
  }
}

dev.off()
