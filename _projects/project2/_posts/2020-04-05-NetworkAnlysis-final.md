---
layout: post
title: "Final Network Analysis"
date: "2020-04-05"
author: maddie
tags:
 - project02
 - static_network
---

<style>
table {
    width:100%;
}
</style>

# Objective
We will employ our pipeline to identify and prioritize putative reversion targets for MDA-MB-231. To do so, virtual screenings of perturbations of the 4 MDA-MB-231 initial conditions (Continuous Normalized RNAseq Expression Data) were run using SFA. The attractors resulting from these perturbations will be classified by knn with the 4 MCF10A and 4 MDA-MB-231 attractors as training sets. We will still "discretize" the output of vitrual screenings in the same way: positive values are represented as 1, negative value are represented as -1, and zeroes remain 0.

The analyses were all done on six datasets:
1. Log steady state
2. DAC
3. Combination of 1+2
4. Discrete log steady state
5. Discrete DAC
6. Combination of 4+5


# Virtual Screening
After an exploration of the use of SFA, we have deicded to initilize our virtual screenings with continuous RNAseq expression values as opposed to discretized values. The FVS are eithor knocked-out, knocked-in, or not changed. The value for knocked-out nodes is fixed at 0, while those that aren't changed are left alone. The question remains: what value should we set knock-in nodes to. We decided it should be specific to the gene as if we choose one value for over expression of any gene, it may not be large enough for some genes.

Since we have four MDAMB231 experimental expression values, we caluclated the mean and standard deviation between them for each FVS node. Then, we set the stimulation activity of a node to the mean activity of the node plus three standard deviations. However, we found that the standard deviation between expression values for the MDAMB231 replicates can be very small, in which case this method doesn't give a large increase in basal activity for knock-ins.

**FVS node**|**Mean**|**SD**|**Mean + 3SD**|**Activity Increase**
:-----:|:-----:|:-----:|:-----:|:-----:
AKT1|11.03917613|0.062919073|11.22793334|0.188757218
AURKA|10.57173554|0.525917137|12.14948695|1.577751411
CTNNB1|12.17360746|0.026141468|12.25203187|0.078424403
FOXM1|10.45660281|0.543256887|12.08637347|1.629770661
GSK3B|10.14239603|0.221541258|10.8070198|0.664623775
HDAC3|9.91842003|0.1072263|10.24009893|0.321678899
JUN|9.99992269|0.21922678|10.65760303|0.657680339
MAPK1|10.99320419|0.064925597|11.18798098|0.19477679
PIAS1|9.476911955|0.062199267|9.663509756|0.186597801
RELA|10.65095632|0.082948965|10.89980321|0.248846896
STAT3|11.03903899|0.144277973|11.47187291|0.432833919
TCF3|10.39763739|0.206599437|11.0174357|0.619798311

The plot below show the distribution of expression values of all network nodes for both the MDAMB231 and MCF10A experimental replicates. Red x's mark the value of knock-in expression for the FVS nodes when simulated as mean + 3\*sd.

![mean + 3sd]({{ site.baseurl }}\_assets\images_proj2\dist_sd.png)


