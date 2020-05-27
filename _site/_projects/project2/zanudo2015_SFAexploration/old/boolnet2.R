library(tidyverse)
library(BoolNet)
# setwd("C:/Users/marazzi/Dropbox/Marazzi/Control_DynamicalSystems/Fall_2019/zanudo2015")
setwd("/Volumes/GoogleDrive/My Drive/ALS_IPS/zanudo2015")
network <- loadNetwork("zanudo_boolean.bn")

df <- data.frame(nodes = c( "a20","apoptosis","bclxl","bid","caspase","ceramide","creb","ctla4","cytoskeletonsignaling","disc","erk","fas",
                            "fasl","fast","flip","fyn","gap","gpcr","grb2","gzmb","iap","ifng","ifngt","il2","il2ra","il2rat","il2rb","il2rbt",
                            "jak","lck","mcl1","mek","nfat","nfkb","p2","p27","pdgfr","pi3k","plcg1","proliferation","rantes","ras","s1p","sfas",
                            "smad","socs","sphk1","stat3","tbet","tcr","tnf","tpl2","tradd","zap70","il15","stimuli","cd45","stimuli2","pdgf","tax"),
                 A = c(0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0),
                 B = c(1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0),
                 C = c(1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0),
                 D = c(0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0),
                 E = c(1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1),
                 F = c(0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0),
                 G = c(1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1),
                 row.names = T)

# df[,c(toupper(letters[1:7]))] <- rep(0,60)
# df[c('stimuli2', 'stimuli', 'il15'),] <- rep(1, ncol(df))

trmt <- list('A' = "sphk1", "B" = "pdgfr", "C" = c("tbet", "ceramide", "ras"), 
             "D" = c("tbet", "ceramide", "grb2"), "E" = c("tbet", "ceramide", "il2rb"), 
             "F"= c("tbet", "ceramide", "il2rbt"), "G" = c("tbet", "ceramide", "erk") )

for(name in names(df)){
  df[trmt[[name]], name] <- 1
}

names(df) <- trmt

# write.table(df, "initial_states.txt", row.names = TRUE, quote = FALSE)

# states <- read.table('initial_states.txt', header = TRUE, row.names = 1)

states <- df

# nodes <- c("ctla4", "tcr", "pdgfr", "fyn", "cytoskeletonsignaling", "lck", "zap70", "grb2", "plcg1", "ras", "gap", "mek", "erk", "pi3k", "nfkb", "nfat", "rantes", "il2", "il2rbt", "il2rb", "il2rat", "il2ra", "jak", "socs", "stat3", "p27", "proliferation", "tbet", "creb", "ifngt", "ifng", "p2", "gzmb", "tpl2", "tnf", "tradd", "fasl", "fast", "fas", "sfas", "ceramide", "disc", "caspase", "flip", "a20", "bid", "iap", "bclxl", "mcl1", "apoptosis", "gpcr", "smad", "sphk1", "s1p", "stimuli", "pdgf", "cd45", "il15", "stimuli2", "tax")
# df <- data.frame(nodes, 1:60) %>% arrange(nodes)
# df$order <- 1:60
# df <- arrange(df, X1.60)
# states2 <- states[df$order, ]
# rownames(states2) <- nodes
# states2 <- states2[,-1]


attractors<-getAttractors(network, type = 'synchronous', method = 'chosen',startStates=states,returnTable = TRUE)
sink(file="attractors_sync_new.txt",type="output")
attractors
sink(file=NULL)

sink(file="basin6.txt",type="output")
getBasinOfAttraction(attractors, 6)
#hi<-getAttractorSequence(attractors_all, 15)
sink(file=NULL)


attractors<-getAttractors(network, type = 'asynchronous', method = 'random',startStates=100000)
sink(file="attractors_async.txt",type="output")
attractors
sink(file=NULL)


listicle<-list(vec1)
attractor1<-getAttractors(network, type = 'synchronous', method = 'chosen', startStates = listicle,returnTable = TRUE)
sink(file="attractor_20000_basin_path.txt",type="output")
attractor1
getBasinOfAttraction(attractor1,1)
sink(file=NULL)


vec1<-c(0,1,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0)
paths<-getPathToAttractor(network,vec1, includeAttractorStates="all")
paths<- paths[,order(names(paths))]
paths<-as.data.frame(t(paths))
write.table(paths,"path_15_4_bn.txt",quote=FALSE,row.names = FALSE)
# 
# getBasinOfAttraction(attractors_all, 1)
# 
# opar <- par(no.readonly = TRUE)
# par(mfrow=c(2, length(attractors_all$attractors)), mar = rep(2,4))
# print(attractors_all)
# 
# p<-plotAttractors(attractors_all)
# attrs <- cbind(p$`1`, p$`4`)
# 
# par(opar)
# pdf(paste("boolnet_attractors_sat_exhaustive.pdf", sep = ""))
# plotAttractors(attractors_all)
# plotAttractors(attractors_all, mode="graph")
# dev.off()
# 
# attractors<-getAttractors(network, type = 'synchronous', method = 'chosen', startStates = states)
# par(mfrow=c(2, length(attractors$attractors)))
# print(attractors, activeOnly=TRUE)
# 
# 
# pdf(paste("boolnet_attractors.pdf", sep = ""))
# plotAttractors(attractors)
# plotAttractors(attractors, mode="graph")
# dev.off()
# 
# 
# #Compare attractor k from SFA to boolean landscape
# k <- data.frame(1,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0) %>% t() %>% as.data.frame()
# row.names(k) <- row.names(attrs)
# 
# myfun <- function(col){
#   return(col - k$V1)
# }
# 
# attrs2 <- apply(attrs, 2, myfun)
# apply(attrs2, 2, sum) #Difference between k and all of the attractors from boolnet is never 0 so it is not included in the boolean landscape
