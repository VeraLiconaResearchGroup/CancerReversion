# Clustering 100,000 simulated attractors

setwd("~/Clustering")
.libPaths("~/R_libs")
library(ClassDiscovery)
library(tidyverse)
library(devtools)
library(magrittr)
library(factoextra)
#library(fpc)
library(ggfortify)
library(dendextend)
library(NMF)




# Read in Data
# Cancerous attractor (MDA-MB-231)
MBA <- read.table("attractor_231.txt", row.names = 1) #Raw SFA output
MD231 <- read.table("231_attractor_discrete", row.names = 1) #Discrete

# Normal attractor (MCF10A)
MCF10A <- read.table("attractor_10A.txt", row.names = 1) #Raw SFA ouput
MCF <- read.table("10A_attractor_discrete", row.names = 1) #Discrete

#Simulated attractors
attr <- read.table("../attractor_df.txt", row.names = 1) #Raw
sim <- read.table("../attractor_df_discrete.txt", row.names = 1) #Discrete


# Manipulate Data
# Create a dataframe of all the raw values

temp <- cbind(MBA, MCF10A, attr) 
all <- temp%>% round(3) #round raw vlaues to three decimals
names <- paste("attractor", seq(1:ncol(attr)), sep = "")
names(all) <- c("attractor_231", "attractor_10A", names)

# Create a dataframe of all the discrete values

all_disc <- cbind(MD231, MCF, sim)
names(all_disc) <- names(all)





# Calculate Direction of Activity Change
# Raw value of DAC
DAC <- all

for( i in 1:ncol(all)){
  DAC[,i] <- temp[,1] - temp[,i] 
}
row.names(DAC)<- paste(row.names(DAC), "_DAC", sep = "")
DAC <- round(DAC, 3)

# Discretize DAC
disc <- function(x){
  if(x < 0){
    x <- -1
  }else if(x > 0){
    x <- 1
  } else{
    x <- 0
  }
}

DAC_disc <- apply(DAC, c(1,2), disc) %>% as.data.frame()





# Create Dataframe with combination of SFA values and DAC
both <- rbind(all, DAC)
both_disc <- rbind(all_disc, DAC_disc)



class <- c("cancerous", "normal", rep("unknown", ncol(attr)))



# Rounded Raw Values Clustering

pdf("Raw_Values.pdf")
all_T <- all %>% t() %>% as.data.frame()
write.table(all_T, "attractors.txt", quote = FALSE)
# add label for coloring
# all_T$class <- c("Cancerous_MDA-MB-231", "Normal_MCF10A", rep("unknown", 1000))

# PCA scree and biplot
pca <- prcomp(all_T, center = TRUE)
screeplot(pca)
biplot(pca)

# Hierarchical
hclust <- hclust(dist(scale(all_T)), method = "complete")
plotColoredClusters(hclust, class, c("red", "blue", rep("gray",ncol(attr))), cex = 0.8, main = "", line = 0) 

all_h_2 <- hclust %>% cutree(k = 2) %>% as.data.frame() %>% set_colnames("A_hierarchical_2")
all_h_3 <- hclust %>% cutree(k = 3) %>% as.data.frame() %>% set_colnames("A_hierarchical_3")

# Heatmap
aheatmap(all,scale = 'row',  Rowv = NA, Colv = 3L, cellwidth = 10, cellheight = 30, hclustfun = "complete",color=colorRampPalette(c('navy','white','firebrick3'))(80), filename = "raw_heatmap.pdf")

#MDS
mds1 <- cmdscale(dist(all_T),eig=TRUE, k=2) # k is the number of dim

x <- mds1$points[-c(1,2),1]
y <- mds1$points[-c(1,2),2]
ggplot(as.data.frame(mds1$points[-c(1,2),]), aes(x, y)) + geom_text( label = rownames(mds1$points[-c(1,2),]), color = "gray") + geom_text(data = mds1$points[1:2,], aes(x=mds1$points[1:2,1], y= mds1$points[1:2,2] ), label = rownames(mds1$points[c(1,2),]), color = c("red", "blue")) + xlab("Coordinate 1") + ylab("Coordinate 2") + ggtitle("Metric MDS")+ theme_bw()


