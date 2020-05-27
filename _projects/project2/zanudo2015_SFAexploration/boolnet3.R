library(tidyverse)
library(BoolNet)
setwd("C:/Users/marazzi/Dropbox/Marazzi/Control_DynamicalSystems/Fall_2019/zanudo2015")
network <- loadNetwork("zanudo_boolean.bn")

#generate initial state where only il15 and stimuli are on
## result should just be a random attractor
state1<-generateState(network,c("stimuli"=1,"il15"=1))
attr1<-getAttractors(network, type="asynchronous",startStates=list(state1))
attr1s<-getAttractors(network, type="synchronous",startStates=list(state1))
print(attr1)
print(attr1s)


#generate initial state where ceramide is off and sphk1 is on permanently
#result should be apoptosis OFF
p1<-fixGenes(network,c("ceramide","sphk1"),c(0,1))
state2<-generateState(network,c("stimuli"=1,"il15"=1,"ceramide"=0,"sphk1"=1))           
attr2<-getAttractors(p1,type="asynchronous",startStates = list(state2))
print(attr2)
attr2s<-getAttractors(p1,type="synchronous",startStates = list(state2))
print(attr2s)


#generate initial state where ceramide, ras, and tbet are on permanently
#result should be apoptosis ON
p2<-fixGenes(network,c("tbet","ceramide","ras"),c(1,1,1))
state3<-generateState(network,c("stimuli"=1,"il15"=1,"ceramide"=1,"ras"=1,"tbet"=1))           
attr3<-getAttractors(p2,type="asynchronous",startStates = list(state3))
print(attr3)
attr3s<-getAttractors(p2,type="synchronous",startStates = list(state3))
print(attr3s)
