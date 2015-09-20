
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:21:43 2015

@author: Austin
"""
import math
import random as rnd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt, asin, cos, sin




##take a list of vetors from a text file
## format of file: space seperated list

## read in vector lists

twopi=6.2831853

def rotate (theta,vec):
#    print(vec)
    W1 = np.array([[0,-vec[2],vec[1]],[vec[2],0,-vec[0]],[-vec[1],vec[0],0]])
    W2 = np.dot(W1,W1)
    E = np.array([[1,0,0],[0,1,0],[0,0,1]])
    a = sin(theta)
    b = 1-cos(theta)
    transform = E + a*W1 + b*W2
#    print(W1)
#    print(transform)
    return transform
    
print "hello"
    
k1=np.dot(rotate(rnd.random()*twopi,[1,0,0]),[0,1,0])    
print(k1)
print(sqrt(np.dot(k1,k1)))    
print(np.dot(k1,[1,0,0]))


    