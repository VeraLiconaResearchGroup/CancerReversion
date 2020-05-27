A Quantitative Pipeline for the Identification of Combinations of Targets for Claudin Low Triple Negative Breast Cancer Reversion
==============================

### Project Description
Claudin-Low Triple Negative Breast Cancer (CL TNBC) has high relapse and low survival rates. Due to the tumors? decreased response to cytotoxic drugs and hormone therapy, alternative therapeutic strategies should be explored. One such strategy is tumor reversion, the biological process by which tumor cells lose a significant fraction of their malignant phenotype. Tumor reversion has been observed for over a century and has been achieved *in vitro*, *in vivo*, and *ex vivo*. In particular, tumor reversion has been achieved *in vitro* with the CL cell line MDA-MB-231, and *ex vivo* in mice xenografted with MDA-MB-231 cells. This project takes a dynamical systems approach to identify *in silico* combinations of therapeutic targets for CL TNBC reversion. An intracellular signaling network was reconstructed with multi-omics profile data for MDA-MB-231. Then a structure-based attractor-based control method for nonlinear dynamic systems was applied to the network to identify driver nodes of the system. Topological signal flow analysis was applied to the network for virtual screenings of driver node perturbations to predict their effect on the system. Combinations of nodes whose concerted perturbation resulted in the system shifting from the tumorigenic basin of attraction to the normal-like basin of attraction were deemed putative concerted reversion targets. Through this methodology, several potential combinations of targets that may shift the cell from a tumorigenic to a normal-like phenotype have been identified to be further validated in future work.

### Folder Architecture

**_posts** contains github markdown blog posts designed to be displayed via jekyll. These posts describe the work that has been done and provides links to literature as well as the data being referenced.

**Differential_Expression** contains raw and processed RNAseq data and differential expression results from Macrogen.

**Network _Components** contains all the files pertaining to the individual components of the model: FunDEGs, TFs, and MRs. It also includes general data used to identify these components including RNAseq, Protein Mass Spec, and Bisulfite.

**Network_Construction** contains all scripts necessary to extract edges between network layers and the resulting files.

**Network_Analysis** contains all scripts necessary to identify and prioritize reversion targets.

**Mutations** contains the mutational profile of MDA-MB-231 and the results of ensembl VEP.

**OLD** contains previous attempts and preliminary anlayses for network construction and analysis.

**sfa-0.01-py3.6.egg** contains the modified SFA package to allow for iterative simulations.

**Writing** contains abstracts and summaries written throughout this project.

**zanudo2015_SFAexploration** contains results from the SFA analysis to determine the uses and limitations of SFA on an example T-LGL network from Zanudo.