# Silohouette plot
fviz_nbclust(all_T, kmeans)
fviz_nbclust(all_T, kmeans, method = "wss")

#K-means
k2_raw <- kmeans(all_T, centers = 2, nstart = 10000, iter.max = 30)
#plotcluster(all_T, k2_raw$cluster, bw = FALSE)
all_km_2 <- k2_raw$cluster %>% as.data.frame() %>% set_colnames("A_KM_2")

k3_raw <- kmeans(all_T, centers = 3, nstart = 10000, iter.max = 30)
#plotcluster(all_T, k3_raw$cluster, bw = FALSE)
all_km_3 <- k3_raw$cluster %>% as.data.frame() %>% set_colnames("A_KM_3")

dev.off()



# Discrete Values Clustering

pdf("Discrete_Values.pdf")
all_disc_T <- all_disc %>% t() %>% as.data.frame()
write.table(all_disc_T, "attractors_discrete.txt", quote = FALSE)
# add label for coloring
# all_T$class <- c("Cancerous_MDA-MB-231", "Normal_MCF10A", rep("unknown", 1000))

# PCA scree and biplot
pca <- prcomp(all_disc_T, center = TRUE)
screeplot(pca)
biplot(pca)

# Hierarchical
hclust <- hclust(dist(scale(all_disc_T)), method = "complete")
plotColoredClusters(hclust, class, c("red", "blue", rep("gray",ncol(attr))), cex = 0.8, main = "", line = 0)

all_disc_h_2 <- hclust %>% cutree(k = 2) %>% as.data.frame() %>% set_colnames("B_hierarchical_2")
all_disc_h_3 <- hclust %>% cutree(k = 3) %>% as.data.frame() %>% set_colnames("B_hierarchical_3")

# Heatmap
aheatmap(all_disc,Rowv = NA, Colv = 3L, cellwidth = 10, cellheight = 30, hclustfun = "complete",color=colorRampPalette(c('navy','white','firebrick3'))(80), filename = "disc_heatmap.pdf")

#MDS
mds1 <- cmdscale(dist(all_disc_T),eig=TRUE, k=2) # k is the number of dim

x <- mds1$points[-c(1,2),1]
y <- mds1$points[-c(1,2),2]
ggplot(as.data.frame(mds1$points[-c(1,2),]), aes(x, y)) + geom_text( label = rownames(mds1$points[-c(1,2),]), color = "gray") + geom_text(data = mds1$points[1:2,], aes(x=mds1$points[1:2,1], y= mds1$points[1:2,2] ), label = rownames(mds1$points[c(1,2),]), color = c("red", "blue")) + xlab("Coordinate 1") + ylab("Coordinate 2") + ggtitle("Metric MDS") + theme_bw()

# Silohouette plot
fviz_nbclust(all_disc_T, kmeans)
fviz_nbclust(all_disc_T, kmeans, method = "wss")

#K-means
k2_disc <- kmeans(all_disc_T, centers = 2, nstart = 10000, iter.max = 30)
#plotcluster(all_disc_T, k2_disc$cluster, bw = FALSE)

all_disc_km_2 <- k2_disc$cluster %>% as.data.frame() %>% set_colnames("B_KM_2")

k3_disc <- kmeans(all_disc_T, centers = 3, nstart = 10000, iter.max = 30)
#plotcluster(all_disc_T, k3_disc$cluster, bw = FALSE)

all_disc_km_3 <- k3_disc$cluster %>% as.data.frame() %>% set_colnames("B_KM_3")
dev.off()





# Raw DAC

pdf("Raw_DAC.pdf")
DAC_T <- DAC %>% t() %>% as.data.frame()
# add label for coloring
# all_T$class <- c("Cancerous_MDA-MB-231", "Normal_MCF10A", rep("unknown", 1000))

# PCA scree and biplot
pca <- prcomp(DAC_T, center = TRUE)
screeplot(pca)
biplot(pca)

