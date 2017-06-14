#!/usr/bin/python


import sys
import os
from pylab import *
from scipy.ndimage import measurements
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt 


if __name__ == '__main__':
    
    file_list=os.listdir("images")
    cristalli = np.array([])
    for i in file_list:
        file_path="images/"+i
        im = Image.open(file_path).convert("L")
        I  = np.asarray(im)
        lw,num = measurements.label(I)
        area = measurements.sum(I, lw, range(num + 1))/255
        plt.imshow(lw)
        plt.show()
        #print area[1:]
        cristalli = np.append(cristalli,area[1:])
    #print cristalli
    plt.hist(cristalli)
    p
    plt.show()

