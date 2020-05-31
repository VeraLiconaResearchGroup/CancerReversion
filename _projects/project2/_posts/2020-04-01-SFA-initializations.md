---
layout: post
title: "SFA Initializations"
date: "2020-04-01"
author: lauren
tags:
 - project02
 - SFA
---


# Purpose
The purpose of this analysis  is to 
1. evaluate if we should discretize normalized expression RNA-seq values before running SFA.
2. determine how we should apply knock-ins, knock-outs, or no change in SFA

## How did we get here
We have been discretizing the normalized expression RNA-seq values (normexp) for performing SFA. Then, we have used values of -1,0,or 1 when performing random initializations for attractor landscape simulation, and FC node virtual screenings.
<br><br>
****
In SFA, the authors say "We assigned 1 and −1 as the values of basal activities for input stimulation and perturbation, respectively." `***`


`***` Please note that in Signal flow Control, the authors say "To implement such inhibition in the signal fow analysis, we set the basal activity of each control target candidate to −10." They do not say what they do for activation
****
<br><br>
So, we discretized because
1. The ranges for the normexp were widely scattered in some datasets. 
2. We would not know how to consistently apply a knock-in or knock out
   - for example, if the normexp of node x was 2.5, but the normexp of node y was .8, applying the value 1 to indicate knock-in would be relatively knocking down the activity of node x
3. we introduced the third term of 0, because if a node's initial condition was 0, we would have to leave it at 0 for there to be no change in its activity.
   - now thinking about this, we could have just somehow indicated no change for any node when coding, but this did not dawn on me until yesterday
4. We did not have -1 when we discretized the normal expression because 0 was to represent a "present level of expression", while 1 represented "high expression".
5. This allowed for -1 to represent "knock-out" of a node, which was not something that would occur naturally in a cell. 


## Terminology Note
1. node perturbation= transient inhibition (setting initial state=-1)
2. node stiulation=transiet activation (setting initial state=1)
3. node knock-out= permanent inhibition (fixing node to OFF, either -1 or 0 deciding on what we want to do)
4. node knock-in=permanent activation (fixing node to ON, either 1 or whatever we decide)

# SFA paper examples

To understand how they simulated the data in SFA paper, we attempted to reproduce the results in 3 networks
<br>

***
## Borisov et al., 2009
![borisov network]({{ site.baseurl }}\_assets\images_proj2\borisov.png)
<br>
model based on ODE of EGFR and Insulin Signaling

### Determining Initial Conditions
After much sleuthing, we determined that there were four initial conditions tested on this network

<div class="datatable-begin"></div>

| initial|condition 1 | initial|condition 2 | initial|condition 3 | initial|conditon 4 |
| :-------: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| node | value | node | value | node | value | node | value |
| EGF | .0001 | EGF | 1 | EGF | .0001 | EGF | 1 |
| I | .0001 | I | .0001 | I | 1 | I | 1 |

<div class="datatable-end"></div>

### Why these initial conditions?
These were based on Borisov et al.'s original ODE study, where they simulated the dynamics of the system with those values.

***
Lee and Cho then performed double perturbations (-1) to network nodes and compared the DAC between the initial condiitions and the perturbation log steady state values.


![perturbation chart]({{ site.baseurl }}\_assets\images_proj2\b_p.png)

We confirmed these results for initial condition three, and perturbation of RasGAP and IRS

|Node|Initial Condition|Perturbation|DAC (pert - initial)|
|:---|:---:|:---:|:---:|---:|
|AKT|2.12E-03|-2.01E-03|-0.00412588|
|EGF|5.00E-05|5.00E-05|0|
|EGFR|2.50E-05|2.50E-05|0|
|ERK|1.07E-03|1.17E-02|0.01063707|
|GAB1|8.07E-03|8.70E-04|-0.00719953|
|GAB1_SHP2|1.80E-03|1.94E-04|-0.00160986|
|GAB1_pSHP2|6.75E-03|5.66E-03|-0.00108952|
|GS|6.20E-03|-5.57E-02|-0.06187185|
|I|5.00E-01|5.00E-01|0|
|IR|2.50E-01|2.50E-01|0|
|IRS|3.94E-02|-4.66E-01|-0.50506128|
|IRS_SHP2|1.14E-02|-1.34E-01|-0.14579863|
|MEK|2.13E-03|2.34E-02|0.02127415|
|PDK1|5.46E-03|-5.18E-03|-0.01063829|
|PI3K|3.78E-02|-3.59E-02|-0.07370425|
|PIP3|1.89E-02|-1.79E-02|-0.03685212|
|RAF|4.26E-03|4.68E-02|0.0425483|
|RAS|-5.83E-03|1.39E-01|0.14447419|
|RasGAP|2.27E-02|-4.48E-01|-0.47050658|
|SFK|4.42E-02|4.42E-02|0|
|SHC|4.72E-06|4.72E-06|0|
|mTOR|7.49E-04|-7.10E-04|-0.00145872|


