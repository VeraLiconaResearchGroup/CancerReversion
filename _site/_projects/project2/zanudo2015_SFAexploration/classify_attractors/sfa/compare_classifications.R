setwd("/Volumes/GoogleDrive/My Drive/ALS_IPS/zanudo2015/classify_attractors")
library(tidyverse)

DACL <- scan('leukemia_sfaDAC.txt', what = character())
kmeansL <- scan('kmeans_ss_11_leukemia', what = character())

DACA <- scan('apoptosis_sfaDAC.txt', what = character())
kmeansA <- scan('kmeans_ss_11_apoptosis', what = character())

length(intersect(DACL, kmeansL))/length(DACL)*100
length(intersect(DACA, kmeansA))/length(DACA)*100


# files
sDACL <- 'sfa/classifications/leukemia_sfaDAC.txt'
sKSSL <- 'sfa/classifications/leukemia_sfa_kmeansSS_10.txt'
sKBL <- 'sfa/classifications/leukemia_sfa_kmeansBoth_12.txt'

sDACA <- 'sfa/classifications/apoptosis_sfaDAC.txt'
sKSSA <- 'sfa/classifications/apoptosis_sfa_kmeansSS_10.txt'
sKBA <- 'sfa/classifications/apoptosis_sfa_kmeansBoth_12.txt'

bDACL <- 'boolnet/leukemia_boolDAC.txt'
bKSSL <- 'boolnet/leukemia_bool_kmeansAttr_10.txt'
bKDACL <- 'boolnet/leukemia_bool_kmeansDAC_11.txt'
bKBL <- 'boolnet/leukemia_bool_kmeansBoth_13.txt'

bDACA <- 'boolnet/apoptosis_boolDAC.txt'
bKSSA <- 'boolnet/apoptosis_bool_kmeansAttr_10.txt'
bKDACA <- 'boolnet/apoptosis_bool_kmeansDAC_11.txt'
bKBA <- 'boolnet/apoptosis_bool_kmeansBoth_13.txt'

comp <- function(ds1, ds2){
  ds1 <- read.table(ds1, header = FALSE)
  ds2 <- read.table(ds2, header = FALSE)
  h <- nrow(ds1)
  i <- nrow(ds2)
  j <- length(intersect(ds1$V1, ds2$V1))
  o <- round(j/h*100,2)
  l <- round(j/i*100,2)
  jl <- intersect(ds1$V1, ds2$V1)
  return(c(h,i,j,o,l,jl))
}

dataframe <- data.frame(row.names = c('sfa_DAC_L vs sfa_kmeansSS_L','sfa_DAC_L vs sfa_kmeansB_L','sfa_DAC_A vs sfa_kmeansSS_A', 'sfa_DAC_A vs sfa_kmeansB_A'))
dataframe2 <- data.frame(row.names = c('boolnet_DAC_L vs boolnet_kmeansSS_L', 'boolnet_DAC_L vs boolnet_kmeansDAC_L', 'boolnet_DAC_L vs boolnet_kmeansB_L',
                                       'boolnet_DAC_A vs boolnet_kmeansSS_A', 'boolnet_DAC_A vs boolnet_kmeansDAC_A', 'boolnet_DAC_A vs boolnet_kmeansB_A'))
dataframe3 <- data.frame(row.names = c('sfa_kmeansSS_L vs sfa_kmeansB_L', 'sfa_kmeansSS_A vs sfa_kmeansB_A'))
dataframe4 <- data.frame(row.names = c('boolnet_kmeansSS_L vs boolnet_kmeansDAC_L', 'boolnet_kmeansSS_L vs boolnet_kmeansB_L', 'boolnet_kmeansDAC_L vs boolnet_kmeansB_L', 
                                       'boolnet_kmeansSS_A vs boolnet_kmeansDAC_A', 'boolnet_kmeansSS_A vs boolnet_kmeansB_A', 'boolnet_kmeansDAC_A vs boolnet_kmeansB_A'))

# SFA DAC vs all sfa clusters
v1 <- comp(sDACL, sKSSL)
v2 <- comp(sDACL, sKBL)

v3 <- comp(sDACA, sKSSA)
v4 <- comp(sDACA, sKBA)

dataframe$l1 <-c(v1[1], v2[1], v3[1], v4[1])
dataframe$l2 <-c(v1[2], v2[2], v3[2], v4[2])
dataframe$intersection <- c(v1[3], v2[3], v3[3], v4[3])
dataframe$percent_l1_intersection <- c(v1[4], v2[4], v3[4], v4[4])
dataframe$percent_l2_intersection <- c(v1[5], v2[5], v3[5], v4[5])