Since using the [mean + 3\*sd](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project2/Network_Analysis/virtual_screening/perturbation_level_sd.txt) of the activity level of the SFA nodes did not provide enough of an increase in activity level, we explored multiplying the mean expression of each node by a factor. Intuitively, a knock-in of a gene resulting in an additionally copy of it would correlate to 2 times the amount of mRNA. However, after a brief literature search, we found that this is [not the case for all genes](https://febs.onlinelibrary.wiley.com/doi/pdf/10.1016/j.molonc.2013.02.018). There may be a point at which the machinery required for transcrption of a gene is exhausted, resulting in less than a 2 fold increase in activity levels. Therefore, we tested setting knock-in basal values to both [1.5 times the mean](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project2/Network_Analysis/virtual_screening/perturbation_level_factor1.5.txt) and [2 times the mean](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project2/Network_Analysis/virtual_screening/perturbation_level_factor2.txt). The plots below show the distribution of expression values of all network nodes for both the MDAMB231 and MCF10A experimental replicates. Red x's mark the value of knock-in expression for the FVS nodes.


**FVS node**|**Mean**|**1.5 * Mean**|**2 * Mean**
:-----:|:-----:|:-----:|:-----:
AKT1|11.03917613|16.55876419|22.07835225
AURKA|10.57173554|15.85760331|21.14347108
CTNNB1|12.17360746|18.26041119|24.34721493
FOXM1|10.45660281|15.68490421|20.91320562
GSK3B|10.14239603|15.21359404|20.28479205
HDAC3|9.91842003|14.87763005|19.83684006
JUN|9.99992269|14.99988404|19.99984538
MAPK1|10.99320419|16.48980628|21.98640838
PIAS1|9.476911955|14.21536793|18.95382391
RELA|10.65095632|15.97643448|21.30191264
STAT3|11.03903899|16.55855849|22.07807798
TCF3|10.39763739|15.59645608|20.79527478

![1.5mean]({{ site.baseurl }}\_assets\images_proj2\dist_15m.png)
![2mean]({{ site.baseurl }}\_assets\images_proj2\dist_2m.png)


Previously, we used the average expression level from MDA-MB-231 as the basal state to apply perturbations to. Now, we will use the four replicates of MDA-MB-231 as separate basal conditions and apply perturbations to all 4 basal states. This will act as 4 "experimental" replicates of our perturbations. Perturbations must result in a shift towards normal for all four replicates to be considered successful. We have 12 FVS nodes resulting in $3^{12} = 531441$ possible perturbations. So far, we have only examined 100,000 of these perturbations. We have only considered perturbations of the FVS, not the whole FC.

# K-nearest Neighbors Classifier
Using the 8 experimental attractors as a training set, we classified the 100,000 attractors resulting from FVS perturbations on all 6 datasets. Two questions arose during this:
1. How many clusters should we use for the training set?
2. What dataset should we use for the analysis?
3. What is the optimal number of neighbors?

The 8 reference attractors clearly fall into 4 clusters with clustered with k-means or multi dimensional scaling. Therefore, I will use 4 clusters for the training set: MDAMB231_A, MDAMB231_B, MCF10A_A, and MCF10A_B. 

![mds both]({{ site.baseurl }}\_assets\images_proj2\mds_both.png)
![mds both disc]({{ site.baseurl }}\_assets\images_proj2\mds_both_disc.png)

#### Exploring Distance Metrics in discrete datasets

The default distance metric for knn is euclidean distance. However, knn can be run using different distance metrics. For the discrete datasets only, I tested knn using the hamming distance between the perturbations and the training set. [Choo and Cho](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6739335/pdf/41598_2019_Article_49571.pdf) use Hamming distnace to determine the boundary of the basin of attraction for an attractor of a Boolean model. States with larger hamming distances are further away from the attractor than states with smaller hamming distances.

**Test case: MDAMB231_2**
(results below from simulation with 2\*Mean for knock-in)
<!---
Dataset: **Log steady state**
- 213 normal perturbations when k = 3
- 2630 normal perutbrations when k = 4
- 3543 when k = 5
- for k larger than 5, more than 80% of perturbations were classified as normal

Dataset: **DAC**
- 213 normal perturbations when k = 3
- 2630 normal perutbrations when k = 4
- 3542 when k = 5
- for k larger than 5, more than 80% of perturbations were classified as normal

Dataset: **Both**
- 213 normal perturbations when k = 3
- 2629 normal perutbrations when k = 4
- 3541 when k = 5
- for k larger than 5, more than 80% of perturbations were classified as normal
--->

<!---
**Test case: MDAMB231_2**

Dataset: **Log steady state discrete** (k=3)
- Every perturbation was classified as normal regardless of distance metric

Dataset: **DAC discrete** (k = 3)
- euclidean distance gave 1,455 normal
- hamming distance gave 1,455 normal
- Both lists are the same
- *52811 normal with hamming or euclidean when k = 4*

Dataset: **both discrete** (k = 3)
- euclidean distance gave 1,455 normal
- hamming distance gave 1,455 normal
- both lists are the same
- *52811 normal with hamming or euclidean when k = 4*
--->

**Table 1.** The number of attractors resulting from perturbations to MDAMB231_2 that are classified as normal based on different datasets and values of k. Stimulations simulated as 2*mean.

**Dataset**|**k = 3**|**k = 4**|**k = 5**|**k > 6**
:-----:|:-----:|:-----:|:-----:|:-----:
Logss|213|2630|3543|Over 80%
DAC|213|2630|3543|Over 80%
Both|213|2629|3542|Over 80%
Logss Disc|Everything|Everything|Nothing|…
DAC Disc|1455|52811|Over 90%|…
Both Disc|1455|52811|Over 90%|…
Logss Disc Hamming|Everything|Everything|Nothing|…
DAC Disc Hamming|1455|52811|Over 90%|…
Both Disc Hamming|1455|52811|Over 90%|…

**Notes:** 
- The 8 reference attractors are the same when discretized by their log steady state value
- Everything classified as normal by DAC discrete is also classified as normal by both discrete, regardless of distance metric.
- Since there are only two reference attractors per cluster, it makes sense to consider the 3 nearest neighbors. 212 of the normal perturbations from DAC with k = 3 are also normal from logss with k = 3 and both with k = 3.
- Only 19 of the perturbations calssified as normal by the raw datasets are also classified as normal by the discrete datasets when k = 3.

## Compare Knn results between simulations with stimulation set to 1.5\*mean and 2\*mean

**Test case: MDAMB231_2**
(results below from simulation with 1.5*Mean for knock-in)

**Table 2.** The number of attractors resulting from perturbations to MDAMB231_2 that are classified as normal based on different datasets and values of k. Stimulations simulated as 1.5*mean.

**Dataset**|**k = 3**|**k = 4**|**k = 5**|**k > 6**
:-----:|:-----:|:-----:|:-----:|:-----:
Logss|3|1089|1521|Over 80%
DAC|3|1087|1514|Over 80%
Both|3|1087|1514|Over 80%
Logss Disc|Everything|Everything|Nothing|…
DAC Disc|720|44558|Over 90%|…
Both Disc|720|44558|Over 90%|…
Logss Disc Hamming|Everything|Everything|Nothing|…
DAC Disc Hamming|720|44558|Over 90%|…
Both Disc Hamming|720|44558|Over 90%|…

<!---
Dataset: **Log steady state**
- 3 normal perturbations when k = 3
- 1089 normal perutbrations when k = 4
- 1521 when k = 5
- for k larger than 5, more than 80% of perturbations were classified as normal

Dataset: **DAC**
- 3 normal perturbations when k = 3
- 1087 normal perutbrations when k = 4
- 1514 when k = 5
- for k larger than 5, more than 80% of perturbations were classified as normal

Dataset: **Both**
- 3 normal perturbations when k = 3
- 1087 normal perutbrations when k = 4
- 1515 when k = 5
- for k larger than 5, more than 80% of perturbations were classified as normal

Dataset: **Log steady state discrete**
- either all normal or all cancerous depending on the k, regardless of distance metric

Dataset: **DAC discrete**
- 720 normal perturbations when k = 3 with hamming or euclidean distance
- 44,558 normal perutbrations when k = 4 with hamming or euclidean distance
- for k larger than 4, more than 90% of perturbations were classified as normal with hamming or euclidean distance

Dataset: **Both discrete**
- 720 normal perturbations when k = 3 with hamming or euclidean distance
- 44,558 normal perutbrations when k = 4 with hamming or euclidean distance
- for k larger than 4, more than 90% of perturbations were classified as normal 
--->

### Conclusions from looking at perturbations from MDAMB231_2

The perturbations from stimulations simultated as 1.5\*mean result in fewer normal perturbations than those simulatied with 2\*mean. The results from the raw datasets are different from the results from the discrete datasets. For the discrete datasets, it seems that looking at 3 nearest neighbors is the best option. Using hamming distance appears to give the same result as euclidean distance, but I will continue to take the intersection between the two. If these observations are consistent for the other sets of perturbations, we may only need to use the discrete DAC dataset insteda of the discrete both. 

These results are quite different from knn on the attractors simulated from discrete initial conditions. Previously, the hamming distance and euclidean distance did not return the same results. Additionally, the raw datasets did not calssify any perturbation as normal. Lastly, the discrete DAC dataset classified more attractors as normal than the discrete both dataset, but now they are classifying the same attractors as normal.

## Explore Intersection between perturbations on different replicates

### Data Set = Both Discrete, 3 Nearest Neighbors

**replicate**|**number of normal perts**
:-----:|:-----:
MDAMB231_1|22521
MDAMB231_2|1455
MDAMB231_3|12915
MDAMB231_4|1

**Intersection between perturbations classified as normal when applied to each replicate:**

| |**MDAMB231_1**|**MDAMB231_2**|**MDAMB231_3**|**MDAMB231_4**
:-----:|:-----:|:-----:|:-----:|:-----:
MDAMB231_1|22521|0|11235|0
MDAMB231_2|0|1455|0|1
MDAMB231_3|11235|0|12915|0
MDAMB231_4|0|1|0|1


### Data Set = Both Discrete, 2 Nearest Neighbors

**Replicate**|**number of normal perts**
:-----:|:-----:
MDAMB231_1|28311
MDAMB231_2|1936
MDAMB231_3|17815
MDAMB231_4|69

**Intersection between perturbations classified as normal when applied to each replicate:**

| |**MDAMB231_1**|**MDAMB231_2**|**MDAMB231_3**|**MDAMB231_4**| 
:-----:|:-----:|:-----:|:-----:|:-----:
MDAMB231_1|28311|0|15240|0
MDAMB231_2|0|1936|0|62
MDAMB231_3|15240|0|17815|0
MDAMB231_4|0|62|0|69


### Data Set = Both Discrete, 4 Nearest Neighbors

**Replicate**|**number of normal perts**
:-----:|:-----:
MDAMB231_1|67085
MDAMB231_2|52811
MDAMB231_3|49918
MDAMB231_4|59488

**Intersection between perturbations classified as normal when applied to each replicate:**

| |**MDAMB231_1**|**MDAMB231_2**|**MDAMB231_3**|**MDAMB231_4**
:-----:|:-----:|:-----:|:-----:|:-----:
MDAMB231_1|67085|38616|46630|39413
MDAMB231_2|38616|52811|32214|38483
MDAMB231_3|46630|32214|49918|29091
MDAMB231_4|39413|38483|29091|59488

**Notes:** 
- Same results for DAC discrete or both discrete, reagardless of distance metric.
- Similar results when stimulation simulated as 1.5\*mean

## Check out Raw datasets

### Data Set = Both, 3 Nearest Neighbors, Stimulation = 2*mean

**Replicate**|**number of normal perts**
:-----:|:-----:
MDAMB231\_1|270
MDAMB231\_2|213
MDAMB231\_3|277
MDAMB231\_4|191

**Intersection between perturbations classified as normal when applied to each replicate:**

| |**MDAMB231\_1**|**MDAMB231\_2**|**MDAMB231\_3**|**MDAMB231\_4**| 
:-----:|:-----:|:-----:|:-----:|:-----:
MDAMB231\_1|270|173|256|159
MDAMB231\_2|173|213|185|191
MDAMB231\_3|256|185|277|169
MDAMB231\_4|159|191|169|191

### Data Set = Both, 3 Nearest Neighbors, Stimulation = 1.5*mean

**Replicate**|**number of normal perts**
:-----:|:-----:
MDAMB231\_1|5
MDAMB231\_2|3
MDAMB231\_3|4
MDAMB231\_4|2

**Intersection between perturbations classified as normal when applied to each replicate:**

| |**MDAMB231\_1**|**MDAMB231\_2**|**MDAMB231\_3**|**MDAMB231\_4**| 
:-----:|:-----:|:-----:|:-----:|:-----:
MDAMB231\_1|5|3|4|2
MDAMB231\_2|3|3|3|2
MDAMB231\_3|4|3|4|2
MDAMB231\_4|2|2|2|2

## Conclusions
- The raw datasets provide more overlap between experimental replicates than the dsicrete datasets, however I don't know if we should be using them based on how the SFA output should be interpreted. 
- Simulating knock-ins with  2\*Mean gives more perturbations than simulating them as  1.5\*Mean.
- I can explore the knn results using 2 clusters for training to see if it makes a difference

## Decisions to Make:
1. What basal activity level do we want to consider a stimualtion or knock-in?
 - A: 2\*Mean
2. Which dataset should we use and how many neighbors should we consider?
 - More exploring needs to be done (see below)


# Exploring knn results using 2 clusters for training

To determine if the discrete datasets did not have overlap of perturbations triggering a shift to the normal cluster, we treid knn classification with 2 clusters in the training set: one with all four cancerous attractors and one with all four normal attractors.

### MDAMB231_1

**Dataset**|**k =1**|**k=2**|**k=3**|**k=4**|**k = 5**|**k = 6**|**k = 7**|**k = 8**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
logss|374|555|255|10230|5638|6502|5562|100000
DAC|372|551|259|10234|5639|6493|5559|100000
both|374|554|256|10236|5638|6497|5558|100000
logss disc|100000|100000|100000|100000|0|100000|100000|100000
DAC disc|4730|28311|22521|100000|100000|100000|100000|100000
both disc|4730|28311|22521|100000|100000|100000|100000|100000
logss disc hamming|100000|100000|100000|100000|0|100000|100000|100000
DAC disc hamming|4730|28311|22521|100000|100000|100000|100000|100000
both discrete hamming|4730|28311|22521|100000|100000|100000|100000|100000

### MDAMB231_2

**Dataset**|**k =1**|**k=2**|**k=3**|**k=4**|**k = 5**|**k = 6**|**k = 7**|**k = 8**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
logss|245|363|190|2950|1256|1587|1279|100000
DAC|244|361|190|2950|1257|1585|1283|100000
both|244|363|190|2949|1256|1587|1282|100000
logss disc|100000|100000|100000|100000|0|100000|100000|100000
DAC disc|0|1936|778|93933|91341|95631|92695|100000
both disc|0|1936|778|93933|91341|95631|92695|100000
logss disc hamming|100000|100000|100000|100000|0|100000|100000|100000
DAC disc hamming|0|1936|778|93933|91341|95631|92695|100000

### MDAMB231_3

**Dataset**|**k =1**|**k=2**|**k=3**|**k=4**|**k = 5**|**k = 6**|**k = 7**|**k = 8**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
logss|344|533|262|10121|5597|6384|5453|100000
DAC|342|530|265|10119|5598|6375|5451|100000
both|343|530|263|10118|5597|6380|5453|100000
logss disc|100000|100000|100000|100000|0|100000|100000|100000
DAC disc|7060|17815|12915|100000|99994|100000|99979|100000
both disc|7060|17815|12915|100000|99994|100000|99979|100000
logss disc hamming|100000|100000|100000|100000|0|100000|100000|100000
DAC disc hamming|7060|17815|12915|100000|99994|100000|99979|100000
both discrete hamming|7060|17815|12915|100000|99994|100000|99979|100000

### MDAMB231_4

**Dataset**|**k =1**|**k=2**|**k=3**|**k=4**|**k = 5**|**k = 6**|**k = 7**|**k = 8**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
logss|227|336|170|2820|1196|1448|1149|100000
DAC|227|333|172|2821|1198|1447|1149|100000
both|227|334|171|2821|1198|1447|1149|100000
logss disc|100000|100000|100000|100000|0|100000|100000|100000
DAC disc|3|69|1|91812|90173|95881|93016|100000
both disc|3|69|1|91812|90173|95881|93016|100000
logss disc hamming|100000|100000|100000|100000|0|100000|100000|100000
DAC disc hamming|3|69|1|91812|90173|95881|93016|100000
both discrete hamming|3|69|1|91812|90173|95881|93016|100000


## Compare Replicates

### DAC discrete, k = 3 

| |**MDAMB231\_1**|**MDAMB231\_2**|**MDAMB231\_3**|**MDAMB231\_4**
:-----:|:-----:|:-----:|:-----:|:-----:
MDAMB231\_1|22521|0|11235|0
MDAMB231\_2|0|778|0|1
MDAMB231\_3|11235|0|12915|0
MDAMB231\_4|0|1|0|1

### DAC discrete, k =2 

| |**MDAMB231\_1**|**MDAMB231\_2**|**MDAMB231\_3**|**MDAMB231\_4**
:-----:|:-----:|:-----:|:-----:|:-----:
MDAMB231\_1|28311|0|15240|0
MDAMB231\_2|0|1936|0|62
MDAMB231\_3|15240|0|17815|0
MDAMB231\_4|0|62|0|69

*Same results for the other discrete datasets*

### Both, k = 3

| |**MDAMB231\_1**|**MDAMB231\_2**|**MDAMB231\_3**|**MDAMB231\_4**
:-----:|:-----:|:-----:|:-----:|:-----:
MDAMB231\_1|256|162|244|148
MDAMB231\_2|162|190|174|171
MDAMB231\_3|244|174|263|158
MDAMB231\_4|148|171|158|171

### Both, k = 5

| |**MDAMB231\_1**|**MDAMB231\_2**|**MDAMB231\_3**|**MDAMB231\_4**
:-----:|:-----:|:-----:|:-----:|:-----:
MDAMB231\_1|5638|1256|5580|1198
MDAMB231\_2|1256|1256|1256|1194
MDAMB231\_3|5580|1256|5597|1198
MDAMB231\_4|1198|1194|1198|1198

## Conclusions
Changing the number of clusters in training set from 4 to 2 does not increse the intersection of perturbations causing a shift to the normal cluster for the four replicates. Use the concatination of the raw datasets and 3 nearest neighbors with 4 custers in the training set because it gives more strigent results.

# FVS node values in training set

We are curious as to why the normal attractors cluster in 2 clusters and the cancerous clusters cluster into two clusters. We explored the activity of the FVS nodes in these attractors to determine if their variation could account for the clustering pattern.

**Table:** The Log2 Fold Change and P-value of FVS nodes from DESeq2 differentail expression analysis.

**Gene\_Symbol**|**MDAMB231/MCF10A FoldChange**|**pVal**
:-----:|:-----:|:-----:
AKT1|1.055452027|0.697701145
CTNNB1|-1.821171473|1.2659e-05 \**
FOXM1|3.398758511|1.90655e-05 \**
GSK3B|-1.853596375|0.000107609 \**
JUN|-1.672221872|0.281549501
MAPK1|-1.198183659|0.045203114
RELA|1.075617822|0.53606185
STAT3|1.167308955|0.429944633
AURKA|6.547791762|1.71696e-12 \**
TCF3|-1.332692592|0.078810701
PIAS1|-1.812271525|5.43419e-06 \**
HDAC3|-1.132226276|0.218909035

\** Significant at the 0.001 level

In MCF10A replicates, CTNNB1, GSK3B, and PIAS1 are significantly more expressed than in MDAMB231. However, this acitivty level of CTNNB1 and GSK3B does not agree with literature. Conversely, AURKA and FOXM1 are signficantly less expressed in MCF10A replicates than in MDAMB231 replicates.

**Table:** The normalized RNAseq expression data for FVS nodes in the eight experinental replicates.

**name**|**MCF10A\_1**|**MCF10A\_2**|**MCF10A\_3**|**MCF10A\_4**|**MDAMB231\_1**|**MDAMB231\_2**|**MDAMB231\_3**|**MDAMB231\_4**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
AKT1|10.87854288|11.12959373|10.84834298|11.09126581|11.00299793|11.10279088|10.97003065|11.08088504
CTNNB1|12.49892803|12.86679471|12.48924827|12.83456686|12.17006454|12.15239972|12.21129594|12.16066965
FOXM1|9.52307189|9.50516907|9.52347905|9.50130126|10.02164228|10.93597817|9.95200219|10.91678859
GSK3B|10.7007353|10.62804171|10.72389264|10.6917195|10.33503625|9.95142719|10.33347286|9.9496478
JUN|9.51122478|10.95592017|9.4903158|10.96094915|9.81710333|10.21395766|9.80478766|10.16384211
MAPK1|11.04388966|11.19875118|11.12124377|11.22272887|10.93552864|11.01103932|10.94906267|11.07718612
RELA|10.47203188|10.68921492|10.52993798|10.65811428|10.73675295|10.53768567|10.65865677|10.67072988
STAT3|10.56428801|10.96178244|10.96925717|11.0879189|11.16121217|10.91066701|11.16668464|10.91759214
AURKA|9.06755978|9.10139478|9.11889841|9.039134|10.07625999|11.02582441|10.15813787|11.02671988
TCF3|10.64874633|10.77559343|10.5523821|10.64619397|10.19490836|10.60056882|10.24625873|10.54881364
PIAS1|10.08320282|9.90076822|10.11744676|9.74628329|9.48901681|9.5292538|9.50232263|9.38705458
HDAC3|10.07136987|10.02308142|10.00478498|10.01184598|9.84842798|10.02732455|9.80683273|9.99109486

**Table:** Standard deviation of log steady-state expression of FVS nodes from the eight experimental replicates predicted by SFA.

**FVS Node**|**Standard Deviation Amoung MCF10A Replicates**|**Standard Deviation Amoung MDAMB231 Replicates**
:-----:|:-----:|:-----:
PIAS1|0.071345|0.02896
AKT1|0.096342|0.069411
CTNNB1|0.175762|0.015115
**JUN**|**0.435238**|0.11205
GSK3B|0.01627|0.107658
TCF3|0.042223|0.108971
MAPK1|0.061739|0.015611
**AURKA**|0.0252|**0.33436**
STAT3|0.082643|0.11887
RELA|0.04879|0.068684
HDAC3|0.020685|0.055916
**FOXM1**|0.014138|**0.330261**

There are other network nodes with larger standard deviations between replicates of the same cell line, such as MVD with a standard deviation of 0.534 among normal replicates, and ICAM1 with a standard deviation of 0.422 among cancer replicates that could also explain why they cluster in 4 groups.

# Perturbation frequency in 100,000 randomly generated perturbations

To ensure that we are capturing a realistic representation of all possible perturbation combinations, we examined the frequency of perturbation orientation for each FVS node in the 100,000 randomly generated initial states.

**Table:** Percent of perturbations where each FVS node is either knocked-in, knocked-out, or not changed.

**perturbation**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Knocked-in|33.426|33.083|33.249|33.389|33.268|33.455|33.306|33.411|33.28|33.318|33.488|33.382
Knocked-out|33.206|33.264|33.406|33.305|33.473|33.335|33.416|33.332|33.103|33.372|33.275|33.355
No Change|33.368|33.653|33.345|33.306|33.259|33.21|33.278|33.257|33.617|33.31|33.237|33.263



# Select normal perturbations

Using 3 nearest neihgbors and the combination of logss and DAC dataset, there are [157 perturbations](https://github.com/MadeleineGastonguay/gastonguay_compsysmed_labnotebook/blob/dev/_projects/project2/Network_Analysis/virtual_screening/successful_perturbations.txt) causing a shift to normal from all 4 replicates. All of these perturbations also triggered a shift to normal in the DAC dataset, and all but one (Perturb_079281) triggered the shift in the logss dataset.

<!---
both but not logss: Perturb_079281
logss but not both:  Perturb_037031
DAC bot not logss: Perturb_005343, Perturb_017420
logss but not DAC: Perturb_037031
DAC but not both: Perturb_005343, Perturb_017420
--->

The summary of the frequency of the orientation of each FVS node in the 157 perturbations is included in this table:

**perturbation**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Knocked-in|12.102|0|82.166|0|89.172|82.166|36.943|29.936|68.79|0|0.637|2.548
Knocked-out|58.599|68.153|7.006|64.968|1.274|6.369|42.675|31.847|7.006|68.79|57.962|52.229
No Change|29.299|31.847|10.828|35.032|9.554|11.465|20.382|38.217|24.204|31.21|41.401|45.223


The results that do not agree with literature is the upregulation of [CTNNB1](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0117097), [GSK3B](https://breast-cancer-research.biomedcentral.com/articles/10.1186/s13058-019-1125-0), and [HDAC3](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5611517/).

Literature evidence:
- *"higher expression of GSK3β correlated with poorer overall patient survival"*
- *"GSK3β inhibitors were identified as EMT inhibitors"*
- *Stable knockdown of β-catenin significantly suppressed migration of MDA-MB-231*
- **BUT:** *[CTNNB1 not as highly expresesed in MDAMB231](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4529819/) and [here](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0117097)* when comapred to other tnbc cell lines
- *Inhibiting histone Deacetylations is a potential therapeutic strategy*

**I wanted to eamine the results from 4 and 5 nearest neighbors to see if it included more perturbations that did not require the activation of CTNNB1  and GSK3B.**

When examining 4 nearest neighbors, we see 2464 perturbations trigger a shift to the normal cluster. The frqeuency of their perturbations can be seen below:

**perturbation**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Knocked-in|20.698|0|57.752|0|69.44|57.021|20.333|34.253|48.539|11.891|55.032|1.136
Knocked-out|47.727|67.695|15.828|68.425|14.245|18.588|52.638|33.076|20.049|50.487|12.459|51.502
No Change|31.575|32.305|26.42|31.575|16.315|24.391|27.029|32.67|31.412|37.622|32.508|47.362

When examining 5 nearest neighbors, we see 3263 perturbations trigger a shift to the normal cluster. The frqeuency of their perturbations can be seen below:

**perturbation**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Knocked-in|23.108|0|61.048|0|66.289|52.927|19.43|35.887|48.452|14.097|55.777|2.053
Knocked-out|45.02|67.729|14.741|68.342|15.538|20.686|50.322|31.934|20.104|48.851|12.994|50.475
No Change|31.873|32.271|24.211|31.658|18.173|26.387|30.248|32.179|31.443|37.052|31.229|47.472


I think we are seeing that we need to upregulate GSK3B and CTNNB1 because in the initial condition for MCF10A, they are upreagulated compared to MDAMB231 (see logfc above). 

It has been observed that activity levels of CTNNB1 are lower in MDAMB231 than in other TNBC cell lines. This makes sense because CTNNB1 regulates cell proliferation and CL tumors have low proliferation rates. However, there is still evidence that inhibition of CTNNB1 in MDAMB231 cell lines decreases rates of metastasis and tumorigenesis, so it still does not make sense to activate it as a therapeutic target.

I'm not sure why we haven't seen these results before - it's likely due to the way that we are now simulating knock-ins and knock-outs and classifying perturbations. Instead of using the basin of attraction as the training set, we are using the attractor itself. This may be too restrictive when classifying attractors from perturbations. However, we have seen the SFA cannot accurately predict attractors from random initial conditions.

Out of the 157 perturbations that trigger the shift to the normal phenotype in all four replicates, there are two that do not require the activation of GSK3B and CTNNB1:

**perturbation**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Perturb_003761|Knock-out|Knock-out|No Change|Knock-out|No Change|Knock-in|Knock-out|Knock-out|Knock-in|Knock-out|Knock-out|Knock-out
Perturb_036358|Knock-out|No Change|No Change|Knock-out|No Change|Knock-in|Knock-out|No Change|Knock-in|Knock-out|No Change|Knock-out

Perturb_003761 requires the pertubration of 10 of the 12 FVS nodes and Perturb_036358 requires perturbation of 7 of the 12 FVS nodes.

### Exploring the number of nodes that must be perturbed to trigger the shift.
Out of curiosity, I wanted to see if we had to perturb a large fraction of the 12 FVS nodes because we are not activating GSK3B and CTNNNB1, or if it is the case that most of the preturbations that trigger the shift require the perturbation of many FVS nodes.

- 1 pertubration with 6 perturbed nodes
- 35 pertubrations with 7 perturbed nodes
- 36 pertubrations with 8 perturbed nodes
- 37 pertubrations with 9 perturbed nodes
- 34 pertubrations with 10 perturbed nodes
- 12 pertubrations with 11 perturbed nodes
- 2 pertubrations with 12 perturbed nodes

Summary Stats:

**Min.** | **1st Qu.**|**Median**|**Mean** | **3rd Qu.**|**Max.**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
6.000|8.000|9.000|8.713|10.000|12.000  

## Are there other normal perturbations that don't require activation of GSK3B and CTNNB1?
Because we only have a sample of 100,000 perturbations out of the 531,441 possibilities, I wanted to lock some of the FVS nodes with consistent perturbation patterns in the parturbations triggering a shft to normal and find all possible perturbations with those constraints. 

I will simulate new perturbations fixing:
- CTNNB1 and GSK3B as no change
- RELA and FOXM1 as knock-out
- PIAS1 as knock-in

And all possible combinations for the other 7 nodes (2187 total). This is a concern because the two above perturbations (Perturb_003761 and Perturb_036358) were included in this list of perturbations and triggered a shift to normal in all 4 replicates the first time I ran knn. This time, they only trigger it in one of the replicates. One perturbation triggerse the shift in 3/4 replicates:

**perturbation**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Perturb_1216|Knock-out|Knock-out|No Change|Knock-out|No Change|Knock-in|Knock-out|Knock-out|Knock-in|Knock-out|Knock-out|No Change

This is the same perturbation as Perturb_003761, but with no change applied to TCF3 instead of kncking it out.

### Elucidating why GSK3B and CTNNB1 must be upregulated

I wanted to determine if the reason we are seeing the need to upregulatee GSK3B and CTNNB1 is because of an issue with the network topology, or because of the afore mentioned issue of the dicrepencies in expression level at initial conditions. To do so, I simulated the attractors for MDAMB231 and MCF10A, but swapped initial conditions for the FVS nodes that didn't agree with literature: GSK3B and CTNNB1. Then, I re-calssified the same 100,000 perturbations of FVS nodes using knn. 9 perturbations triggered the shift from normal to cancer in all 4 cancerous replicates. The frequency of their perturbation orientation is below:

**perturbation**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Knocked-in|0|0|0|0|0|100|0|11.111|100|0|0|0
Knocked-out|100|77.778|88.889|66.667|33.333|0|88.889|55.556|0|44.444|77.778|55.556
No Change|0|22.222|11.111|33.333|66.667|0|11.111|33.333|0|55.556|22.222|44.444

This tells me that our results are very sensitive to the initial conditions of the reference attractors.

<!--

To do so, I simulated the attractors for MDAMB231 and MCF10A, but swapped initial conditions for the FVS and source nodes that didn't agree with literature: GSK3B, CTNNB1, PAK2, PPP4C, PRPF4, and PRMT5. Then, I re-calssified the same 100,000 perturbations of FVS nodes using knn. The 18 perturbations that tiggered a shift to normal in all four cell lines have the frequency below:


**perturbation**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Knocked-in|0|0|0|0|0|100|0|33.333|100|0|0|0
Knocked-out|83.333|66.667|72.222|61.111|50|0|88.889|33.333|0|55.556|83.333|61.111
No Change|16.667|33.333|27.778|38.889|50|0|11.111|33.333|0|44.444|16.667|38.889

Here, we see that CTNNB1 and GSK3B do not need to be upregulated, which is what we would expect.

I did the same experiment only flipping CTNNB1 and GSK3B (excluding source nodes), and found similar results. 9 perturbations triggered the shift from normal to cancer in all 4 cancerous replicates.

**perturbation**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Knocked-in|0|0|0|0|0|100|0|11.111|100|0|0|0
Knocked-out|100|77.778|88.889|66.667|33.333|0|88.889|55.556|0|44.444|77.778|55.556
No Change|0|22.222|11.111|33.333|66.667|0|11.111|33.333|0|55.556|22.222|44.444

This tells me that our results are very sensitive to the initial conditions of the reference attractors.
--->

# Looking For similar trends in literature for GSK3B and CTNNB1

[Here](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE75168), we observe the same trend in GSK3B but not in CTNNB1 from normalized counts:



**name**|**logfc**|**p-value**|**MCF10A\_1**|**MCF10A\_2**|**MCF10A\_3**|**MDAMB231\_1**|**MDAMB231\_2**|**MDAMB231\_3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
GSK3B|-1.135526001|1.01E-05|1788.99|1944.36|1254.37|775.35|741.93|751.92
CTNNB1|1.559422991|2.39E-14|8479.24|8861.55|7088.68|23417.67|26209.64|22368.38

From [RPKM data](http://lincs.hms.harvard.edu/db/datasets/20348/main), we see the same trend in GSK3B but not CTNNB1 

*there is only one replicate for MDA-MB-231 and two replicates for MCF10A which were averaged together*

name |MCF10A|	MDAMB231
:-----:|:-----:|:-----:
GSK3B	| 4.628451756 |	3.741966099
CTNNB1|	6.769542581	|7.121709815

# Literature search these perturbations:
- = Knock-out, + = Knock-in, nc = no change

**name**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Perturb\_006159|-|-|+|nc|+|+|nc|nc|+|nc|nc|nc
**Perturb\_036358**|**-**|**nc**|**nc**|**-**|**nc**|**+**|**-**|**nc**|**+**|**-**|**nc**|**-**
Perturb\_003761|-|-|nc|-|nc|+|-|-|+|-|-|-
Perturb\_007217|-|nc|+|-|nc|+|+|nc|+|nc|nc|-
Perturb\_015436|-|-|+|-|nc|nc|+|nc|+|-|-|nc
Perturb\_020657|nc|-|+|nc|+|-|+|nc|nc|-|-|-
Perturb\_031922|nc|-|+|nc|+|nc|+|nc|-|-|-|nc


*If HDAC3 is left unchanged, JUN must be activated

**Recall:**
The summary of the frequency of the orientation of each FVS node in the 157 perturbations is included in this table:

**perturbation**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Knocked-in|12.102|0|82.166|0|89.172|82.166|36.943|29.936|68.79|0|0.637|2.548
Knocked-out|58.599|68.153|7.006|64.968|1.274|6.369|42.675|31.847|7.006|68.79|57.962|52.229
No Change|29.299|31.847|10.828|35.032|9.554|11.465|20.382|38.217|24.204|31.21|41.401|45.223


AURKA:
- https://www.jbc.org/content/early/2016/09/20/jbc.M116.738666.full.pdf
    - inhibition of AURKA by BET leads to apoptosis or senscence in TNBC
- AURKA promotes stemness and breast cancer metastases
    - https://breast-cancer-research.biomedcentral.com/articles/10.1186/s13058-018-1020-0
- **not many studies done on its direct inhibition**

PIAS1:
- 	https://www.researchgate.net/publication/270907408_A_novel_role_for_the_SUMO_E3_ligase_PIAS1_in_cancer_metastasis
     - regulator of EMT, metastasis and stemness
     - it's inhibition increases metastesis
- https://www.nature.com/articles/srep17663
    - PIAS proteins can deregulate the activity of STAT3
- **cannot find evidence of its activation being studied**

FOXM1 inhibition:
- https://www.ncbi.nlm.nih.gov/pubmed/30572639
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6061948/
    - it's a regulator of EMT, invasion, and metastasis
- https://europepmc.org/article/pmc/pmc6254995
    -  FOXM1 inhibition significantly suppressed MDA‑MB‑231 cell tumorigenesis in vivo
    - inhibition of FOXM1 leads to reversal of EMT

CTNNB1 does not match literature
- https://www.ncbi.nlm.nih.gov/pubmed/27959422
    - it's inhibition reverses EMT
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6144355/pdf/ol-16-04-4984.pdf
    - activation of WNT/CTNNB1 pathway is associated with poor prognosis and metastasis

GSK3B is against literature
- regulator of EMT and CSC
- explored as a therapeutic target
- its inhibition decreases EMT and stemness
- https://digitalcommons.library.tmc.edu/utgsbs_dissertations/806/
-	https://breast-cancer-research.biomedcentral.com/articles/10.1186/s13058-019-1125-0
- https://link.springer.com/article/10.1186/s13058-019-1125-0
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6721324/


HDAC3 inhibition has been tested as a therapeutic strategy

- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6428526/
    - EZH2 and HDAC inhibition shall co-operate to induce apoptosis in TNBC cell line MDA-MB-231
- https://link.springer.com/article/10.1007/s13346-018-0551-3
    - The histone deacetylase inhibitors (HDACi) are new class of anticancer agents that stimulate differentiation/apoptosis and inhibit the proliferation of cancer cells by inhibiting the function of HDACs
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6144355/pdf/ol-16-04-4984.pdf
     - A preclinical study
confirmed a histone deacetylase inhibitor could partially reverse EMT 

AKT inhibition evidence:
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6785914/
- https://www.annalsofoncology.org/article/S0923-7534(19)31239-6/fulltext
    - helpful in patients with AKT dysregulation
- https://www.karger.com/Article/Fulltext/455821
- https://www.oncotarget.com/article/18166/text/
    - supresses CSC formation in BC when targeted with HSF1 
- https://link.springer.com/article/10.1186/s12943-015-0421-2
     - PDL1 is activated by PI3k/AKT signaling, and its inhibition has been shown to reverse EMT, so inhibiting AKT1 may have a simil
     ar effect

STAT3 inhibition:
- https://www.nature.com/articles/srep17663
    - Can reverse EMT
- 	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6518732/pdf/13046_2019_Article_1206.pdf
    - 	Several inhibitors of STAT3 have been tested and shown to inhibit tumor growth/migration and stem cell properties
    - regulates Stemness, proliferation, migration, EMT


TCF3 inhibition:
- https://www.researchgate.net/publication/232610667_Control_of_Breast_Cancer_Growth_and_Initiation_by_the_Stem_Cell-Associated_Transcription_Factor_TCF3
    - regulates Stem cells, cell growth
    - its inhibition reduces tumor formation

MAPK1:
- while there is evidence that inhibtion of the MAPK pathway is a potential therapeutic target, there is not evidence of MAPK1 itself as a target
    - makes sense that we see it split between the three perturbations
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6827047/
    - often times MAPK inhibition leads to the activation of compensatory feed-back loops, so combinatorial interventions are necessary

RELA: 
- https://erc.bioscientifica.com/view/journals/erc/26/6/ERC-19-0087.xml
    - inhibiting NFKB pathway may increases sensitivity to endocrine care in TNBC


## Depmap Essentiality of Genes for MDA-MB-231

As the goal is to trigger tumor reversion and not cell death, we want to make sure that we are not knocking out any genes necessary for cell survival. DEPMAP provides a Gene Effect score for each gene on a cell line denoting the dependency of the cell line on said gene. Cell lines aree dependent on genes with a gene effect score less than -1. The gene effect score of our FVS nodes are below:

[AURKA:](https://depmap.org/portal/gene/AURKA?tab=dependency&dependency=Avana&characterization=expression) -0.89 

[FOXM1:](https://depmap.org/portal/gene/FOXM1?tab=overview&dependency=Avana&characterization=expression) -0.145 

[AKT1:](https://depmap.org/portal/gene/AKT1?tab=overview&dependency=Avana&characterization=expression) 0.145 

[JUN:](https://depmap.org/portal/gene/JUN?tab=overview&dependency=Avana&characterization=expression) -0.299 

[RELA:](https://depmap.org/portal/gene/RELA?tab=overview&dependency=Avana&characterization=expression) - 0.28

[STAT3:](https://depmap.org/portal/gene/STAT3?tab=overview&dependency=Avana&characterization=expression) 0.246

[TCF3:](https://depmap.org/portal/gene/TCF3?tab=overview&dependency=Avana&characterization=expression) 0.149

[MAPK1:](https://depmap.org/portal/gene/MAPK1?tab=overview&dependency=Avana&characterization=expression) -0.522

[HDAC3](https://depmap.org/portal/gene/HDAC3?tab=overview&dependency=Avana&characterization=expression) has score -1.31 --> wouldn't want to inhibit it 

[GSK3B](https://depmap.org/portal/gene/GSK3B?tab=overview) -0.0388

[CTNNB1](https://depmap.org/portal/gene/CTNNB1?tab=dependency&dependency=Avana) : -0.1686

[PIAS1:](https://depmap.org/portal/gene/PIAS1?tab=dependency&dependency=Avana) -0.323

The only FVS node that MDA-MB-231 upon which exhibits dependncy (Esentiality score \< -1) is HDAC3. Thus, perturbations that require its inhibition will not be considered for expermiental validaion.

## Conclusions
More experimentation needs to be done with different FVS sets and including perturbations of the source nodes. Running virtual screenings using RNAseq data from the additionally study would be another control to identify successful perturbations. As of now, I would prioritize **Perturb\_036358** for experimental validation because only 7 nodes need to be perturbed, and it does not require activation of GSK3B or CTNNB1.
