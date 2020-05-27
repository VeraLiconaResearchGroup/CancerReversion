import scipy.spatial
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl 
mpl.use('agg')

#DAC for readout nodes between boolean attractors (Apoptosis- Leukemia)

booleanDAC = {"apoptosis":1, "bid":1, "ceramide":1, "disc":1, "fas":1, "iap":-1,  "s1p":-1}
boolDAC = pd.DataFrame(booleanDAC.values(), index = booleanDAC.keys(), columns = ["BooleanDAC"])

df = pd.read_csv('new_RONs_DACandHam/DAC_A_L1_RONs.txt', delim_whitespace = True, index_col = ["leuk_attr", "apop_attr"])


##hamming  = pd.DataFrame(columns = ['hamming_distance'], index = df.index)
##hamming = df.apply(scipy.spatial.distance.hamming, 1, args = [booleanDAC])
##print(hamming.describe())
##
### Create a figure instance
##fig = plt.figure(1, figsize=(9, 6))
##
### Create an axes instance
##ax = fig.add_subplot(111)
##
### Create the boxplot
##bp = ax.boxplot((1-hamming)*100)
##
### Save the figure
##fig.savefig('fig1.png', bbox_inches='tight')
##
##countdf = pd.DataFrame(hamming.value_counts(), columns = ['Count'])
##countdf['Percent'] = countdf.Count/sum(countdf.Count)*100
##countdf['Percent_Accuracy'] = (1-countdf.index)*100
##countdf.sort_values(by = ['Percent_Accuracy'], inplace = True)
##final = countdf[['Percent_Accuracy','Percent']]
##final.index = range(final.shape[0])
##final.columns = ['Percent_Accuracy', 'Percent_Attractors']
##print(final)

# Hamming distance for nodes without Boolean DAC of 0

boolDAC2 = boolDAC[boolDAC["BooleanDAC"] !=0]
hamming2 = pd.DataFrame(columns = ['hamming_distance'], index = boolDAC2.index)

df2 = df.loc[:,boolDAC2.index]
hamming = df2.apply(scipy.spatial.distance.hamming, 1, args = [boolDAC2["BooleanDAC"]])
d = pd.DataFrame(hamming, columns = ['Hamming_Distance'])
d["Percent_accuracy"] = (1-d.Hamming_Distance)*100
d.to_csv('new_RONs_DACandHam2/hamming_DAC_A_L1.txt', sep = ' ')
print(hamming.describe())

# Create a figure instance
fig = plt.figure(1, figsize=(6, 6))
ax = fig.add_subplot(111)
bp = ax.boxplot((1-hamming)*100)
ax.set_title('Hamming Distance for DAC of RONs comparing\n Apoptosis basin to Leukemia1 basin')
ax.set_ylabel('Percent Accuracy in RONs')
ax.set_xticks([])


# Save the figure
fig.savefig('new_RONs_DACandHam2/hamming_boxplot_L1.png', bbox_inches='tight')

countdf = pd.DataFrame(hamming.value_counts(), columns = ['Count'])
countdf['Percent'] = countdf.Count/sum(countdf.Count)*100


countdf['Percent_Accuracy'] = (1-countdf.index)*100
countdf.sort_values(by = ['Percent_Accuracy'], inplace = True)
final = countdf[['Percent_Accuracy','Percent']]
final.index = range(final.shape[0])
final.columns = ['Percent_Accuracy', 'Percent_Attractors']
final.sort_values(by = ['Percent_Accuracy'], inplace = True, ascending = False)
final.to_csv('new_RONs_DACandHam2/hamming_DAC_A_L1_summary.txt', sep = ' ')
print(final)