# Hierarchical
hclust <- hclust(dist(scale(DAC_T)), method = "complete")
plotColoredClusters(hclust, class, c("red", "blue", rep("gray", ncol(attr))), cex = 0.8, main = "", line = 0) 

DAC_h_2 <- hclust %>% cutree(k = 2) %>% as.data.frame() %>% set_colnames("C_hierarchical_2")
DAC_h_3 <- hclust %>% cutree(k = 3) %>% as.data.frame() %>% set_colnames("C_hierarchical_3")

# Heatmap
aheatmap(DAC, scale = 'row',  Rowv = NA, Colv = 3L, cellwidth = 10, cellheight = 30, hclustfun = "complete",color=colorRampPalette(c('navy','white','firebrick3'))(80), filename = "DAC_heatmap.pdf")

#MDS
mds1 <- cmdscale(dist(DAC_T),eig=TRUE, k=2) # k is the number of dim

x <- mds1$points[-c(1,2),1]
y <- mds1$points[-c(1,2),2]
ggplot(as.data.frame(mds1$points[-c(1,2),]), aes(x, y)) + geom_text( label = rownames(mds1$points[-c(1,2),]), color = "gray") + geom_text(data = mds1$points[1:2,], aes(x=mds1$points[1:2,1], y= mds1$points[1:2,2] ), label = rownames(mds1$points[c(1,2),]), color = c("red", "blue")) + xlab("Coordinate 1") + ylab("Coordinate 2") + ggtitle("Metric MDS") + theme_bw()


# Silohouette plot
fviz_nbclust(DAC_T, kmeans)
fviz_nbclust(DAC_T, kmeans, method = "wss")

#K-means
k2_DAC <- kmeans(DAC_T, centers = 2, nstart = 10000, iter.max = 30)
#plotcluster(DAC_T, k2_DAC$cluster, bw = FALSE)

DAC_km_2 <- k2_DAC$cluster %>% as.data.frame() %>% set_colnames("C_km_2")

k3_DAC <- kmeans(DAC_T, centers = 3, nstart = 10000, iter.max = 30)
#plotcluster(DAC_T, k3_DAC$cluster, bw = FALSE)

DAC_km_3 <- k3_DAC$cluster%>% as.data.frame() %>% set_colnames("C_km_3")
dev.off()



# Discrete DAC

pdf("Discrete_DAC.pdf")
DAC_disc_T <- DAC_disc %>% t() %>% as.data.frame()
# add label for coloring
# all_T$class <- c("Cancerous_MDA-MB-231", "Normal_MCF10A", rep("unknown", 1000))

# PCA scree and biplot
pca <- prcomp(DAC_disc_T, center = TRUE)
screeplot(pca)
biplot(pca)

# Hierarchical
hclust <- hclust(dist(scale(DAC_disc_T)), method = "complete")
plotColoredClusters(hclust, class, c("red", "blue", rep("gray", ncol(attr))), cex = 0.8, main = "", line = 0) 

DAC_disc_h_3 <- hclust %>% cutree(k=3) %>% as.data.frame() %>% set_colnames("D_hierarchical_3")
DAC_disc_h_4 <- hclust %>% cutree(k=4) %>% as.data.frame() %>% set_colnames("D_hierarchical_4")

# Heatmap
aheatmap(DAC_disc,Colv = 3L, cellwidth = 10, cellheight = 30, hclustfun = "complete",color=colorRampPalette(c('navy','white','firebrick3'))(80), filename = "DAC_disc_heatmap.pdf")

#MDS
mds1 <- cmdscale(dist(DAC_disc_T),eig=TRUE, k=2) # k is the number of dim

x <- mds1$points[-c(1,2),1]
y <- mds1$points[-c(1,2),2]
ggplot(as.data.frame(mds1$points[-c(1,2),]), aes(x, y)) + geom_text( label = rownames(mds1$points[-c(1,2),]), color = "gray") + geom_text(data = mds1$points[1:2,], aes(x=mds1$points[1:2,1], y= mds1$points[1:2,2] ), label = rownames(mds1$points[c(1,2),]), color = c("red", "blue")) + xlab("Coordinate 1") + ylab("Coordinate 2") + ggtitle("Metric MDS") + theme_bw()

