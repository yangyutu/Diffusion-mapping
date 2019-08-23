# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:11:45 2015

@author: yuugangyang
"""

import numpy as np
import sklearn
import math
import pylab as P
import matplotlib.pyplot as plt

plt.close('all')
descriptorSet = []
for ii in range(1,8149):
#for ii in [1,7674]:
#for i in [7414,7674]:
    print ii
    data = np.genfromtxt('bddata/configsetslam9/startmeshgrid'+str(int(ii))+'.txt')[:,1:3]
    nbs = sklearn.neighbors.NearestNeighbors(n_neighbors=7,algorithm='ball_tree').fit(data)
    distances, indices = nbs.kneighbors(data)
    angle = []
    for i in range(data.shape[0]):
        x0 = data[i,0]
        y0 = data[i,1]    
        for nb_idx, dist in zip(indices[i,1:],distances[i,1:]):
            if dist < 2.85:
                x1 = data[nb_idx,0]
                y1 = data[nb_idx,1]
                angle.append(math.atan2(y1-y0,x1-x0)*180.0/math.pi)
    descriptor,edges = np.histogram(angle,bins=128,range=(-180.0,180.0))
    descriptorSet.append(descriptor)    
 
descriptorSet = np.array(descriptorSet)
np.savetxt('orient_hist.txt',descriptorSet)
#P.hist(np.array(angle))
#P.figure(2)
#P.scatter(data[:,0],data[:,1])
# 7598 grain boundary
seq = [7598,7674]
for des in seq:
    plt.figure
    plt.plot(edges[:-1],descriptorSet[des])
    plt.xlabel('angle')
    plt.ylabel('normalized count')