
# ham <- read.table('sfa/hamming_DAC_A_L1.txt', header = TRUE)
ham <- read.table('sfa/hamming_DAC_A_L2.txt', header = TRUE)
ham2 <- ham %>% filter(Percent_accuracy == 100)
ham2$apop_attr <- factor(ham2$apop_attr, levels = unique(ham2$apop_attr))
(t1 <- table(ham2$apop_attr)/length(unique(ham2$leuk_attr))*100)
summary(as.numeric(t1))
(a <- names(t1[t1>=60]))
length(a)

length(unique(ham2$apop_attr))
# write.table(unique(ham2$apop_attr), 'sfa/GOODAPOPBASIN.txt', quote  =FALSE, row.names = FALSE)
(bad_apop <- unique(ham$apop_attr[which(!(ham$apop_attr %in% intersect(ham$apop_attr, ham2$apop_attr)))]))
length(bad_apop) #19 apoptosis attractors that never give a good DAC when compared to L1

#Explore leukemia attractors combined with the 'good' apoptosis attractors
(t <- table(ham2$leuk_attr)/length(unique(ham2$apop_attr))*100)
summary(as.numeric(t))
length(unique(ham2$leuk_attr))
# Conisder those leukemia attrs accurate more than 70% of the time:
(l <- names(t[t>=70]))


ham2 <- read.table('hamming_DAC_A_L2.txt', header = TRUE)
ham1 <- read.table('hamming_DAC_A_L1.txt', header = TRUE)

ham2n <- read.table('new_RONs_DACandHam/hamming_DAC_A_L2.txt', header = TRUE)
ham1n <- read.table('new_RONs_DACandHam/hamming_DAC_A_L1.txt', header = TRUE)

ham <- rbind(ham1,ham2)
ham$RONset <- 'old'
hamn <- rbind(ham1n,ham2n)
hamn$RONset <- 'new'
ham_all <- rbind(ham,hamn)
ham_all$RONset <- factor(ham_all$RONset, levels = c('old', 'new'), ordered = TRUE)

summary <- table(hamn$Percent_accuracy) %>% as.data.frame()
names(summary)= c('Percent Accuracy', 'Number of comparisons')
summary %>% mutate(`Percent of Attractors` = round(`Number of comparisons`/sum(`Number of comparisons`)*100,2))

boxplot(ham_all$Percent_accuracy ~ham_all$RONset, xlab = 'Set of RONs', ylab = 'Percent Accuracy in RONs', main = 'Hamming Distatnce for difference in RONs between \nApoptosis and Leukemia SFA attractors', notch = TRUE)
