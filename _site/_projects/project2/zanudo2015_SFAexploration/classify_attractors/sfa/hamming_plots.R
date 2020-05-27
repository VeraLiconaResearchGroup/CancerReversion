setwd("~/Google Drive File Stream/My Drive/ALS_IPS/zanudo2015/classify_attractors/sfa")
h1 <- read.table('hamming_DAC_A_L1.txt', header = TRUE)
h2 <- read.table('new_RONs_DACandHam2/hamming_DAC_A_L1.txt', header = TRUE)
h1$RONs <- 'old'
h2$RONs <- 'new'

h3 <- rbind(h1,h2)
png('new_RONs_DACandHam2/boxplot_L1_hamming_newvold_RON.png')
boxplot(h3$Percent_accuracy ~ h3$RONs, xlab = 'RON set', ylab= 'Percent accuracy in RONs', main = 'Hamming Distance of DAC of RONs comparing\n Apoptosis basin to Leukemia1 basin',notch = TRUE)
dev.off()

h4 <- read.table('hamming_DAC_A_L2.txt', header = TRUE)
h5 <- read.table('new_RONs_DACandHam2/hamming_DAC_A_L2.txt', header = TRUE)
h4$RONs <- 'old'
h5$RONs <- 'new'
h6 <- rbind(h4,h5)
png('new_RONs_DACandHam2/boxplot_L2_hamming_newvold_RON.png')
boxplot(h6$Percent_accuracy ~ h6$RONs, xlab = 'RON set', ylab= 'Percent accuracy in RONs', main = 'Hamming Distance of DAC of RONs comparing\n Apoptosis basin to Leukemia2 basin', notch  = TRUE)
dev.off()

h7 <- rbind(h3,h6)
png('new_RONs_DACandHam2/boxplot_hamming_newvold_RON.png')
boxplot(h7$Percent_accuracy ~ h7$RONs, xlab = 'RON set', ylab= 'Percent accuracy in RONs', main = 'Hamming Distance of DAC of RONs comparing\n Apoptosis basin to both Leukemia basin', notch  = TRUE)
dev.off()


png('new_RONs_DACandHam2/hamming_newRON.png')
boxplot((h7 %>% filter(RONs == 'new'))$Percent_accuracy, notch = T, ylab = "Percent Accuracy in Readout Nodes")
dev.off()

df1 <- read.table('DAC_A_L1_all.txt', header = TRUE)
df1$flip <- as.factor(df1$flip)
table(df1$flip)

df2 <- read.table('DAC_A_L2_all.txt', header = TRUE)
df2$flip <- as.factor(df2$flip)
table(df2$flip)

df <- rbind(h2,h5)
summary <- table(df$Percent_accuracy) %>% as.data.frame()
summary %>% mutate(`Percent of Comparisons` = round(Freq/sum(Freq)*100,2))
