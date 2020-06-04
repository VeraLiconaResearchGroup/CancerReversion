setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) #set wd to wherever script is located
library(MASS)
library(tidyverse)
library(e1071)
library(plotly)


scree.plot = function(d, k) {
  stresses=sammon(d, k=k)$stress
  for(i in rev(seq(k-1)))  
    stresses=append(stresses,sammon(d, k=i)$stress)
  plot(seq(k),rev(stresses), type="b", xaxp=c(1,k, k-1), ylab="Stress", xlab="Number of dimensions")
}


# Read in boolean attractors that are classified as leukemia and apoptosis based off of readout nodes
exprl <- read.table('../classify_attractors/boolnet/leukemia_boolnet.txt', stringsAsFactors = F)
expra <- read.table('../classify_attractors/boolnet/apoptosis_boolnet.txt', stringsAsFactors = F)

# Add attractor numbers for leukemia1, leukemia2, and apoptosis
exprl[nrow(exprl)+1,"V1"] <- 'attr_507'
exprl[nrow(exprl)+1,] <- 'attr_284'
expra[nrow(expra)+1,] <- 'attr_195'

# data <- read.table('boolnet_attractors_noX.txt', header = TRUE, row.names = 1)
# data <- data[-c(1,2),]
# data <- data %>% as.matrix()
# ham <- hamming.distance(data)

# Read in datasets
dataa <- read.table('../boolnet_attractors.txt', header = TRUE, row.names = 1) #attractors
datad <- read.csv('../boolnet_DAC.csv', header = TRUE, row.names = 1) #DAC
datad <- datad[-c(1,2),]
datad[is.na(datad)] <- "X"
datab <- cbind(dataa,datad) #Both

# Set dataset of interest to data:
data <- datab

# Create vector with phenotypes
other <- rownames(data)
data_sub <- data[rownames(data) %in% exprl$V1 | rownames(data) %in% expra$V1,]
dup <- duplicated(data_sub)
data_sub$names <- rownames(data_sub)
data_sub2 <- data_sub[!dup,]
intattr_names <- data_sub2$names
data_sub2 <- data_sub2[,-ncol(data_sub2)]
data2 <- rbind(data_sub2, data[!rownames(data) %in% rownames(data_sub),]) 
rnames <- rownames(data2)[!duplicated(data2)]
data2 <- data2 %>% distinct() %>%  as.matrix()


phen <- rep('Apoptosis', nrow(data_sub2))
phen[intattr_names %in% exprl$V1] <- 'Leukemia'

# Associate the removed duplicates back
dupli <- data[duplicated(data),]
ndupli <- data[!duplicated(data),]
association <- data.frame(row.names = rownames(dupli))
for(row in rownames(dupli)){
  association[row,"match"] <- rownames(ndupli)[row.match(dupli[row,], ndupli)]
}
association$phenotype <- rep("other", nrow(association))
association$phenotype[rownames(association) %in% exprl$V1] <- "Leukemia"
association$phenotype[rownames(association) %in% expra$V1] <- "Apoptosis"

pdf('mds_explore.pdf')

# Hamming Distance
ham <- hamming.distance(data2)
data2[which(data2 == "X")] <- sample(c(0,1), size = 1)
data2<- data2 %>% as.numeric %>%  distinct()
ham <- stats::dist(data2, "minimum")
#error with canberra and euclidean
scree.plot(ham,10)

# Sammon MDS with 2 dimensions
mds3 <- ham %>% sammon(k = 2)
mds3$stress

plotdf <- mds3$points %>% as.data.frame()
rownames(plotdf) <- rnames

names(plotdf) <- c("X", "Y")
plotdf$phenotype <- c(phen, rep("other", nrow(plot)-length(intattr_names)))
plotdf[rownames(association),] <- plotdf[association$match,]


print(ggplot(plotdf, aes(X,Y,color = phenotype)) + geom_point(alpha = 1) + 
  geom_text(data = plotdf[which(intattr_names %in% c("attr_195", "attr_507", "attr_284")),], label = c("Apoptosis", "Leukemia", "Leukemia"), show.legend = F) +
  theme_bw() + 
  theme(panel.border = element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), 
        axis.line = element_line(colour = "black")))

dev.off()
