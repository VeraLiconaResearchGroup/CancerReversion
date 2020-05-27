# Clustering 100,000 simulated attractors

setwd("~/Clustering")
.libPaths("~/R_libs")
library(ClassDiscovery)
library(tidyverse)
library(devtools)
library(magrittr)
library(factoextra)
library(fpc)
library(ggfortify)
library(dendextend)
library(NMF)


all_T <- read.table("attractors.txt", header = TRUE, row.names = 1, sep = " ")

k3_raw <- kmeans(all_T, centers = 3, nstart = 10000, iter.max = 30)
all_km_3 <- k3_raw$cluster %>% as.data.frame() %>% set_colnames("A_KM_3")
write.table(all_km_3, "cluster_attrs_sslfc_kmeans_3.txt", quote = FALSE)

print("totss")
k3_raw$totss
print("withinss")
k3_raw$withinss
print("tot.withinss")
k3_raw$tot.withinss
print("betweenss")
k3_raw$betweenss
print("size")
k3_raw$size
print("iter")
k3_raw$iter
print("ifault")
k3_raw$ifault

print('k3done')

coordinates<-discrcoord(all_T, k3_raw$cluster)
write.table(coordinates$proj, "dc_coords_attrs_sslfc_k3.txt", quote = FALSE)
text <- c("231", "10A", rep("",100000))

pdf("attrs_sslfc_kmeans.pdf")
plotcluster(all_T, k3_raw$cluster, bw = FALSE, pch = 16)
legend("bottomleft", c("Cluster1","Cluster2", "Cluster3"),cex=.8,col=c("black","red", "green"),pch=c(16,16,16))
text(coordinates$proj[,1], coordinates$proj[,2], text, cex = 1.2, font = 2, col = "lightskyblue")
dev.off()

