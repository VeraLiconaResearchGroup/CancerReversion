library(tidyverse)
library(BoolNet)
# setwd("C:/Users/marazzi/Dropbox/Marazzi/Control_DynamicalSystems/Fall_2019/zanudo2015")
setwd("/Volumes/GoogleDrive/My Drive/ALS_IPS/zanudo2015")
network <- loadNetwork("zanudo_boolean.bn")


trmt <- list('A' = "sphk1", "B" = "pdgfr", "C" = c("tbet", "ceramide", "ras"), 
             "D" = c("tbet", "ceramide", "grb2"), "E" = c("tbet", "ceramide", "il2rb"), 
             "F"= c("tbet", "ceramide", "il2rbt"), "G" = c("tbet", "ceramide", "erk"))

df <- data.frame(nodes = c( "a20","apoptosis","bclxl","bid","caspase","ceramide","creb","ctla4","cytoskeletonsignaling","disc","erk","fas",
                            "fasl","fast","flip","fyn","gap","gpcr","grb2","gzmb","iap","ifng","ifngt","il2","il2ra","il2rat","il2rb","il2rbt",
                            "jak","lck","mcl1","mek","nfat","nfkb","p2","p27","pdgfr","pi3k","plcg1","proliferation","rantes","ras","s1p","sfas",
                            "smad","socs","sphk1","stat3","tbet","tcr","tnf","tpl2","tradd","zap70","il15","stimuli","cd45","stimuli2","pdgf","tax"),
                 replicate(2,sample(0:1,60,rep=TRUE)) , replicate(2,sample(0:1,60,rep=TRUE)), replicate(2,sample(0:1,60,rep=TRUE)), replicate(2,sample(0:1,60,rep=TRUE)), replicate(2,sample(0:1,60,rep=TRUE)), replicate(2,sample(0:1,60,rep=TRUE)), replicate(2,sample(0:1,60,rep=TRUE)), row.names = T)

df[c('stimuli', 'il15'),] <- NA
df[c('pdgf', 'stimuli2', 'cd45', 'tax'),] <- NA


dfA <- df
for (i in 1:ncol(df)){
  dfA[trmt[["A"]],] <- 1
}
names(dfA) <- paste("A", 1:ncol(df), sep = "")


df2 <- dfA
for(let in toupper(letters[2:7])){
  temp <- df
  for(i in 1:ncol(df)){
    temp[trmt[[let]], ] <- 1
  }
  names(temp) <- paste(let, 1:ncol(df), sep = "")
  df2 <- cbind(df2 , temp)
}

df2 <- df
i = 1
for(let in toupper(letters[1:7])){
  df2[trmt[[let]],i:i+1] <- 1
  i <- i+2
}

states <- df2
attractors<-getAttractors(network, type = 'asynchronous', method = 'chosen',startStates=states,returnTable = TRUE)
sink(file="attractors_sync2_70.txt",type="output")
attractors
sink(file=NULL)
