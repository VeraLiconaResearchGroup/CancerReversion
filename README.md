Cancer Reversion
=============================
This lab notebook is developed from a jekyll template developed by [Florian Schneider](https://github.com/fdschneider/jekyll-lablog). It contains data, scripts, and documentation of the work for my undergraduate honors thesis with the [Computational Systems Medicine Team](https://veraliconaresearchgroup.github.io/) at UConn Health's Center for Quantitative Medicine.

## Project Description
Claudin-Low Triple Negative Breast Cancer (CL TNBC) has high relapse and low survival rates. Due to the tumors? decreased response to cytotoxic drugs and hormone therapy, alternative therapeutic strategies should be explored. One such strategy is tumor reversion, the biological process by which tumor cells lose a significant fraction of their malignant phenotype. Tumor reversion has been observed for over a century and has been achieved *in vitro*, *in vivo*, and *ex vivo*. In particular, tumor reversion has been achieved *in vitro* with the CL cell line MDA-MB-231, and *ex vivo* in mice xenografted with MDA-MB-231 cells. This project takes a dynamical systems approach to identify *in silico* combinations of therapeutic targets for CL TNBC reversion. An intracellular signaling network was reconstructed with multi-omics profile data for MDA-MB-231. Then a structure-based attractor-based control method for nonlinear dynamic systems was applied to the network to identify driver nodes of the system. Topological signal flow analysis was applied to the network for virtual screenings of driver node perturbations to predict their effect on the system. Combinations of nodes whose concerted perturbation resulted in the system shifting from the tumorigenic basin of attraction to the normal-like basin of attraction were deemed putative concerted reversion targets. Through this methodology, several potential combinations of targets that may shift the cell from a tumorigenic to a normal-like phenotype have been identified to be further validated in future work.


## Folder Architecture
**\_projects** Contains data, scripts, and results from the development of a quantitative pipeline for the identification of reversion targets in Claudin-Low Triple Negative Breast Cancer.



### Requirements
- install Developer Ruby
  - if you already have hombrew installed
  ```
  brew install ruby
  export PATH=/usr/local/opt/ruby/bin:$PATH
  ```
  - otherwise, install homebrew, then Ruby
  ```
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  brew install ruby
  export PATH=/usr/local/opt/ruby/bin:$PATH
  ```
- then from terminal install Jekyll (reccommended to sudo install using follow command)
  ```
  gem install --user-install bundler jekyll
  ```
### Deploy the Notebook
clone the repository to your machine. Then in terminal, navigate to the repository and use:
  `jekyll serve` to run it locally. Jekyll will provide a local url to navigate to in your internet browser.
  
