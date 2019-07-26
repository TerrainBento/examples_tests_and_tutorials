# As of July 2019, please find the notebooks in the [main terrainbento repository](https://github.com/TerrainBento/terrainbento/).

[![DOI](https://zenodo.org/badge/123941759.svg)](https://zenodo.org/badge/latestdoi/123941759)
[![Build Status](https://travis-ci.org/TerrainBento/examples_tests_and_tutorials.svg?branch=master)](https://travis-ci.org/TerrainBento/examples_tests_and_tutorials)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TerrainBento/examples_tests_and_tutorials/master?filepath=Welcome_to_TerrainBento.ipynb)

Examples, tests, and tutorials for the [terrainbento modular landscape evolution modeling package](https://terrainbento.github.io) built on top of the [Landlab Toolkit](http://landlab.github.io).

## Installation instructions

These installation instructions assume you already have python and the conda package management tool installed on you computer. We recommend that you use the [Anaconda python distribution](https://www.anaconda.com/download/). Unless you have a specific reason to want Python 2.7 we strongly suggest that you install Python 3.7 (or the current 3.* version provided by Anaconda).


### Step 1: Install terrainbento.
[This page](https://github.com/TerrainBento/terrainbento/blob/master/README.md#installation-instructions) describes the options avaliable to install terrainbento. Choose and complete one of them. 

### Step 2: Clone this repository
Next you will need to download the contents of this repository. You can either click the "Clone or Download" button, or clone using the git command line. 

```
git clone https://github.com/TerrainBento/examples_tests_and_tutorials.git
```

### Step 3: Install the requirements

Next navigate to the directory containing the examples and install the required packages. 
```
cd examples_tests_and_tutorials
conda install --file=requirements.txt
```
