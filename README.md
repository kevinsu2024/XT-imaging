**About**
This is the repository for all code developed for the XT-imaging task, part of Fawzi Lab.
Currently, we are working on blood streak detection for calculated XT images.

**Files**
experiments: This folder includes experiments with the FRT model from guynir42.

pretrained_models: This folder includes open-source models found that may be uesful in identifying streaks
- LSWMS: This model uses the weighted mean-squares algorithm to identify lines, on top of Hough transform. 
- Pyradon: This is a library used to find streaks in astronomical images, using Fast Radon Transform.
Link to Pyradon paper: https://iopscience.iop.org/article/10.3847/1538-3881/aaddff/pdf

Currently experimenting with Pyradon. This model is built to identify patterns in very noisy images, which is similar to our application. 

Instructions for use:
1. Install Anaconda: https://www.anaconda.com/download
2. Create and activate the conda environment in your directory: https://conda.io/projects/conda/en/latest/user-guide/tasks/manag