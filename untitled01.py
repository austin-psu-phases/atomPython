# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:58:58 2015

@author: Austin
"""


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

posnumber=0
poshead=[]




with open('tetra.vasp', 'r') as fin:
    data = fin.read().splitlines(True)
    tempdat = data[2:5]
    print(tempdat[0].split('  '))
    print(tempdat)
    
with open('output', 'w') as fout:
    fout.writelines(data[2:5])
    


#def POSheadcut(file): 
#    lines=6
#    part1.open(file,"r")
#    part2.open(file,"w")
#    i=0
#    poshead.append([])   
#    for lines in part1:
#        poshead[posnumber].append(line)
#        part1.next()
#    for lines in part1:
#        
#        
#
#    posnumber=posnumber+1    
#    return 0
    
    
    