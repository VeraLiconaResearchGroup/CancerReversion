---
layout: post
title: "Planning for Boolean Network Construction"
date: "2019-05-16"
author: maddie
tags:
 - project01
 - boolean_network
 - SURF
---

## Objective
To lay out the steps to take and identify objectives for the next portion of this project.  
*~~ After finishing Static Network construction and running virtual screenings~~*

## Questions
1. Are the nodes we include in this model the same nodes from the static network?
2. Will we use weighted sums?
3. How do we classify the attractor states as cancerous or normal like?

# Game Plan

1. Write Boolean equations
  - train with time series phosphoproteomics
2. Convert the Boolean operator’s equation based on biological action mechanisms into **weighted sum logics**
  - **NOTE:** Cho does this in his Boolean model for Colorectal cancer, but it is not necessary.
  - **What it is:** Defines both the basal node states and node relationships quantitatively as weights.
  - **Purpose:** It's difficult to define node states and adjust logic based of experimental data because we cannot adjust values quantitatively, so weighted sums gives us a way to do that.
  - **How:** Give an input to each node via a weighted sum vector $W_S = M_C \cdot V^t+V_B$. Where $M_C$ is the connectivity matrix and its entities are determined from the logical equations. $V^t$ is a vector of each nodes' state at time t, and $V_B$ is a vector of each nodes' basal state determined from gene expression data. Mutational data can be incorporated at this step by altering the basal level of nodes. Then, the next state of the node is determined by:
  <p align = "center">
  $$ V^{t+1}_ i =
  	\begin{cases}
  		1 & (W_S)_ i > 0 \\
  		V^t_i & (W_S)_ i = 0 \\
  		0 & (W_S)_ i <0
  	\end{cases}
  $$
</p>

3. Run synchronous updating
4. Validate Model
  - Need to find CRISPR data
5. Estimate attractor landscape by investigating the results of 100,000 randomly sampled initial states
  - Classify attractor states with normal like score?
6. Node perturbation analysis
  - Activation
  - Inhibition
  - Restoration

## Exploratory Model
I looked into the R package [BoolNet](https://cran.r-project.org/web/packages/BoolNet/BoolNet.pdf) to see if I could use it for the construction of this model.
From what I've concluded, if I write the model as an SBML file, BoolNet can easily read it in, predict attractor states, and run perturbation analyses.

```{R}
library("BoolNet")
library("XML")

mod2 <- loadSBML("Toy_Model_2.xml", symbolic = FALSE)

print(getAttractors(mod2))

perturbNetwork(mod2, perturb = “transitions”)
```

This is the output for get attractors:
<div style="text-align:center" markdown="1">
![alt text]({{ site.baseurl }}\_assets\images\Example_Boolean_Model.png)  
</div>

Alternatively, I have all the matlab scripts from the Cho paper in which they implemented weighted sums so I could adapt them to our model.
