setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) #set wd to wherever script is located
library(tidyverse)
library(RColorBrewer)
theme_set(theme_bw(base_size=12) + theme(panel.grid = element_blank()))

####################### User Specifications ####################

###################### Read in files ###########################
# IS to Boolean attractors
Apop <- read.table('sfa_Apop_all.txt', header = T, row.names = 1)
Leuk1 <-  read.table("sfa_L1_states.txt", header = T, row.names = 1)
Leuk2 <-  read.table("sfa_L2_states.txt", header = T, row.names = 1)

###############################################################
Leuk <- rbind(Leuk1, Leuk2)

Apop$phenotype <- "Apoptosis"
Leuk$phenotype <- "Leukemia"

# Get boxplots for each node in each cluster
RONs <- c('apoptosis', 'bid', 'ceramide', 'disc', 'fas','iap' ,'s1p')


logss <- rbind(Apop, Leuk)
logss <- logss[,c(RONs, "phenotype")]


# pdf(paste(folder, "/cluster_report/Expression_distribution_", k,".pdf", sep = ""))
pdf('Distribution_of_fixed_sfa_logss.pdf')
for(node in names(logss[,-ncol(logss)])){
  # print(ggplot(logss, aes_string("clusters", node, fill = "clusters")) +
  #         geom_boxplot(notch = T) + ggtitle(paste("Log Steady State Expression of", node)) +
  #         xlab("cluster") + ylab("Log Steady State Expression") +
  #         scale_fill_manual(values = getPalette(colourCount)))

  print(ggplot(data = logss, aes_string("phenotype", node)) +
          geom_boxplot() +
          geom_jitter(shape=16, position=position_jitter(0.2), aes(color = phenotype)) +
          ggtitle(paste("Log Steady State Expression of ", node, sep = "")) +
          xlab("phenotype") + ylab("Log Steady State Expression") +
          guides(colour = guide_legend(override.aes = list(alpha = 1))))
}
dev.off()


# # pdf(paste(folder, "/cluster_report/Expression_distribution_", k,".pdf", sep = ""))
# pdf('density_of_sfa_logss.pdf')
# for(node in names(logss[,-ncol(logss)])){
#   # print(ggplot(logss, aes_string("clusters", node, fill = "clusters")) + 
#   #         geom_boxplot(notch = T) + ggtitle(paste("Log Steady State Expression of", node)) + 
#   #         xlab("cluster") + ylab("Log Steady State Expression") + 
#   #         scale_fill_manual(values = getPalette(colourCount)))
#   
#   print(ggplot(data = logss, aes_string(node, fill = 'phenotype')) +
#           geom_density(alpha = 0.5) + 
#           ggtitle(paste("Density of Log Steady State Expression of ", node, sep = "")) +
#           xlab("Log Steady State Expression") + 
#           guides(colour = guide_legend(override.aes = list(alpha = 1))))
# }
# dev.off()



