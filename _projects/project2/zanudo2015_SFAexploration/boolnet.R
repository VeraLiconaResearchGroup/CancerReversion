library(tidyverse)
library(BoolNet)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) #set wd to wherever script is located
network <- loadNetwork("zanudo_boolean.bn")
states <- read.table('basal_states.txt', header = TRUE)
nodes <- c("ctla4", "tcr", "pdgfr", "fyn", "cytoskeletonsignaling", "lck", "zap70", "grb2", "plcg1", "ras", "gap", "mek", "erk", "pi3k", "nfkb", "nfat", "rantes", "il2", "il2rbt", "il2rb", "il2rat", "il2ra", "jak", "socs", "stat3", "p27", "proliferation", "tbet", "creb", "ifngt", "ifng", "p2", "gzmb", "tpl2", "tnf", "tradd", "fasl", "fast", "fas", "sfas", "ceramide", "disc", "caspase", "flip", "a20", "bid", "iap", "bclxl", "mcl1", "apoptosis", "gpcr", "smad", "sphk1", "s1p", "stimuli", "pdgf", "cd45", "il15", "stimuli2", "tax")
df <- data.frame(nodes, 1:60) %>% arrange(nodes)
df$order <- 1:60
df <- arrange(df, X1.60)
states2 <- states[df$order, ]
rownames(states2) <- nodes
states2 <- states2[,-1]

states2t=t(states2)
write.csv(states2t,"boolnet_ordered.txt",row.names = FALSE,quote=FALSE)


attractors_all<-getAttractors(network, type = 'synchronous', method = 'random',startStates=10000,returnTable = TRUE)
sink(file="attractors1220.txt",type="output")
attractors_all
sink(file=NULL)
sink(file="basin_15.txt",type="output")
getBasinOfAttraction(attractors_all,15)
#hi<-getAttractorSequence(attractors_all, 15)
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