# Silohouette plot
fviz_nbclust(DAC_disc_T, kmeans)
fviz_nbclust(DAC_disc_T, kmeans, method = "wss")

#K-means
k2_DAC_disc <- kmeans(DAC_disc_T, centers = 2, nstart = 10000, iter.max = 30)
#plotcluster(DAC_disc_T, k2_DAC_disc$cluster, bw = FALSE)

k3_DAC_disc <- kmeans(DAC_disc_T, centers = 3, nstart = 10000, iter.max = 30)
#plotcluster(DAC_disc_T, k3_DAC_disc$cluster, bw = FALSE)

DAC_disc_km_2 <- k2_DAC_disc$cluster %>% as.data.frame() %>% set_colnames("D_km_2")
DAC_disc_km_3 <- k3_DAC_disc$cluster %>% as.data.frame() %>% set_colnames("D_km_3")

dev.off()


# Both

pdf("Raw_values_and_DAC.pdf")
both_T <- both %>% t() %>% as.data.frame()
# add label for coloring
# all_T$class <- c("Cancerous_MDA-MB-231", "Normal_MCF10A", rep("unknown", 1000))

# PCA scree and biplot
pca <- prcomp(both_T, center = TRUE)
screeplot(pca)
biplot(pca)

# Hierarchical
hclust <- hclust(dist(scale(both_T)), method = "complete")
plotColoredClusters(hclust, class, c("red", "blue", rep("gray", ncol(attr))), cex = 0.8, main = "", line = 0) 

both_h_2 <- hclust %>% cutree(k=2) %>% as.data.frame() %>% set_colnames("E_hierarchical_2")
both_h_3 <- hclust %>% cutree(k=3) %>% as.data.frame() %>% set_colnames("E_hierarchical_3")

# Heatmap
aheatmap(both,scale = 'row',  Rowv = NA, Colv = 3L, cellwidth = 10, cellheight = 30, hclustfun = "complete",color=colorRampPalette(c('navy','white','firebrick3'))(80), filename = "both_heatmap.pdf")

#MDS
mds1 <- cmdscale(dist(both_T),eig=TRUE, k=2) # k is the number of dim

x <- mds1$points[-c(1,2),1]
y <- mds1$points[-c(1,2),2]
ggplot(as.data.frame(mds1$points[-c(1,2),]), aes(x, y)) + geom_text( label = rownames(mds1$points[-c(1,2),]), color = "gray") + geom_text(data = mds1$points[1:2,], aes(x=mds1$points[1:2,1], y= mds1$points[1:2,2] ), label = rownames(mds1$points[c(1,2),]), color = c("red", "blue")) + xlab("Coordinate 1") + ylab("Coordinate 2") + ggtitle("Metric MDS") + theme_bw()

# Silohouette plot
fviz_nbclust(both_T, kmeans)
fviz_nbclust(both_T, kmeans, method = "wss")

#K-means
k2_both <- kmeans(both_T, centers = 2, nstart = 10000, iter.max = 30)
#plotcluster(both_T, k2_both$cluster, bw = FALSE)

both_km_2 <- k2_both$cluster %>% as.data.frame() %>% set_colnames("E_km_2")
# 
k3_both <- kmeans(both_T, centers = 3, nstart = 10000, iter.max = 30) #Quick-TRANSfer stage steps exceeded maximum (= 50100)
#plotcluster(both_T, k3_both$cluster, bw = FALSE)

both_km_3 <- k3_both$cluster %>% as.data.frame() %>% set_colnames("E_km_3")

dev.off()




# Both discrete

pdf("Values_and_DAC_Discrete.pdf")

both_disc_T <- both_disc %>% t() %>% as.data.frame()
# add label for coloring
# all_T$class <- c("Cancerous_MDA-MB-231", "Normal_MCF10A", rep("unknown", 1000))

