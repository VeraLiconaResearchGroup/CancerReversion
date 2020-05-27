#----------------------------------------------------------
# sfa_heatmaps.R creates heatmaps of SFA attractors and experimental data
#
# INPUTS:
# 1. Normalized RNAseq Expression Data from Experimental Replicates
# 2. Attractors Estimated from Expeerimental Replicates
#
# OUTPUTS:
# 1. Heatmaps
#----------------------------------------------------------

setwd("~/Documents/GitHub/gastonguay_compsysmed_labnotebook/_projects/project2/Network_Analysis")
library(tidyverse)
library(NMF)


# Read in normalized RNAseq experssion data from experimental replicates
d <- read.table('inputfiles/network_nodes_normalized_expression_replicates.txt', header = T, row.names = 1)

# Read in attractors estimated from experimental conditions with SFA and orient to have nodes as rows and attractors as columns
data <- read.table('inputfiles/ref_attrs_logss.txt', header = T, row.names = 1) %>% t() %>% as.data.frame()

#Subset both dataframes so they only contain nodes in both datasets
d <- d[rownames(d) %in% rownames(data), ]
data <- data[rownames(data) %in% rownames(d), ]


#Order both dataframes in alphabetical order by node name
data$name <- rownames(data)
data <- data %>% arrange(name)
rownames(data) <- data$name
data <- data %>% select(-'name')

d$name <- rownames(d)
d <- d %>% arrange(name)
rownames(d) <- d$name
d <- d %>% select(-'name')

#Generate heatmap of normalized RNAseq expression data from experimental replicates
p <- aheatmap(d, hclustfun = "complete", cellwidth= 60,  color=colorRampPalette(c('navy','white','firebrick3'))(80), 
              filename = 'RNAseq_expression.png', scale = "column", Rowv = F)

order = p$rowInd #Save order of nodes in the heatmap of experimental data 

#Generate heatmap of SFA attractors estimated from experimental replicates in the same order as heatmaps of experimental data
p2 <- aheatmap(data, hclustfun = "complete", cellwidth= 60,  color=colorRampPalette(c('navy','white','firebrick3'))(80), 
               filename = 'sfa_experimental_attrs_test.png', Rowv = order, revC = FALSE, scale = 'column')


