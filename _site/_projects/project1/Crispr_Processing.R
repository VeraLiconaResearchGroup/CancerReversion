# Extracting CRISPR data

setwd("~/Documents/GitHub/gastonguay_compsysmed_labnotebook/_projects/project1")

#Load libraries
library(tidyverse)

#read in desired nodes
nodes <- read.csv() %>% t()


#read in CRISPR data
crsipr <- read.csv()



for (node in names(nodes))
{
  if (node in names(crispr))
  {
    df$node <- crispr$node[3]
  }
}
  