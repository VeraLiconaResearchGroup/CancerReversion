#
setwd("/Volumes/GoogleDrive/My Drive/ALS_IPS/zanudo2015/sfa_fixednodes/DAC")
library(tidyverse)

DAC <- read.table("DAC_A_L1_rons.txt", header = TRUE)
DAC <- DAC[,-c(1,2)]

RON_0 <- c('fasl','fast', 'gzmb', 'ifngt', 'nfkb', 'pi3k', 'tpl2', 'tradd')

df <- DAC[,RON_0]

pdf('RON0_dist_L1.pdf')
for(name in names(df)){
  t <- table(df[,name])
  lab <- as.character(round(t/sum(t)*100,2))
  labs <- c(lab[1], '0', '0', lab[2]) 
  if(length(t) == 1) labs <- lab[1] 
  labs <- paste(labs, "%")
  print(labs)
  hist(df[,name], main = name, labels = labs, breaks = 3, xlab = 'DAC')
}
dev.off()



# Compare DAC of attractors resulting from fixed nodes to see how many are unique

L1 <- read.table("DAC_A_L1_all.txt", header = TRUE)
L1 <- L1[,-c(1,2)]
L1_unique <- distinct(L1)
#Number of replicates:
dim(L1)[1] - dim(L1_unique)[1]
#percent of replicates:
(dim(L1)[1] - dim(L1_unique)[1])/dim(L1)[1]*100

L2 <- read.table("DAC_A_L2_all.txt", header = TRUE)
L2 <- L2[,-c(1,2)]
L2_unique <- distinct(L2)
#Number of replicates:
dim(L2)[1] - dim(L2_unique)[1]
#percent of replicates:
(dim(L2)[1] - dim(L2_unique)[1])/dim(L2)[1]*100


# Compare DAC of attractors resulting from fixed nodes to see how many are unique

L1 <- read.table("../../DAC_results_L1A/DAC_all.txt", header = TRUE)
L1 <- L1[,-c(1,2)]
L1_unique <- distinct(L1)
#Number of replicates:
dim(L1)[1] - dim(L1_unique)[1]
#percent of replicates:
(dim(L1)[1] - dim(L1_unique)[1])/dim(L1)[1]*100

L2 <- read.table("../../DAC_results_L2A/DAC_all.txt", header = TRUE)
L2 <- L2[,-c(1,2)]
L2_unique <- distinct(L2)
#Number of replicates:
dim(L2)[1] - dim(L2_unique)[1]
#percent of replicates:
(dim(L2)[1] - dim(L2_unique)[1])/dim(L2)[1]*100
