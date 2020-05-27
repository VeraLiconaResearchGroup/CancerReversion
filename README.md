Cancer Reversion
=============================
The lab notebook of Madeleine S. Gastonguay for the Computational Systems Medicine Team.

## Description
This is a lab notebook developed from a jekyll template developed by [Florian Schneider](https://github.com/fdschneider/jekyll-lablog). It contains data, scripts, and documentation of the work for my undergraduate honors thesis with the [Computational Systems Medicine Team](https://veraliconaresearchgroup.github.io/) at UConn Health's Center for Quantitative Medicine.

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
  
