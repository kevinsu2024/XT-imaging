**About**
This is the repository for all code developed for the XT-imaging task, part of Fawzi Lab.
Currently, we are working on blood streak detection for calculated XT images.

**Files**
experiments: This folder includes experiments with the Canny edge detection method on images, testing its ability to identify streaks, as well as tests to the Pyradon library

pretrained_models: This folder includes open-source models found that may be uesful in identifying streaks
- LSWMS: This model uses the weighted mean-squares algorithm to identify lines, on top of Hough transform. 
- Pyradon: This is a library used to find streaks in astronomical images, using Fast Radon Transform.
Link to Pyradon paper: https://iopscience.iop.org/article/10.3847/1538-3881/aaddff/pdf

Currently experimenting with Pyradon. This model is built to identify patterns in very noisy images, which is similar to our application. 