# Boolean DAC vs all boolean clusters
v1 <- comp(bDACL, bKSSL)
v2 <- comp(bDACL, bKDACL)
v3 <- comp(bDACL, bKBL)

v4 <- comp(bDACA, bKSSA)
v5 <- comp(bDACA, bKDACA)
v6 <- comp(bDACA, bKBA)

dataframe2$l1 <- c(v1[1], v2[1], v3[1], v4[1], v5[1], v6[1])
dataframe2$l2 <- c(v1[2], v2[2], v3[2], v4[2], v5[2], v6[2])
dataframe2$intersection <- c(v1[3], v2[3], v3[3], v4[3], v5[3], v6[3])
dataframe2$percent_l1_intersection <- c(v1[4], v2[4], v3[4], v4[4], v5[4], v6[4])
dataframe2$percent_l2_intersection <- c(v1[5], v2[5], v3[5], v4[5], v5[5], v6[5])

# SFA clusters against eachother
v1 <- comp(sKSSL, sKBL)
v2 <- comp(sKSSA, sKBA)

dataframe3$l1 <- c(v1[1], v2[1])
dataframe3$l2 <- c(v1[2], v2[2])
dataframe3$intersection <- c(v1[3], v2[3])
dataframe3$percent_l1_intersection <- c(v1[4], v2[4])
dataframe3$percent_l2_intersection <- c(v1[5], v2[5])

# Boolean clusters against eachother
v1 <- comp(bKSSL, bKDACL)
v2 <- comp(bKSSL, bKBL)
v3 <- comp(bKDACL, bKBL)

v4 <- comp(bKSSA, bKDACA)
v5 <- comp(bKSSA, bKBA)
v6 <- comp(bKDACA, bKBA)

dataframe4$l1 <- c(v1[1], v2[1], v3[1], v4[1], v5[1], v6[1])
dataframe4$l2 <- c(v1[2], v2[2], v3[2], v4[2], v5[2], v6[2])
dataframe4$intersection <- c(v1[3], v2[3], v3[3], v4[3], v5[3], v6[3])
dataframe4$percent_l1_intersection <- c(v1[4], v2[4], v3[4], v4[4], v5[4], v6[4])
dataframe4$percent_l2_intersection <- c(v1[5], v2[5], v3[5], v4[5], v5[5], v6[5])

# SFA DAC vs Boolean DAC

# convert boolean attractors into initial states
ref <- read.table('is_to_attr_2.txt', header = TRUE)
comp_sfa_bn  <- function(ds1, ds2){
  ds1 <- read.table(ds1, header = FALSE)
  df <- read.table(ds2, header = FALSE)
  is <- ref[paste('attr_',ref$Attr, sep = '') %in% df$V1, 'initial_state']
  h <- nrow(ds1)
  i <- length(is)
  j <- length(intersect(ds1$V1, is))
  o <- round(j/h*100,2)
  l <- round(j/i*100,2)
  jl <- intersect(ds1$V1, is)
  return(c(h,i,j,o,l,jl))
}

v1 <- comp_sfa_bn(sDACL, bDACL)
v2 <- comp_sfa_bn(sDACA, bDACA)
dataframe5 <- data.frame(row.names = c('sfa_DAC_L vs bn_DAC_L', 'sfa_DAC_A vs bn_DAC_A'))

dataframe5$l1 <- c(v1[1], v2[1])
dataframe5$l2 <- c(v1[2], v2[2])
dataframe5$intersection <- c(v1[3], v2[3])
dataframe5$percent_l1_intersection <- c(v1[4], v2[4])
dataframe5$percent_l2_intersection <- c(v1[5], v2[5])


df_all <- rbind(dataframe,  dataframe2, dataframe3, dataframe4, dataframe5)
write.table(df_all, 'classification_comparisons.txt', quote = FALSE, row.names = TRUE)


########

data <- read.table('sfa/sfa_logss.txt', header = TRUE, row.names = 1)
key <- read.table('sfa/is_to_A_L_inBN.txt', header = TRUE, row.names = 1)

apop <- row.names(key)[key$label == 'Apoptosis']
leuk1 <- row.names(key)[key$label == 'Leukemia1']
leuk2 <- row.names(key)[key$label == 'Leukemia2']

apoptosis <- data[row.names(data) %in% apop,]
leukemia1 <- data[row.names(data) %in% leuk1,]
leukemia2 <- data[row.names(data) %in% leuk2,]

DACL <- read.table(sDACL, header = FALSE)
DACA <- read.table(sDACA, header = FALSE)

length(intersect(apop, DACA$V1))
length(intersect(leuk1, DACL$V1))
length(intersect(leuk2, DACL$V1))


