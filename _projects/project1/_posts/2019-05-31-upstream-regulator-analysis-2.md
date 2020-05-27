---
layout: post
title: "Upstream Regulator Analysis Take Two"
date: "2019-05-31"
author: maddie
tags:
 - project01
 - static_network
 - TRASPATH
---

# Goal
To identify master regulators upstream of the transcription factors.

## Context Genes as All Proteins Present
We ran the GeneXplain workflow **"Master regulators with context genes and weighting"** using the list of expressed proteins as context genes, weighted by their intensity. After filtering for a Z-score > 1.5 and an FDR < 0.05, MRs were compared to protein expression data. This resulted in 68 MRs covering all 8 [transcription factors]({{ site.baseurl }}{% post_url  2019-04-15-transcription-factor-analysis %}).

## Context Genes as SOC
As an exploratory analysis, we ran the same pathway but only using the SOC genes with protein intensity weighting, as we usually do. This means that those SOC genes without protein data were weighted 0. After filtering in the same manner described above, we were left with 66 MRs covering all transcription factors.

## Comparison
Since the set of SOC genes is typically used as context genes for TRANSPATH, we decided to compare the MRs that resulted from the two pathways. Of the two lists of MRs, 60 were the same.


![venn]({{ site.baseurl }}\_assets\images\MR_context_SOC_vs_allprtn.png)
