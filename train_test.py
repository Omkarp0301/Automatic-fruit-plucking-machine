# -*- coding: utf-8 -*-
"""train_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hc21q_medBkqz7CsNew8lpkPAsIt2SXt
"""

from google.colab import drive
drive.mount('/content/drive')

import os

image_path='/content/drive/My Drive/darknet/data/Lemon_Dataset'
os.chdir(image_path)

path_list=[]

for current_dir, dirs, files in os.walk('.'):
  for f in files:
    if f.endswith('.jpg'):
      file_loc = image_path + '/' + f
      path_list.append(file_loc + '\n')

path_list_test = path_list[:int(len(path_list)*0.20)]
path_list = path_list[int(len(path_list)*0.20):]

with open('train.txt', 'w') as train:
  for i in path_list:
    train.write(i)

with open('test.txt','w') as test:
  for i in path_list_test:
    test.write(i)

i=0

with open(image_path + '/' + 'classes.names','w') as cls, \
     open(image_path + '/' + 'classes.txt', 'r') as text:

     for l in text:
       cls.write(l)

       i += 1

with open(image_path + '/' + 'image_data.data', 'w') as data:

  data.write('classes = ' + str(i) + '\n')

  data.write('train = ' + image_path + '/' + 'train.txt' + '\n')

  data.write('valid = ' + image_path + '/' + 'test.txt' + '\n')

  data.write('names = ' + image_path + '/' + 'classes.names' + '\n')

  data.write('backup = backup')
