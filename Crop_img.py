# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 12:51:32 2021

@author: Adarsh
"""

import cv2
import matplotlib.pyplot as plt
import os, glob
from tqdm import tqdm
path_img = glob.glob(os.path.join('D:\\Internship\\Solar_astronomy\\Project_3-Sigmoid\\Final_data\\images','*.png'))
path_img.sort()
path_label = glob.glob(os.path.join('D:\\Internship\\Solar_astronomy\\Project_3-Sigmoid\\Final_data\\Crop_data\\labels','*.txt'))

dir_img = os.listdir('D:\\Internship\\Solar_astronomy\\Project_3-Sigmoid\\Final_data\\images')
dir_img.sort()


for i in tqdm(range(len(path_img))):
  img = cv2.imread(path_img[i])
  dh, dw, _ = img.shape

  fl = open(path_label[i], 'r')
  data = fl.readlines()
  fl.close()
  k = 1
  for dt in data:

      # Split string to float
      _, x, y, w, h = map(float, dt.split(' '))

 
      l = int((x - w / 2) * dw)
      r = int((x + w / 2) * dw)
      t = int((y - h / 2) * dh)
      b = int((y + h / 2) * dh)
      
      if l < 0:
          l = 0
      if r > dw - 1:
          r = dw - 1
      if t < 0:
          t = 0
      if b > dh - 1:
          b = dh - 1

      #cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 1)
      img1 = img[t:b,l:r]
      cv2.imwrite( 'D:\\Internship\\Solar_astronomy\\Project_3-Sigmoid\\Final_data\\Crop_data\\New_croped_images\\' +dir_img[i][0:-4] +'-'+ str(k) + '.png' , img1 )
      k = k+1
