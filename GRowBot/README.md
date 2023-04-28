# GRowBot Project

This repository contains the code and resources for the GRowBot project, an autonomous robot designed for precision application of fertilizers and herbicides, as well as better management of crops in agriculture. The project is in its early stages, and the current focus is on developing computer vision algorithms for crop and weed counting, as well as disease classification.

## Project Overview

The GRowBot project aims to:

1. Optimize the use of fertilizers and herbicides in agriculture by implementing precision farming techniques.
2. Reduce the environmental impact of agrochemicals through targeted application.
3. Increase crop yields and improve overall farm management.

## Current Progress

At this stage, the project contains a few Jupyter Notebook files with the following functionalities:

1. Training a YOLOv8 (You Only Look Once) model for crop and weed detection and inference on a test set.
2. Training an SSD (Single Shot MultiBox Detector) model for crop and weed detection.
3. Integrating hypothetical NPK nutrient testing results and providing fertilisation ratio recommendations based on test results.



![An example output from inference on the 100 test set images. To simulate the GRowBot moving along a 100m row of carrots the test images were loosely ordered so that their were more weed annotations towards the back. This would simulate a situation where there are more weeds at one end where maybe seeds have blown in from an adjacent field. ](images/Carrot_weed_dens_graph.png)



## Future Work
The GRowBot project is still in its early stages, and there are plans to further develop the project, including:

- Transferring to Python files once a local GPU enabled machine has been bought
- Finding a crop / dataset so that the bounding box can be passed to a disease classification network
- Further testing and hyperparameter tuning with these and other object detection algorithms
