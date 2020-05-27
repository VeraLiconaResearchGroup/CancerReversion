import pandas as pd

d1 = pd.read_csv('231_all_expressed_genes_andprtn', delim_whitespace = True, index_col = False)
d2 = pd.read_csv('SOC_pval_276', delim_whitespace = True, index_col = False)

d3 = d2.loc[d2.iloc[:,0].isin(d1.iloc[:,0]),:]
d3.to_csv('SOC_pval_expressed_210', sep = " " , index = False, header = False)
