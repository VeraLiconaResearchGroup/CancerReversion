setwd("./") # Change WD
.libPaths("~/R_libs")
# library(tidyverse)
library(fpc)

#Plotting clusters of attractors

##################### User Specifications ############################
# Please specify the number of clusters you are visualizing
k =11 #If k greater than 10, need to manually add colors

# Select which dataset you used to calculate kmeans
# 1 for logss, 2 for DAC, and 3 for both
d <- 1

# provide vector with which clusters you want visualized
viz <- seq(0,k-1)
# viz<-c(1,3,4) #use this with numbers of clusters that are less than total
######################################################################

datasets <- c("logss", "DAC", "both")
data_set <- datasets[d]

# Read in dataset that was used to calculate kmeans
plotdf <- read.table("sfa_logss_disc.txt", header = TRUE, row.names = 1) 


# Read in dataframe with kmeans cluster assignments for each cluster
clusters <- read.table(paste("kmeans_ss/kmeans_ss_",k,".txt", sep = ""), row.names =1, header = TRUE) 
names(clusters) <- "Cluster"
cl <-clusters$Cluster

# Get names of refernce attractors
# ref <- read.table("inputfiles/reference_attractors.txt", header = TRUE,  nrow = 1, row.names = 1)%>%names()
ref <- c('L1.1', "L1.2", "L2.1", "L2.2", "A5.1", "A5.2", "A5.3")
# ref <- c('Leukemia', "Apoptosis")
l <- length(ref)

#Calulate discriminant coordinates for each cluster
coordinates<-discrcoord(plotdf, cl)

#Write out discriminant coordinates
write.table(coordinates$proj, paste("dc_coords_", data_set, "_kmeans_",k, ".txt", sep = ""))

# Can alter these colors to chose different ones, or add more if you have more than 10 colors
col_opt <- c("darkslateblue", "deeppink1","aquamarine3", "royalblue" , "orchid1",  "darkorchid", "firebrick3", "goldenrod2", "darkslategray", "grey")
# col_opt <-rainbow(k)
col_opt <- c('#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080')

# Making colors transleucent
col_opt_T <- col_opt
for( n in 1:length(col_opt)){
  rgb.val <- col2rgb(col_opt[n])
  col_opt_T[n] <- rgb(rgb.val[1], rgb.val[2], rgb.val[3], max = 255, alpha = 0.2*255)
}

color <- rep(col_opt_T[1], nrow(clusters))
for(n in 1:k-1){
  color[cl == n] <- col_opt_T[n+1]
}

# Colors for phenotype reference triangles
ref_col <- c()
for(n in 1:l){
  c <- cl[n]
  ref_col[n] <- col_opt[c+1]
}

pdf(paste("Kmeans_", k, ".pdf", sep = ""))
plotcluster(plotdf, cl, pch = 1, bw = FALSE, main = paste("Attractor Landscape"), col = color)
legend("bottom", c(paste("cluster", seq(0,k-1)), ref),cex=.8, col=c(col_opt[1:k], ref_col), pch=c(rep(1, k), rep(17, l)))
points(coordinates$proj[1:l,1], coordinates$proj[1:l,2], bg=ref_col, col = "black", pch=24, cex = 1.5)
dev.off()

########## Altering plot to visualize only what we want ##############
v <- length(viz)
if(v < k){
  viz2 <- cl %in% viz
  plotdf <- plotdf[viz2,]
  vizz <- paste(as.character(viz), collapse = "_")
  coordinates <- discrcoord(plotdf, cl[viz2])
  #Write out discriminant coordinates
  write.table(coordinates$proj, paste("figures/dc_coords_", data_set, "_kmeans",k, "_",vizz,".txt", sep = ""))
  cl <- cl[viz2]
  color <- color[viz2]
  col_opt <- col_opt[viz+1]
  
    
  pdf(paste("figures/Kmeans", k, "_",vizz,".pdf", sep = ""))
  plotcluster(plotdf, cl, pch = 1, bw = FALSE, main = paste("Attractor Landscape"), col = color)
  legend("bottomleft", c(paste("cluster", viz), ref),cex=.8, col=c(col_opt, ref_col), pch=c(rep(1, v), rep(17, l)))
  points(coordinates$proj[1:l,1], coordinates$proj[1:l,2], bg=ref_col, col = "black", pch=24, cex = 1.5)
  dev.off()
  
}



