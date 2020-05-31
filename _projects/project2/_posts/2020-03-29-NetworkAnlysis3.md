---
layout: post
title: "Network Analysis"
date: "2020-03-29"
author: maddie
tags:
 - project02
 - static_network
---

## Objective
After running our SFA experimentation on the T-LGL Leukemia network, we realized we need to modify our network analysis pipeline. The randomly simulated SFA attractors cannot be associated to a phenotype by kmeans clustering. Instead, we will try to run knn with the 4 MCF10A and 4 MDA-MB-231 attractors as training sets. We will still "discretize" in the same way: positive values are represented as 1, negative value are represented as -1, and zeroes remain 0.

The analyses were all done on six datasets:
1. Log steady state
2. DAC
3. Combination of 1+2
4. Discrete log steady state
5. Discrete DAC
6. Combination of 4+5


## Virtual Screening
We have modified the SFA code to fix FVS nodes in a perturbation instead of just initializing them. We have 12 FVS nodes resulting in $3^{12} = 531441$ possible perturbations. So far, we have only examined 100,000 of these perturbations. We have only considered perturbations of the FVS, not the whole FC.

Previously, we used the average expression level from MDA-MB-231 as the basal state to apply perturbations to. Now, we will use the four replicates of MDA-MB-231 as separate basal conditions and apply perturbations to all 4 basal states. This will act as 4 "experimental" replicates of our perturbations. Perturbations must result in a shift towards normal for all four replicates to be considered successful.

## CAVEAT
**In the analysis described in this post, the initial conditions for MDA-MB-231 were discretized versions of the normalized RNAseq expression data. Knock-ins were fixed to 1, knock-outs were fixed to -1, and no changes were accidentally fixed to 0. Thus, the results of this anlaysis may be interseting but are pretty much useless. If you are still interested in the results from this anlaysis conintue reading this post! See [SFA Initializations]({{ site.baseurl }}{% post_url 2020-03-29-NetworkAnlysis3 %}) post for a rationale as to why we should be using continuous values for the initial conditions of SFA, and see [Final Network Anaysis]({{ site.baseurl }}{% link _projects/project2/_posts/2020-04-05-NetworkAnlysis-final.md %})  for results of virtual screenings using continuous initial conditions and properly simulated perturbations.**

***

## K-nearest Neighbors Classifier
Using the 8 experimental attractors as a training set, we classified the 100,000 attractors resulting from FVS perturbations on all 6 datasets. Two questions arose during this:
1. What is the optimal number of neighbors?
2. What dataset should we use for the analysis?

When chosing the optimal number of neighbors, I considered values of 3, 5, and 7. For most of the datasets, the first two neighbors of all the perturbations were MDA-MB-231 attractors, so chosing 3 nearest neighbors resulted in no normal attractors. With a knn of 7, all four normal attractors will be in nearest neighbors, we will prioritize based on distance.

**For datasets 1-3 (The Raw Values), there were never any perturbations calssified as normal, regardless of the number of neighbors.** Thus, I only explored discrete datasets.

#### Exploring Distance Metrics

The default distance metric for knn is euclidean distance. However, knn can be run using different distance metrics. For the discrete datasets only, I tested knn using the hamming distance between the perturbations and the training set. [Choo and Cho](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6739335/pdf/41598_2019_Article_49571.pdf) use Hamming distnace to determine the boundary of the basin of attraction for an attractor of a Boolean model. States with larger hamming distances are further away from the attractor than states with smaller hamming distances.

**Test case: MDAMB231_1**

Dataset: **Log steady state discrete**
- No normal perturbations regardless of the distance metric used

Dataset: **DAC discrete** (k = 7)
- euclidean distance gave 93,420 normal
- hamming distance gave 97,467 normal
- 93283 attractors classified by normal as both

Dataset: **both discrete** (k = 7)
- euclidean distance gave 42,319 normal
- hamming distance gave 13,338 normal
- everything classified as normal by hamming distance was also classified as normal using hamming distance 


I compared the results between knn on the discretized logss and DAC and knn on just the discretized DAC. Regardless of the distane metric used, eveything that is classified as normal with the discrete both is also classified as normal with the discrete DAC datatset. **Thus, it makes sense to use the discrete both dataset for our anlysis because it gives more stringent results.**

For the both discrete dataset, using the hamming distance is more stringent in determining normal perturbations. Therefore, I think we should use it going forward.

### Perturbations from MDAMB231_1

**Test**: I used the both discrete dataset with 7 nearest neighbors to identify potential normal perturbations. Then, I prioritized those perturbations that have the four MCF10A attractors closest. These can further be prioritized based on the distance between the perturbation and the normal attractors.

