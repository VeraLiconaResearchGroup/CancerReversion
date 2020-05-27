setwd("C:/Users/marazzi/Dropbox/Marazzi/Control_DynamicalSystems/Fall_2019/zanudo2015")
test <- read.table('attr_logss.txt', header = TRUE,row.names=1)
vector <- c()
for(name in names(test)) vector <- c(vector, test[[name]])

hist(vector)
