# PCA
setwd("/Volumes/GoogleDrive/My Drive/ALS_IPS/zanudo2015/Clustering_test")
library(MASS)
library(tidyverse)
# library(e1071)
# library(plotly)
library(factoextra)
theme_set(theme_bw(base_size=12) + theme(panel.grid = element_blank()))

attrsss <- read.table('boolnet_attractors_noX.txt', header = TRUE, row.names = 1, na.strings = "X")
attrsss <- attrsss[-c(1,2),]
attrsDAC <- read.table('boolnet_DAC_noX.txt', header = TRUE, row.names = 1, na.strings = "X")
attrsDAC <- attrsDAC[-c(1,2),]
attr <- cbind(attrsss,attrsDAC)
map <- read.table('../is_attrs_bn.txt', header = T, row.names = 1)

lbool <- read.table("../classify_attractors/boolnet/classify_attractors_newRONs/leukemia_boolnet.txt", header = F, stringsAsFactors = F)
lbool[nrow(lbool)+1,] <- "attr_284"
lbool[nrow(lbool)+1,] <- "attr_507"
abool <- read.table("../classify_attractors/boolnet/classify_attractors_newRONs/apoptosis_boolnet.txt", header = F, stringsAsFactors = F)
abool[nrow(abool)+1,] <- "attr_195"

map$bn <- paste("attr_", map[,1], sep = "")
map$phenotyrpe <- ifelse(map$bn %in% lbool$V1, "Leukemia", ifelse(map$bn %in% abool$V1, "Apoptosis", "Other"))
map$phenotype <- as.factor(map$phenotype)
map$phenotype2 <- ifelse(map$bn == 'attr_195', "Apoptosis", ifelse(map$bn == 'attr_284' | map$bn == 'attr_507' , "Leukemia", "Other"))

pca <- prcomp(attrsDAC, center = TRUE)
fviz_screeplot(pca)

pcdf <- pca$x %>% as.data.frame()
pcdf$phenotype <- as.factor(ifelse(rownames(pcdf) %in% abool$V1, "Apoptosis", ifelse(rownames(pcdf) %in% lbool$V1, "Leukemia", "Other")))
ggplot(pcdf, aes(PC1, PC2, color = phenotype)) + geom_point()

km <- kmeans(pcdf[,c(1,2)], 7, nstart = 10000)
ggplot() + geom_point(data = pcdf, aes(PC1, PC2, color = as.factor(km$cluster))) + geom_text(data = pcdf[rownames(pcdf) %in% c('attr_195', 'attr_284', 'attr_507'), ], aes(x = PC1, y = PC2), label = c('Apoptosis', 'Leukemia', "Leukemia"))
length(which(km$cluster == 5))

ggplot(pcdf, aes(PC1,PC2)) + geom_point( aes(shape = phenotype, color =  as.factor(km$cluster)),  cex = 2) +
  geom_text(data = pcdf[rownames(pcdf) %in% c("attr_195", "attr_507", "attr_284"),], aes(PC1, PC2), label = c('Apoptosis', "Leukemia", "Leukemia"), show.legend = F) +
  theme(panel.background = element_blank())

# SFA results
df <- read.table('../classify_attractors/sfa/sfa_logss_disc.txt', header = T, row.names = 1)
pca <- prcomp(df, center = TRUE)
fviz_screeplot(pca)
pcdf <- pca$x %>% as.data.frame()
ggplot(pcdf, aes(PC1, PC2)) + geom_point()






