import pandas as pd
from scipy import stats
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from sklearn.manifold import MDS

# Read in Datasets to cluster

d1 = pd.read_csv('boolnet_attractors_noX.txt', delim_whitespace = True, index_col = ['name'])
d2 = pd.read_csv('boolnet_DAC_noX.txt', delim_whitespace = True, index_col = ['name'])
d3 = pd.read_csv('boolnet_both_noX.txt', delim_whitespace = True, index_col = ['name'])

mds = MDS(2, metric = True, n_init = 25, n_jobs = -1)
hey = mds.fit(d1)
