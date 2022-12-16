# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 13:47:02 2021

@author: Adarsh
"""

#cd D:\\Interns\\Solar_astronomy\\Project_3-Sigmoid\\Final_data



path_sigmoid = 'Crop_data\\Classificationv2\\2014'
path_original = 'images\\'

path_label = 'labels'


import os, glob
from tqdm import tqdm

files_sigmoid = glob.glob(os.path.join(path_sigmoid, '*.png'))
files_original = glob.glob(os.path.join(path_original, '*.png') )
files_label = glob.glob(os.path.join(path_label, '*.txt'))
name_original = os.listdir(path_original)
name_sigmoid = os.listdir(path_sigmoid)

import cv2 as cv
import cv2
import matplotlib.pyplot as plt


for i in tqdm(range(len(files_original))):
    for j in range(len(files_sigmoid)):
        if name_original[i][:-4] == name_sigmoid[j].split('-')[0]:
            
            img_rgb = cv2.imread(files_original[i])
            
        
            img = cv2.imread(files_original[i],0)
            img2 = img.copy()
            template = cv.imread(files_sigmoid[j],0)
            w, h = template.shape[::-1]
            # All the 6 methods for comparison in a list
            #methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
                  #      'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
            
            methods = [  'cv.TM_SQDIFF_NORMED']
            for meth in methods:
                img = img2.copy()
                method = eval(meth)
                # Apply template Matching
                res = cv.matchTemplate(img,template,method)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
                if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
                    top_left = min_loc
                else:
                    top_left = max_loc
                bottom_right = (top_left[0] + w, top_left[1] + h)
                
                cv.rectangle(img_rgb,top_left, bottom_right, 255, 2)
                #plt.subplot(121),plt.imshow(res,cmap = 'gray')
                #plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
                #plt.subplot(122),plt.imshow(img,cmap = 'gray')
                #plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
                #plt.suptitle(meth)
                #plt.show()
                cv2.imwrite('Detected_sigmoid\\'+ name_original[i] , img_rgb)
                
              
# For 2013 and 2014   
              
for i in tqdm(range(len(files_original))):
    for j in range(len(files_sigmoid)):
        if name_original[i][:-4] == name_sigmoid[j].split('-')[0]+ '-' + name_sigmoid[j].split('-')[1]:
            
            img_rgb = cv2.imread(files_original[i])
            
        
            img = cv2.imread(files_original[i],0)
            img2 = img.copy()
            template = cv.imread(files_sigmoid[j],0)
            w, h = template.shape[::-1]
            # All the 6 methods for comparison in a list
            #methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
                  #      'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
            
            methods = [  'cv.TM_SQDIFF_NORMED']
            for meth in methods:
                img = img2.copy()
                method = eval(meth)
                # Apply template Matching
                res = cv.matchTemplate(img,template,method)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
                if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
                    top_left = min_loc
                else:
                    top_left = max_loc
                bottom_right = (top_left[0] + w, top_left[1] + h)
                
                cv.rectangle(img_rgb,top_left, bottom_right, 255, 2)
                #plt.subplot(121),plt.imshow(res,cmap = 'gray')
                #plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
                #plt.subplot(122),plt.imshow(img,cmap = 'gray')
                #plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
                #plt.suptitle(meth)
                #plt.show()
                cv2.imwrite('Detected_sigmoid\\'+ name_original[i] , img_rgb)
                
    


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

    
    img1 = img[t:b,l:r]
    
    #if img1 == :
    if abs(img1.shape[0]-sigmoid.shape[0])< 5 and abs(img1.shape[1]-sigmoid.shape[1])<5 :
        print(img1.shape)
        cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 1)
        cv2.imwrite('Detected_sigmoid\\2011_012.png', img)
        
plt.imshow(img1)
plt.show()





import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv2.imread(path_original)
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread(path_sigmoid,0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imwrite('res.png',img_rgb)



import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(path_original,0)
img_rgb = cv2.imread(path_original)
img2 = img.copy()
template = cv.imread(path_sigmoid,0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
#methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
      #      'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

methods = [  'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    cv.rectangle(img_rgb,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
    cv2.imwrite('Detected_sigmoid\\2011_013.png', img_rgb)






























