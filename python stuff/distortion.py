
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


print "hello"

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


imgs=10

df1 = pd.read_csv('tetra.txt', sep=' ')
print(df1)
coords1 = df1.values

df2 = pd.read_csv('tetra2.txt', sep=' ')
print(df2)
coords2 = df2.values

coords1=np.array(coords1)
coords2=np.array(coords2)
# list of difference between vectors

diff1=coords1-coords2
print(diff1)



unormvecs=[]

i=0

for i in range(len(diff1)):
    if diff1[i,1] and diff1[i,0] == 0:
         unormvecs.append([1,0,0])
    norm=sqrt(pow(diff1[i,1],2)+pow(diff1[i,0],2))
    unormvecs.append([diff1[i,1]/norm, -diff1[i,0]/norm, 0])



images=[[[(((imgs+1-j)/float(imgs+1)))*coords1[i]+((j/float(imgs+1)))*coords2[i]]for j in range(0,imgs+2)] for i in range(len(diff1)) ]
images = np.array(images)



# takes each intermediate structure and adds on a normal vector which is rotated randomly 
# the normal vectors are scaled by: [magnitude of difference vector]/10
#loop i goes through the different axes
#loop j goes through the interpolated values but skips the end points
#loop k goes through 

i=0
j=0
rndk=10
for i in range(len(diff1)):
    for j in range(0,imgs+1):
        if j != imgs+1 and j != 0 :
            n1=None
            norm=None
            addn=None
            angle=None
            n1=float(sqrt(np.dot(diff1[i],diff1[i]))/10)
            angle=rnd.uniform(0,float(twopi))
            addn=np.dot(rotate(angle,diff1[i]), unormvecs[i])
            k=0  # the random function has difficulties with small numbers 
                # this is corrected by calling the function multiple times to ensure the distribution is random
            for k in range(0,rndk+1):
                addn=np.dot(rotate(angle,diff1[i]), addn)              
            addn=n1*addn/sqrt(np.dot(addn,addn))
            images[i][j]=images[i][j]+addn



images = images.swapaxes(0, 2)
images.shape = images.shape[1:]
print(images.shape)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for image in images:
    ax.scatter(image[:, 0], image[:, 1], image[:, 2])
plt.show()

