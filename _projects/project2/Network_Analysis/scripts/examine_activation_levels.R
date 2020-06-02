#--------------------------------------------------
# examine_activation_levels.R is a script that generates figures illustrating how the proposed activity level for knock-in perturbations 
# compares to the expression distribution of the rest of the network nodes. It also pulls the fold change and p-value for FVS nodes.
#
# INPUTS:
# 1. Normalized Expression Data of Network Nodes
# 2. Activity level of FVS nodes when knock-in simulateed as 2*mean
# 3. Activity level of FVS nodes when knock-in simulateed as 1.5*mean
# 4. Activity level of FVS nodes when knock-in simulateed as meean + 3*sd
# 5. A list of FVS nodes
# 6. data2.csv: the file containng results from DESeq2 analyses
#
# OUTPUTS:
# 1. Figures illustrating the distribution of expression values
# 2. A table with log fold change and adjusted p-value for each FVS node
#--------------------------------------------------

setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) #set wd to wherever script folder is located
setwd("..") #cahange working directory to Network_Analysis Folder

library(reshape)
library(tidyverse)

theme <- theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
               panel.background = element_blank(), axis.line = element_line(colour = "black"))

# Read in normalized expression data of network nodes
nodes <- read.table("inputfiles/network_nodes_normalized_expression_replicates.txt", header = T, row.names = 1)
nodes2 <- melt(nodes)

# Visualize distribution of activity levels with histogram and boxplot
ggplot(data = nodes2, aes(value)) + geom_histogram(binwidth = .5, fill = 'white', color = 'black') +
  ggtitle("Distribution of Normalized Expression Data for MDA-MB-231 and MCF10A") +
  labs(x= 'Normalized Expression') + theme

boxplot(nodes2$value)

# Summary stats of expression values for network nodes
summary(nodes2$value)

#Read in pre-generated activity levels for each FVS node (Use 4b_calculate_activation.py)
perts2 <- read.table("perturbation_level_factor2.txt", header = T, row.names = 1) #Knock-in = 2*mean
perts1.5 <- read.table("perturbation_level_factor1.5.txt", header = T, row.names = 1) #Knock-in = 1.5*mean
perts <- read.table("perturbation_level_sd.txt", header = T, row.names = 1) #Knock-in = mean + 3*sd

pdf('images/compare_stimulation_values.pdf') #Safe images to pdf file

#Boxplot of normalized expression data with knock-in values of mean + 3*sd overlayed 
boxplot(nodes2$value, ylab= 'Normalized Expression Value')
points(rep(1, nrow(perts)), perts$Mean...3SD, col = 'red', pch = 4)
title('Distribution of Expression Values With Stimulations Set as Mean + 3*SD')
legend('topright', c("Experimental Expression Value", "Stimualtion Expression Value"), col = c("black", "red"), pch = c(1, 4))

#Boxplot of normalized expression data with knock-in values of 1.5*mean overlayed 
boxplot(nodes2$value, ylab= 'Normalized Expression Value')
points(rep(1, nrow(perts1.5)), perts1.5$X1.5.Mean, col = 'red', pch = 4)
title('Distribution of Expression Values With Stimulations Set as 1.5*Mean')
legend('topright', c("Experimental Expression Value", "Stimualtion Expression Value"), col = c("black", "red"), pch = c(1, 4))

#Boxplot of normalized expression data with knock-in values of 2*mean overlayed 
boxplot(nodes2$value, ylim = c(0, max(perts2$X2Mean)+.01) , ylab = 'Normalized Expression Value')
points(rep(1, nrow(perts2)), perts2$X2.Mean, col = 'red', pch = 4)
title('Distribution of Expression Values With Stimulations Set as 2*Mean')
legend('topright', c("Experimental Expression Value", "Stimualtion Expression Value"), col = c("black", "red"), pch = c(1, 4))

#Histogram of normalized expression data with knock-in values of mean + 3*sd overlayed 
ggplot(data = nodes2, aes(value)) + geom_histogram(binwidth = .5, fill = 'white', color = 'black') +
  ggtitle("Distribution of Normalized Expression Data for MDA-MB-231 and MCF10A \n with Stimulations as Mean + 3*SD") +
  labs(x= 'Normalized Expression') + theme + geom_point(data = data.frame(x = perts$Mean...3SD, y = rep(0, nrow(perts))), aes(x,y), color = 'red', pch = 4, cex = 3) 

#Histogram of normalized expression data with knock-in values of 1.5*mean overlayed 
ggplot(data = nodes2, aes(value)) + geom_histogram(binwidth = .5, fill = 'white', color = 'black') +
  ggtitle("Distribution of Normalized Expression Data for MDA-MB-231 and MCF10A \n with Stimulations as 1.5*Mean") +
  labs(x= 'Normalized Expression') + theme + geom_point(data = data.frame(x = perts1.5$X1.5.Mean, y = rep(0, nrow(perts1.5))), aes(x,y), color = 'red', pch = 4, cex = 3) 

#Histogram of normalized expression data with knock-in values of 2*mean overlayed 
ggplot(data = nodes2, aes(value)) + geom_histogram(binwidth = .5, fill = 'white', color = 'black') +
  ggtitle("Distribution of Normalized Expression Data for MDA-MB-231 and MCF10A \n with Stimulations as 2*Mean") +
  labs(x= 'Normalized Expression') + theme + geom_point(data = data.frame(x = perts2$X2.Mean, y = rep(0, nrow(perts2))), aes(x,y) , color = 'red', pch = 4, cex = 3) 

dev.off()


## Explore log2 fold change a adjusted p-value of FVS nodes
FVS <- scan("inputfiles/FVS_12", what = "character", skip = 1) #Read in FVS nodes

df <- read.csv("../Network_Components/FunDEGs/data2.csv", header = T, row.names = 1) #Read in results from DESeq2 Analysis
df2 <- df %>% filter(Gene_Symbol %in% FVS)
df3 <- df2[,c("Gene_Symbol", "MDA_MB.231.MCF10A.fc" ,"MDA_MB.231.MCF10A.bh.pval")]
write.table(df3, "FVS_fc_pval.txt", quote = F, row.names = F)



