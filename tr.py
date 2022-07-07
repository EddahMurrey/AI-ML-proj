import os
import shutil
import random

root = 'H1'

dest_path = "H1/S3"

files_list = []

for root, dirs, files in os.walk('H1/IMAGES'):
    for file in files:
          if file.endswith(".png"):
            files_list.append(os.path.join(root, file))

filesToCopy = random.sample(files_list, 50) 

if os.path.isdir(dest_path) == False:
    os.makedirs(dest_path)

for file in filesToCopy:
    shutil.move(file, dest_path)
