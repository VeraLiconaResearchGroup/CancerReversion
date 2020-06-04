setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) #set wd to wherever script is located

dataset = 'both'

pdf(paste('mds_kmeans_', dataset, '_boolnet.pdf', sep = ""))
for(k in 2:15){
  mds2 <- read.table(paste("mds_boolnet_", dataset, "_2.txt", sep = ""), header = T, row.names = 1)
  mds3 <- read.table(paste("mds_boolnet_", dataset, "_3.txt", sep = ""), header = T, row.names = 1)
  # mds3 <- mds3[,1:2]
  # clusters <- read.table(paste("kmeans_", dataset, "/kmeans_", dataset, k, '.txt', sep= ""), header = T, row.names = 1)
  
  exprl <- read.table('../classify_attractors/boolnet/leukemia_boolnet.txt', stringsAsFactors = F)
  expra <- read.table('../classify_attractors/boolnet/apoptosis_boolnet.txt', stringsAsFactors = F)
  # Add attractor numbers for leukemia1, leukemia2, and apoptosis
  exprl[nrow(exprl)+1,"V1"] <- 'attr_507'
  exprl[nrow(exprl)+1,] <- 'attr_284'
  expra[nrow(expra)+1,] <- 'attr_195'
  
  phenotype <- rep('other', nrow(mds2))
  phenotype[rownames(mds2) %in% exprl$V1] <- 'Leukemia'
  phenotype[rownames(mds2) %in% expra$V1] <- 'Apoptosis'
  
  # print(ggplot(mds2, aes(X,Y)) + geom_point(aes(shape = phenotype, color = as.factor(clusters$clusters)), cex = 2) +
  #   geom_text(data = mds2[which(intattr_names %in% c("attr_195", "attr_507", "attr_284")),], label = c('Apoptosis', "Leukemia", "Leukemia"), show.legend = F) +
  #   theme_bw() + 
  #   theme(panel.border = element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(), 
  #           axis.line = element_line(colour = "black")))
  
  k4 <- kmeans(mds2, k, nstart = 10000)
  temp <- k4$cluster %>% as.data.frame()
  names(temp) <- 'cluster'
  temp$attractor <- rownames(temp)
  temp <- temp[,2:1]
  write.table(temp, paste("kmeans_", dataset, "_2d/kmeans_", dataset, k, ".txt", sep = ""), quote = F, row.names = F)
  k = 7
  k4 <- read.table(paste("kmeans_", dataset, "_2d/kmeans_", dataset, k, ".txt", sep = ""), header = T, row.names = 1)
  names(k4) <- 'cluster'
  
  print(ggplot(mds2, aes(X,Y)) + geom_point(aes(color =  as.factor(k4$cluster),shape = phenotype),  cex = 2) +
    geom_text(data = mds2[which(intattr_names %in% c("attr_195", "attr_507", "attr_284")),], aes(X, Y), label = c('Apoptosis', "Leukemia", "Leukemia"), show.legend = F) +
    theme_bw() +
    theme(panel.border = element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
                axis.line = element_line(colour = "black")))

  # fig <- plot_ly(plot, x = ~V1, y = ~V2, z = ~V3, color = ~k4$cluster)
  # fig <- fig %>% add_markers()
  # fig
}
dev.off()
