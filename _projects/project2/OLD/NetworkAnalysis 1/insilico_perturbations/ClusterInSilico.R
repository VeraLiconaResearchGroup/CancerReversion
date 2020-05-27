library(tidyverse)
library(fpc)
library(cluster)

pref <- 'SFAoutput_full_FC1_'

n = 6561
nchar(n)
thing <- seq(1,6561)
suf <- c()
for( m in thing){
  suf <- c(suf, paste(paste(rep('0', 4 - nchar(m)), collapse = ""), m, sep = ""))
}

names <- paste(pref, suf, '.txt', sep ="")
df <- read.table(paste("SFAoutputFC1/SFAoutput_full_FC1_0100.txt", sep = ""), row.names = 1, header = FALSE)

for(name in names){
  df1 <- read.table(paste("SFAoutputFC1/", name, sep = ""), row.names = 1, header = FALSE)
  df <- cbind(df, df1)
}

df <- df[,-1]


# Discretize DAC
disc <- function(x){
  if(x < 0){
    x <- -1
  }else if(x > 0){
    x <- 1
  } else{
    x <- 0
  }
}

df_disc <- apply(df, c(1,2), disc) %>% as.data.frame()
df_disc <- df_disc %>% t() %>% as.data.frame()

row.names(df_disc) <- paste("Perturb_", suf, sep = "")
write.table(df_disc, "Perturbations_FC1.txt", quote = FALSE)

a231 <- read.table("../SFA_2/231_attractor_discrete", row.names = 1) %>% t() %>% as.data.frame()
a10a <- read.table("../SFA_2/10A_attractor_discrete", row.names = 1) %>% t() %>% as.data.frame()

data <- rbind(a231, a10a, df_disc)

k3 <- kmeans(data, centers = 3, nstart = 10000, iter.max = 30)
plotcluster(data, k3$cluster, bw = FALSE, pch = 16)
legend("bottomleft", c("cluster1", "cluster2", "cluster3"), col= c("black", "red", "green"), pch = c(16,16,16))


gapstat1 <- clusGap(data, kmeans, 15, B = 150, iter.max = 30, nstart = 100)
plot1 <- fviz_gap_stat(gapstat1, maxSE = list(method = "Tibs2001SEmax"))
plot1
maxSE(plot1$data$gap, plot1$data$SE.sim, method = "Tibs2001SEmax")


k10 <- kmeans(data, centers = 10, nstart = 10000, iter.max = 30)
plotcluster(data, k10$cluster, bw = FALSE, pch = 16)
legend("right", paste("Cluster", seq(1,10), sep = ""), col= rainbow(10), pch = rep(16, 10))


