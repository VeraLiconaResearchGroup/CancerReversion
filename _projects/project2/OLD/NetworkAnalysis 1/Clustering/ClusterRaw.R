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
# sim <- read.table("../attractor_df_discrete.txt", row.names = 1) #Discrete


# Manipulate Data
# Create a dataframe of all the raw values

temp <- cbind(MBA, MCF10A, attr) 
all <- temp%>% round(3) #round raw vlaues to three decimals
names <- paste("attractor", seq(1:ncol(attr)), sep = "")
names(all) <- c("attractor_231", "attractor_10A", names)

# Create a dataframe of all the discrete values

# all_disc <- cbind(MD231, MCF, sim)
# names(all_disc) <- names(all)





# Calculate Direction of Activity Change
# Raw value of DAC
# DAC <- all

# for( i in 1:ncol(all)){
#   DAC[,i] <- temp[,1] - temp[,i] 
# }
# row.names(DAC)<- paste(row.names(DAC), "_DAC", sep = "")
# DAC <- round(DAC, 3)
# 
# # Discretize DAC
# disc <- function(x){
#   if(x < 0){
#     x <- -1
#   }else if(x > 0){
#     x <- 1
#   } else{
#     x <- 0
#   }
# }
# 
# DAC_disc <- apply(DAC, c(1,2), disc) %>% as.data.frame()





# Create Dataframe with combination of SFA values and DAC
# both <- rbind(all, DAC)
# both_disc <- rbind(all_disc, DAC_disc)



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

