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


imgs=5

df1 = pd.read_csv('file1.txt', sep=' ')
print(df1)
coords1 = df1.values

df2 = pd.read_csv('file2.txt', sep=' ')
print(df2)
coords2 = df2.values

# list of difference between vectors

diff1=coords1-coords2
print(diff1)

# angle about z= arcsine of y/sqrt(x^2 + y^2)
# angle about y= arcsine of z/sqrt(z^2 + H^2)
# gives transform matrix to point x in direction of vector
# transform normal vector by angle1, angle2 and then randangle about x axis

#list of angles for transformation obtained below:


# get list of cross products (normal vectors) to diff1

#print((np.cross(coords1[3],coords2[3])))



unormvecs=[]

for i in range(len(diff1)):
    if diff1[i,1] and diff1[i,0] == 0:
         unormvecs.append(1,0,0)
    norm=sqrt(pow(diff1[i,1],2)+pow(diff1[i,0],2))
#    print(norm)
    unormvecs.append([diff1[i,1]/norm, -diff1[i,0]/norm, 0])



print("this should be zero...if it worked")
k1=np.dot(rotate(rnd.random()*twopi,diff1[1]),unormvecs[1])
print(np.dot(k1,diff1[1]))




#for i in range(len(diff1)):
#    n_place=[]
#    norm=None
#    print(n_place)
#    print(norm)
#    norm=np.linalg.norm(np.cross(coords1[i],coords2[i])) 
#    n_place=np.cross(coords1[i],coords2[i])*(1/norm)
#    print(n_place)
#    print(norm)
#    unormvecs.append(n_place)
#    


## interpolate by some odd number of points between coordinates 


# define normRndRot 
# takes a normal unit vector 
# coordinate transform by anglez and angley 
# apply a random rotation about x''


# unto each image add normRndRot

# make a imgs+2 by len(diff1) array
images=[[[coords1[i]+((j/float(imgs+1)))*coords2[i]]for j in range(0,imgs+2)] for i in range(len(diff1)) ]
images = np.array(images)




##
#vectors=np.random.RandomState(42).rand(100,3)
#print vectors
#print "space"
#np.save("output1",vectors)
#newvector = np.load("output1.npy")
#print newvector
##