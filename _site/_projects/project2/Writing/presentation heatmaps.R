# Heatmaps

library(readxl)
library(NMF)
library(readr)
avg_exp <- read_delim("attractors.txt", "\t", escape_double = FALSE, col_names = TRUE, col_types = cols(MCF10A = col_number(),MDAMB231 = col_number()), trim_ws = TRUE)
avg_expr<-data.frame(avg_exp)
rownames(avg_expr)=avg_expr[,1]
avg_expr = avg_expr[,-1]
names(avg_expr)<-c('MCF10A','MDA-MB-231')
apply(avg_expr, 2, as.numeric)
aheatmap(avg_expr, hclustfun = "complete",cellwidth= 80, Rowv = NA, color=colorRampPalette(c('navy','white','firebrick3'))(80),filename="attractors.png")

network <- read_delim("network_avg_expression_10A_231.csv", ",", escape_double = FALSE, col_names = TRUE, col_types = cols(MCF10A.mean = col_number(),MDA_MB.231.mean = col_number()), trim_ws = TRUE)
avg_expr<-data.frame(network)
rownames(avg_expr)=avg_expr[,1]
avg_expr = avg_expr[,-1]
names(avg_expr)<-c('MCF10A','MDA-MB-231')
apply(avg_expr, 2, as.numeric)
aheatmap(avg_expr, hclustfun = "complete", cellwidth= 80, Rowv = NA, color=colorRampPalette(c('navy','white','firebrick3'))(80),filename="RNAseq.png")
