# Research Artifacts

The following repo contains the research artifacts for the paper "Demonstrating and Analyzing the Effects of Dynamic Contact Graphs in Improving Wireless Adhoc Delay Tolerant Networks through a Simulated Stratospheric Testbed", presented at [AIAA SciTech](https://www.aiaa.org/SciTech) 2025. 

> The paper itself will be linked when made public on AIAA's ARC distribution platform.

The artifacts include:

* `sim_tests.ipynb` - A Jupyter notebook that runs simulations of the three types described in the paper, and plots outputs of the data.

* `f23_495.ipynb` - (Not included in paper) This uses actual positional data from a launch of 4 balloons instead of randomly generated trajectories.

* `dr_test.ipynb` - A test of calculating the data rates between nodes given receive power using root-finding.

* `system_plot_concat.ipynb` - Takes in 8 CSV files (one for each system) and plots them on a single image.

* `figs_new/` - Figs that were generated for the paper.

## Using the Artifacts

To use the Jupyter notebooks, just clone this repo:

```bash
git clone --recursive [git-url]
```

and run the notebook cells. Make sure to run the top-most cell first (which installs dependencies).

## Authorship

The following artifacts are provided with permission from the University of Michigan, and the authors:

* Ali Mosallaei (alimos@umich.edu)

* Daniil Voloshin (daniilv@umich.edu)

* James W. Cutler (jwcutler@umich.edu)

The paper is published by AIAA with permission from the University of Michigan, which holds the copyright to the work. 

