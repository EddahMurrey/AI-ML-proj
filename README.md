# cocos-usecase
Covid-19 Detection Usecase Using Pytorch

We are researching on Covid 19 detection using chest xray images using Pytorch. The images were downloaded from 
[Kaggle](https://www.kaggle.com/tawsifurrahman/covid19-radiography-database), an online community for data scientists
and machine learning enthusiasts. The algorithm would then try to detect from the images downloaded which patient 
image has covid-19. The images are in three folders normal, viral, covid with about 1000 images each. This is a 
continual research hence, we are working to improve the usecase and algorithm and also add more datasets. 

###Prerequisites
- Anaconda or Google Colab to write code in Jupyter notebook

### How It Works
The algorithm has set of sets that it follows to achieve accurate prediction. These steps are critical and dependent 
on the previous step hence these steps affect each other.These are:
1. Importing Libraries
Python libraries are imported to be used for the project. This code cell after importing libraries prints th
```
%matplotlib inline

import os
import shutil
import random
import torch
import torchvision
import numpy as np

from PIL import Image
from matplotlib import pyplot as plt

torch.manual_seed(0)

print('Using PyTorch version', torch.__version__)
```

2. Preparing Training and Test Sets
3. Creating Custom Dataset
4. Image Transformations
5. Prepare DataLoader
6. Data Visualization
7. Model Creation 
8. Model Training
9. Prediction

