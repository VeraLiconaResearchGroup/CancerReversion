# Find Configurartions of Perturbations that cause normal attractors

setwd("~/Documents/GitHub/gastonguay_compsysmed_labnotebook/_projects/project2/NetworkAnalysis/insilico_perturbations")
library(tidyverse)
library(mlxR)

# Read in Data

FC <- "FC2"
normal <- readLines("Normal_perturb_FC2_int_156.txt")
basal <- read.table(paste(FC, "_231_basal", sep = ""), header = FALSE, row.names=  1) %>% t() %>% as.data.frame()
# Strong perturbations because of DAC and sign flip
strong <- read.table(paste("strong_perturbations_",FC,".txt", sep= ""), header = TRUE, sep = '\t', colClasses = c("character"))
strong <- strong$Perturbation.Number

ns <- c()
for(perturb in normal){
  # print(perturb)
  n <- unlist(strsplit(perturb, "_"))[2]
  ns <- c(ns, n)
}

# If you want strong perturbations, uncomment this and change name of df below
ns <- intersect(ns, strong)

# Make a dataframe of all FC initial conditions resulting in normal attractors
FCic <- as.data.frame(matrix(nrow = length(ns), ncol = ncol(basal)))
row.names(FCic) <- paste("Perturb", ns, sep = "_")
names(FCic) <- names(basal)

for(n in ns){
  df <- read.table(paste("FCbasal_perturbation/FC_perturbation_", n, ".txt", sep = ""), header = FALSE) %>% t() %>% as.data.frame()
  FCic[paste("Perturb_", n, sep = ""),] <- df[1,] 
}

# Find which were actually perturbed
pert <- FCic
for(n in 1:nrow(FCic)){
  z <- 0
  for( i in 1:ncol(FCic)){
    # print(FCic[n,i])
    if(FCic[n,i] == basal[1,i]){
      pert[n,i] <- "N"
      z <- z + 1
    }else if(FCic[n,i] == 1){
      pert[n, i] <- "activated"
    }else if(FCic[n,i] == 0){
      pert[n, i] <- "zero"
    }else if(FCic[n,i] == -1){
      pert[n, i] <- "inhibited"
    }
  pert$Npert[n] <- ncol(FCic)-z
  }
}

pert2 <- pert[order(pert$Npert, decreasing = FALSE),]
pert2["Percent activated",] <- rep(0, ncol(pert2))
pert2["Percent inhibited",] <- rep(0, ncol(pert2))
pert2["Percent zero",] <- rep(0, ncol(pert2))
pert2["Percent N",] <- rep(0, ncol(pert2))

for(n in 1:(ncol(pert2)-1)){
  a <- table(pert2[,n])
  for(i in 2:length(names(a))){
    pert2[paste("Percent", names(a)[i]),n] <- round(a[names(a) == names(a)[i]]/(nrow(pert2)-4)*100, 2)
  }
}

pert2$Npert[(nrow(pert2)-3):nrow(pert2)] <- NA

basal$Npert <- NA
row.names(basal) <- "basal"
pert2 <- rbind(pert2, basal)

write.table(pert2, paste("Normal_STRONG_perturbations_", FC, "_orientation.txt", sep = ""), quote = FALSE)


