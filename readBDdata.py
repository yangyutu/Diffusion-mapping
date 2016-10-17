# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:47:03 2015

@author: yuugangyang
"""

import numpy as np
from computeHausdorff import *
dataset = []
n = 8148
for i in np.arange(1,n+1):
    data = np.genfromtxt('bddata/configsetslam9/startmeshgrid'+str(int(i))+'.txt')[:,0:2]
    dataset.append(data)
    
dist = np.zeros((n,n))
for i in range(len(dataset)-1):
    print i
    for j in range(i+1,len(dataset)):
        s1 = dataset[i]
        s2 = dataset[j]
        dist[i,j] = computeHausdorffDistance(s1,s2)
        
dist = dist + np.transpose(dist)
np.savetxt('BD_data_dist.txt',dist)
    
    