# PCA scree and biplot
pca <- prcomp(both_disc_T, center = TRUE)
screeplot(pca)
biplot(pca)

# Hierarchical
hclust <- hclust(dist(scale(both_disc_T)), method = "complete")
plotColoredClusters(hclust, class, c("red", "blue", rep("gray", ncol(attr))), cex = 0.8, main = "", line = 0) 

both_disc_h_h28 <- hclust %>% cutree(h=28) %>% as.data.frame() %>% set_colnames("F_hierarchical_10")

# Heatmap
aheatmap(both_disc, Colv = 3L, cellwidth = 10, cellheight = 30, hclustfun = "complete",color=colorRampPalette(c('navy','white','firebrick3'))(80), filename = "both_disc_heatmap.pdf")

#MDS
mds1 <- cmdscale(dist(both_disc_T),eig=TRUE, k=2) # k is the number of dim
x <- mds1$points[-c(1,2),1]
y <- mds1$points[-c(1,2),2]
ggplot(as.data.frame(mds1$points[-c(1,2),]), aes(x, y)) + geom_text( label = rownames(mds1$points[-c(1,2),]), color = "gray") + geom_text(data = mds1$points[1:2,], aes(x=mds1$points[1:2,1], y= mds1$points[1:2,2] ), label = rownames(mds1$points[c(1,2),]), color = c("red", "blue")) + xlab("Coordinate 1") + ylab("Coordinate 2") + ggtitle("Metric MDS") + theme_bw()


# Silohouette plot
fviz_nbclust(both_disc_T, kmeans)
fviz_nbclust(both_disc_T, kmeans, method = "wss")

#K-means
k2_both_disc <- kmeans(both_disc_T, centers = 2, nstart = 10000, iter.max = 30)
#plotcluster(both_disc_T, k2_both_disc$cluster, bw = FALSE)

both_disc_km_2 <- k2_both_disc$cluster %>% as.data.frame() %>% set_colnames("F_km_2")

k3_both_disc <- kmeans(both_disc_T, centers = 3, nstart = 10000, iter.max = 30)
#plotcluster(both_disc_T, k3_both_disc$cluster, bw = FALSE)

both_disc_km_3 <- k3_both_disc$cluster %>% as.data.frame() %>% set_colnames("F_km_3")


dev.off()




# Write out results

clusters <- cbind(all_h_2, all_h_3, all_km_2, all_km_3, all_disc_h_2, all_disc_h_3, all_disc_km_2, all_disc_km_3, DAC_h_2, DAC_h_3, DAC_km_2, DAC_km_3, DAC_disc_h_3, DAC_disc_h_4, DAC_disc_km_2, DAC_disc_km_3, both_h_2, both_h_3, both_km_2, both_km_3, both_disc_h_h28, both_disc_km_2, both_disc_km_3)
write.table(clusters, "cluster_assignments.txt", quote = FALSE)

cl_raw <- cbind(all_h_2, all_h_3, all_km_2, all_km_3)
write.table(cl_raw, "cluster_Raw.txt", quote = FALSE)

cl_DAC <- cbind(DAC_h_2, DAC_h_3, DAC_km_2, DAC_km_3)
write.table(cl_DAC, "cluster_DAC.txt", quote = FALSE)

cl_both <- cbind(both_h_2, both_h_3, both_km_2, both_km_3)
write.table(cl_both, "cluster_Both.txt", quote = FALSE)

cl_disc <- cbind(all_disc_h_2, all_disc_h_3, all_disc_km_2, all_disc_km_3)
write.table(cl_disc, "cluster_Disc.txt", quote = FALSE)

cl_disc_DAC <- cbind(DAC_disc_h_3, DAC_disc_h_4, DAC_disc_km_2, DAC_disc_km_3)
write.table(cl_disc_DAC, "cluster_DAC_disc.txt", quote = FALSE)

cl_disc_both <- cbind(both_disc_h_h28, both_disc_km_2, both_disc_km_3)
write.table(cl_disc_both, "cluster_both_disc.txt", quote = FALSE)