When doing this with perutrbations from MDAMB231_1, we have 3062 normal perturbations.

FVS nodes from these normal perturbations: *see excel sheet*

Compared to FVS nodes in MDAMB231 and MCF10A basal states: *see excel sheet*

**name**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
one|1433|792|1597|30|685|1052|393|1289|1166|1280|2768|11
zero|799|1163|302|549|713|1007|1088|900|939|617|294|66
negone|830|1107|1163|2483|1664|1003|1581|873|957|1165|0|2985

### Comparing Knn results from different MDA-MB-231 Replicates

#### Both Discrete:

Number of perturbations classified as normal using knn with **7** nearest neighbors on both discrete:

| Replicate  | Number of Normal Pertrubations |
|------------|--------------------------------|
| MDAMB231_1 | 13,338                          |
| MDAMB231_2 | 1,037                           |
| MDAMB231_3 | 19,868                          |
| MDAMB231_4 | 3,199                           |

Number of perturbations classified as normal using knn with **5** nearset neighbors on both dsicrete:

| Replicate  | Number of Normal Pertrubations |
|------------|--------------------------------|
| MDAMB231_1 | 5,121                        |
| MDAMB231_2 | 0                           |
| MDAMB231_3 | 14,189                         |
| MDAMB231_4 | 69                           |

#### DAC Discrete:

Number of perturbations classified as normal using knn with **7** nearest neighbors in DAC discrete

| Replicate  | Number of Normal Pertrubations |
|------------|--------------------------------|
| MDAMB231_1 | 97,467                        |
| MDAMB231_2 | 97,503                           |
| MDAMB231_3 | 99,980                         |
| MDAMB231_4 | 99,989                           |

Number of perturbations classified as normal using knn with **5** nearest neighbors on DAC dsicrete:

| Replicate  | Number of Normal Pertrubations |
|------------|--------------------------------|
| MDAMB231_1 | 69,498                        |
| MDAMB231_2 | 90,403                           |
| MDAMB231_3 | 98,571                         |
| MDAMB231_4 | 93,820                           |


#### Comparing the number of perturbations classified as normal from multiple replictes

Using Both Discrete, 7 Nearest Neighbors

|  | MDAMB231_1 | MDAMB231_2 | MDAMB231_3 | MDAMB231_4 |
|------------|------------|------------|------------|------------|
| MDAMB231_1 | 13338 | 1037 | 13338 | 671 |
| MDAMB231_2 |  | 1037 | 1037 | 273 |
| MDAMB231_3 |  |  | 19868 | 768 |
| MDAMB231_4 |  |  |  | 3199 |


**There are 273 perturbations classified as normal from all 4 replicates**

**name**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
one|168|40|117|0|22|108|0|107|130|46|273|0
zero|73|102|2|7|33|89|141|82|82|38|0|0
negone|32|131|154|266|218|76|132|84|61|189|0|273


## Kmeans
Test case on MDAMB231_1 discrete both dataset.

There is no k that separates the MDA-MB-231 and the MCF10A attractors completely, but kmeans on the discrete 2n-tuples clusters MCF10A 1-3 together and the other references together. 

Comparing these results to the knn results, there is no overlap between the attractors that cluster with the MCF10A and the prioritized normal perturbations determined by the number of normal nearest neighbors. There is overlap between the perturbations in the cluster and the perturbations in the list of 7 nearest neighbors but not 5 nearest neighbors.

**name**|**AKT1**|**AURKA**|**CTNNB1**|**FOXM1**|**GSK3B**|**HDAC3**|**JUN**|**MAPK1**|**PIAS1**|**RELA**|**STAT3**|**TCF3**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
one|2904|2848|2881|0|2927|2871|2442|2864|2901|2847|4925|3738
zero|2865|2937|2833|2451|2825|2889|3695|2851|2862|2866|3709|4896
negone|2865|2849|2920|6183|2882|2874|2497|2919|2871|2921|0|0

Comparing the orientation of the FVS nodes for these "normal" perturbations as opposed to the perturbations classified as normal by knn, there does not appear to be a common orientation for the majority of these FVS nodes. In the perturbations classified as normal by knn, we do see a pattern for several FVS nodes.


## Examiming Source nodes

Perturbing the source nodes that are clearly different between the MDAMB231 basal states and the MCF10A basal states moves the attractors closer to the normal attractors. However, there are 17 such nodes, and we cannot target 17 source nodes as 12 FVS nodes, so I need to systematically determine which source nodes should be perturbed in concert with several FVS nodes.

*See excel sheet*

