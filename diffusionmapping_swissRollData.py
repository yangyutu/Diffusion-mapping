# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:20:23 2015

@author: yuugangyang
"""

from time import time
import pylab
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
import scipy
import math
from sklearn import manifold, datasets
from sampleDataExample import *
import numpy as np
from compute_diffusion_map import compute_diffusion_map
from thresholdDistanceMatrix import thresholdDistanceMatrix

from sklearn.metrics.pairwise import euclidean_distances
plt.close('all')

n_points = 1000
data = np.genfromtxt('swissRollpoints.txt')
X = data[:,0:3]
color = data[:,3]

dist_Y = euclidean_distances(X,X)


thresholdDistanceMatrix(dist_Y)

#using diffusion mapping to do this
epi =100
dist_thresh = np.exp(-dist_Y**2/epi/2.0)
M = dist_thresh
for i in range(M.shape[0]):
    M[i] = M[i]/np.sum(M[i])

from sklearn.manifold.spectral_embedding_ import _graph_is_connected
plt.figure(10)
plt.imshow(dist_thresh)
plt.colorbar()
if not _graph_is_connected(dist_thresh):
    raise ValueError('Graph is disconnected')

embedding, result = compute_diffusion_map(dist_thresh, n_components=5)    

    
# w,v = np.linalg.eig(M)

# U,S,V = np.linalg.svd(M)

# plt.figure(1)
# plt.plot(np.real(v[:,1]))

# plt.figure(2)
# plt.plot(np.real(v[:,2]))

# plt.figure(3)
# plt.plot(np.real(v[:,3]))

plt.figure(1)
plt.scatter(embedding[:,1], embedding[:,2], c=color, cmap=plt.cm.Spectral)
# plt.axis('tight')

fig = plt.figure(figsize=(15, 8))

ax = fig.add_subplot(111, projection='3d')
ax.scatter(embedding[:, 1], embedding[:, 2], embedding[:, 3], c=color, cmap=plt.cm.Spectral)
ax.view_init(4, -72)
