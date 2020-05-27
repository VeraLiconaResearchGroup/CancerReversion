#---------------------------------------------------------
# convert_ID.R Converts ensembl ID to Gene Symbol ID for gene expression data of network nodes
#
# INPUTS:
# 1. Dataframe with Ensembl ID and Hugo ID for expressed genes in MDA-MB-231
# 2. List of network nodes
# 3. Normalized expression data
#---------------------------------------------------------

setwd("~/Documents/GitHub/gastonguay_compsysmed_labnotebook/_projects/project2/Network_Analysis/test_RNAseq2")

# Read in dataframe with ensembl and gene symbol IDs
df <- read.delim("~/Documents/GitHub/gastonguay_compsysmed_labnotebook/_projects/geneXplain_backup/231_prtn_genes_all_expressed.txt", stringsAsFactors = F)

#Read in network nodes
network_nodes <- scan("~/Documents/GitHub/gastonguay_compsysmed_labnotebook/_projects/project2/network analysis 3/inputfiles/network_nodes_227.txt", what = character())

# Read in normalized expression
normalized_expression <- read.delim("~/Documents/GitHub/gastonguay_compsysmed_labnotebook/_projects/project2/discussion/normalized_expression.txt", stringsAsFactors = F)

# Replace ensembl IDs with Gene IDs
ens <- df %>% filter(Gene_Symbol %in% network_nodes) %>% select(ID, Gene_Symbol)

normalized_expression$ID <- str_split(normalized_expression$gene, '.', 1)

temp <- c()
for(t in normalized_expression$gene){temp <- c(temp, unlist(str_split(t, "\\."))[1])}

normalized_expression$ID <-temp

new_df <- normalized_expression %>% filter(ID %in% ens$ID)

temp2 <- c()
for(t in new_df$ID){
  temp2 <- c(temp2, ens[ens$ID == t, "Gene_Symbol"])
}

new_df$gene_symbol <- temp2

write.table(new_df, 'Normalized_expression_genesymbol.txt', quote = F, row.names = F)