setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) #set wd to wherever script is located
library(tidyverse)
library(NMF)


data <- read.csv('sfa_A_L.csv', header = T, row.names = 1)
names(data)[c(1,2)] <- c("L1", "L2")
map <- read.table('is_bn_map.txt', header = T, row.names = 1)
data <- read.table('classify_attractors/sfa/sfa_logss.txt', header = T, row.names = 1)

data2 <- data[map$phenotype != 'Other',]
vec <- rownames(map)[map$phenotype != 'Other']
vec <- paste(vec, 1:length(vec), sep = "_")


RONs <- c('apoptosis', 'ceramide', 'bid', 'disc', 'fas', 'iap', 's1p')
data3 <- data2[names(data) %in% RONs,]
data3 <- data3 %>% t() %>% as.matrix()
# data3 <- data3 %>% as.matrix

data2 <- data %>% as.matrix


aheatmap(data3, hclustfun = "complete", cellwidth= 60,  color=colorRampPalette(c('navy','white','firebrick3'))(80),filename="sfa_A_L_expression_RONs.png", scale = 'column')

png('sfa_expression_heatmap.png')
a <-aheatmap(data2,hclustfun = "complete", cellwidth= 60,  color=colorRampPalette(c('navy','white','firebrick3'))(80), filename="sfa_A_L_expression_norowscale.png", scale = 'column')
heatmap(data3,  cexCol = .8, scale = 'col', cexRow= .2)
dev.off()

data <- read.table('boolnet_A_L_attractors.txt', header = T, row.names = 1, stringsAsFactors = F)
data$names <- rownames(data)
data <- data %>% filter(A1 != 's')
rownames(data) <- data$names
data[,-ncol(data)] <- data[,-ncol(data)] %>% apply(2, as.numeric)
data <- data[,-ncol(data)]
data2 <- data  %>%  as.matrix
a <- aheatmap(data2, hclustfun = "complete", cellwidth= 60,  color=colorRampPalette(c('navy','white','firebrick3'))(80),filename="boolean_A_L_attractors_noscale.png")

datas <- read.csv('sfa_A_L.csv', header = T, row.names = 1)
names(datas)[c(1,2)] <- c("L1", "L2")
data2 <- datas  %>%  as.matrix

ord <- c(rownames(datas)[!rownames(datas) %in% rownames(data)], rownames(data)[a$rowInd])
ord2 <- c()
for(elem in ord) ord2 <- c(ord2, which(rownames(datas) == elem))

disc <- function(x){
  if(x > 0) x<-1
  else if(x < 0 ) x <- -1
  return(x)
}

data2 <- data2 %>% apply(c(1,2), disc)

aheatmap(data2, revC = F, Rowv = ord2, hclustfun = "complete", cellwidth= 60,  color=colorRampPalette(c('navy','white','firebrick3'))(80), filename="sfa_A_L_expression_.png")