**Conclusions**
<br>
Initial conditions in this model were selected based on the previously known information. The initialized nodes were source nodes. These conditions were between .0001 and 1. A perturbation to a node was modeled as a -1

## Schliemann 2011 ODE model
![schliemann network]({{ site.baseurl }}\_assets\images_proj2\schliemann.png)
<br>
model based on ODE of TNF signaling for apoptosis

### Determining Initial Conditions
For this network, there were varied initial conditions for node TNF

|initial condition 1| |initial condition 2|| initial condition 3|| initial conditon 4||initial conditon 5||
|:-------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|-------------------:|
|node|value|node|value|node|value|node|value|node|value|
|TNF |0.02|TNF |0.2|TNF |2|TNF |20|TNF |200|

### Why these initial conditions?
These were based on the original ODE study, where they simulated the dynamics of the system with those values.

***
Lee and Cho then performed double perturbations (-1) to network nodes and compared the DAC between the initial condiitions and the perturbation log steady state values.

We performed a similar analysis as above, and could reproduce the results for initial condition 5, and perturbation of NFkB and A20


**Conclusions**
<br>
Initial conditions in this model were selected based on the previously known information. The initialized node is a source node. These conditions were between .02 and 200. A perturbation to a node was modeled as a -1. However, this does not address what would occur if you were to stimulate a node

## Nelander 2008 Perturbation Biology model

![nelander network]({{ site.baseurl }}\_assets\images_proj2\nelander.png)
<br>
model based on ODE of EGFR Signaling

### Determining Initial Conditions
While the initial conditions for this network were slightly unclear, by comparison with the original publication, and then simulation of results, we believe the initial condition is EGFR=-1


***
Lee and Cho then performed double perturbations (-1) to network nodes and compared the DAC between the initial condiitions and the perturbation log steady state values.

We performed a similar analysis as above, and could reproduce the results for initial EGFR=-1 and perturbations to p-MEK and PI3K.


**Conclusions**
<br>
Initial conditions in this model were selected based on the previously known information. **Do note that EGFR is not a source node.** These conditions were -1 A perturbation to a node was modeled as a -1. However, this does not address what would occur if you were to stimulate a node.


# 231 and 10A Data
We wanted to see the spread of normexp for network nodes 

![histo](./histo.png)
|Min.|1st Qu.|Median|Mean 3rd Qu.|Max.|
|:--|:--:|:--:|:--:|--:|
|2.950| 8.779| 9.832| 9.693|10.886|19.362|


***
## Why did AKT look weird?
Yesterday, AKT1 when discritized was 1 and 0 in half of the 10A attractors, and half of the 231 attractors
We investigated the normexp for AKT1
![akt1]({{ site.baseurl }}\_assets\images_proj2\akt1.png)

LogFC=1.055452
pvalue=0.6178509

So, AKT1 is not highly differentially expressed, which explains the inconsistencies between biological replicates.



### Some overall conclusions
1. In SFA, they only initialized nodes they had known values for, or based on literature
2. Continuous numbers for initializations still have the correct DAC in teir examples


### Questions to Answer
1. Will we discretize? If so, how?
2. How will we intialize a network?
3. How will we apply knock-ins or knock-outs? What values will we set the nodes to?

# Conclusions from our Discussion

1. simulating knock-ins: across the experimental undesired state normalized expression values, take 2x the average expression
2. Attractor Landscape: values across ranges of all experimental conditions
3. histogram spread of normexp is useful