setwd("~/Google Drive File Stream/My Drive/ALS_IPS/zanudo2015/classify_attractors/sfa")
# Look at orientation of 'Leukemia' SFA attractors
library(tidyverse)
library(e1071)

interest <- read.table("is_to_A_L_inBN.txt", header = TRUE, row.names = 1)
apop <- read.table('classify_attractors_newRONs/apoptosis_sfaDAC.txt')
leuk <- read.table('classify_attractors_newRONs/leukemia_sfaDAC.txt')

length(intersect(rownames(interest[interest$label == 'Apoptosis',]), apop$V1))
length(intersect(rownames(interest[interest$label == 'Leukemia1',]), leuk$V1))
length(intersect(rownames(interest[interest$label == 'Leukemia2',]), leuk$V1))

#Don't match all the RONs

ref <- read.table('is_to_A_L_inBN.txt', header = TRUE, row.names = 1)
logss <-read.table('sfa_logss.txt', header = TRUE, row.names = 1)
disc <- function(x){
  if(x > 0){
    x = 1
  }else if(x == 0){
    x= 0
  }else{
    x = -1
  }
  return(x)
}
logss_disc <- apply(logss,c(1,2),disc) 
logss_disc <- logss_disc %>% as.data.frame()

leuk1 <- logss[rownames(logss_disc) %in% rownames(ref[ref$label == 'Leukemia1',]),]
leuk2 <- logss[rownames(logss_disc) %in% rownames(ref[ref$label == 'Leukemia2',]),]
apop <- logss[rownames(logss_disc) %in% rownames(ref[ref$label == 'Apoptosis',]),]

expr_mat <- leuk1 %>%  t() %>%  as.matrix()
heatmap(expr_mat, scale = 'column')

expr_mat <- leuk2 %>%  t() %>%  as.matrix()
heatmap(expr_mat, distfun = hamming.distance, scale = 'column')

expr_mat <- rbind(leuk1, leuk2) %>%  t() %>%  as.matrix()
heatmap(expr_mat, scale = 'column')

expr_mat <- apop %>%  t() %>%  as.matrix()
heatmap(expr_mat, scale = 'column')

sink(file = 'table_of_rons.txt', type= 'output')
for(name in names(leuk1)){
  print(name)
  print(table(leuk1[,name]))
  print(table(leuk2[,name]))
  print(table(apop[,name]))
}
sink(file = NULL)

library(readxl)
library(NMF)
library(readr)

expr <- logss_disc[rownames(logss_disc) %in% rownames(ref),]
expr_mat <- expr %>%  t() %>%  as.matrix()
heatmap(expr_mat, scale = 'column')
aheatmap(expr_mat, hclustfun = "complete",cellwidth= 80, Rowv = NA, color=colorRampPalette(c('navy','white','firebrick3'))(80),filename="test_expr_attrs.png")

expr2 <- logss[rownames(logss_disc) %in% rownames(ref),]
expr_mat2 <- expr2 %>%  t() %>%  as.matrix()
heatmap(expr_mat2, scale = 'column')




