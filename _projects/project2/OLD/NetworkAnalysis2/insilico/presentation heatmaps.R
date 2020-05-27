# Heatmaps

library(readxl)
library(NMF)
library(readr)
library(tidyverse)
norm <- read.table('normal_DAC_disc.txt', row.names = 1, header = TRUE)
norm <- norm %>% t() %>% as.data.frame()
# norm <- norm %>% scale()
avg_exp <- read_delim("for_heatmaps_attrs.txt", "\t",  escape_double = FALSE, col_names = TRUE, col_types = cols(name = col_character(), MCF10A = col_number(),Pert= col_number(), MDAMB231 = col_number()), trim_ws = TRUE)
# avg_expr <- read.table('for_heatmaps_attrs.txt', row.names = 1)
avg_expr<-data.frame(avg_exp)
avg_expr <- avg_expr[,-4]
rownames(avg_expr)=avg_expr[,1]
avg_expr = avg_expr[,-1]
names(avg_expr)<-c('MDA-MB-231','MCF10A')#, 'Pert')
apply(avg_expr, 2, as.numeric)
aheatmap(avg_expr, hclustfun = "complete",cellwidth= 20, color=colorRampPalette(c('navy','white','firebrick3'))(80),filename="attractors.png")
aheatmap(norm, hclustfun = "complete",cellwidth= 20,  color=colorRampPalette(c('navy','white','firebrick3'))(80),filename="norm_attractors.png")

row.names(avg_expr) <- row.names(norm)
df <- cbind(avg_exp, norm)
df <- df[,-1]
apply(df, 2, as.numeric)
aheatmap(df, hclustfun = "complete",cellwidth= 80, color=colorRampPalette(c('navy','white','firebrick3'))(80),filename="all.png")

norm3 <- norm[,c("MCF10A","Perturb_0285488")] 
norm3$MDAMB231 <- rep(0, nrow(norm3))

RON <- c("CASP3", "CCNG2", "CDC20", "CDC25A", "CDC25C", "CDK1", "CYLD", "FYN", "HDAC1", "HUWE1", "KAT2B", "NOTCH1", "PRKCD", "PTK6", "PTPN1", "RAC1", "RB1", "RPS6KA3", "S100A2")
norm2 <- norm3[row.names(norm3) %in% paste(RON,"_DAC", sep = ""),]
aheatmap(norm3, hclustfun = "complete",cellwidth= 80,  scale = "row",color=colorRampPalette(c('navy','white','firebrick3'))(80),filename="attractors_ofint_DAC_disc.png")

df2 <- df[row.names(df) %in% paste(RON,"", sep = ""),]
aheatmap(df2, hclustfun = "complete",cellwidth= 80,  color=colorRampPalette(c('navy','white','firebrick3'))(80),filename="norm_attractors_RON_logss.png")

network <- read_delim("network_avg_expression_10A_231.csv", ",", escape_double = FALSE, col_names = TRUE, col_types = cols(MCF10A.mean = col_number(),MDA_MB.231.mean = col_number()), trim_ws = TRUE)
avg_expr<-data.frame(network)
rownames(avg_expr)=avg_expr[,1]
avg_expr = avg_expr[,-1]
names(avg_expr)<-c('MCF10A','MDA-MB-231')
apply(avg_expr, 2, as.numeric)
aheatmap(avg_expr, hclustfun = "complete", cellwidth= 80, Rowv = NA, color=colorRampPalette(c('navy','white','firebrick3'))(80),filename="RNAseq.png")
