# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:27:12 2015

@author: yuugangyang
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:47:03 2015

@author: yuugangyang
"""

import numpy as np
from computeHausdorff import *
dataset = []
n = 8148
seq = np.random.choice(np.arange(1,n+1),n/2).astype(np.int)
for i in seq:
    data = np.genfromtxt('bddata/configsetslam9/startmeshgrid'+str(int(i))+'.txt')[:,1:3]
    [u,s,v] = np.linalg.svd(data)
    center = np.mean(data,axis=0)
    data[:,0] = data[:,0] - center[0]
    data[:,1] = data[:,1] - center[1]
    data = np.dot(data,v)
    dataset.append(data)

datasize = len(dataset)
dist = np.zeros((datasize,datasize))
for i in range(len(dataset)-1):
    print i
    for j in range(i+1,len(dataset)):
        s1 = dataset[i]
        s2 = dataset[j]
        dist[i,j] = computeHausdorffDistance(s1,s2)
        
dist = dist + np.transpose(dist)
np.savetxt('BD_data_dist_randomsample_size_'+str(datasize)+'.txt',dist)
np.savetxt('random_seq_size_'+str(datasize)+'.txt',seq)
    
    
