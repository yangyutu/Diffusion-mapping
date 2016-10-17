# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:26:08 2015

@author: yuugangyang
"""

from time import time
import pylab
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
import numpy as np
import scipy
import math
from sklearn import manifold, datasets
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.decomposition import PCA
matplotlib.interactive(True)
from sklearn.manifold.spectral_embedding_ import _graph_is_connected
from compute_diffusion_map import *
from thresholdDistanceMatrix import *
from sampleDataExample import *
plt.rc('text',usetex=True)
# Next line to silence pyflakes. This import is needed.
Axes3D

n_points = 800
#X, color = datasets.samples_generator.make_swiss_roll(n_points)
#
plt.close('all')
X, color = getCornerPlane(n_points)
X, color = getTwinPeaks(n_points)
fig = plt.figure(1)
ax = fig.add_subplot(111,projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')

# now we calculate the pair-wise distance
dist = euclidean_distances(X,X)
sort_dist = np.sort(dist)
dist_thresh,epi = thresholdDistanceMatrix(dist,epi=0.5,mode='manual')
#dist_thresh,epi = thresholdDistanceMatrix(dist)
plt.figure(10)
plt.imshow(dist_thresh)
plt.colorbar()
if not _graph_is_connected(dist_thresh):
    raise ValueError('Graph is disconnected')


embedding, result = compute_diffusion_map(dist_thresh,alpha=0.,n_components=10)

sum_vec = np.sum(dist_thresh,axis=1)

sum_vec = np.power(sum_vec,-0.5)
norm_mat = np.diag(sum_vec)


M = np.dot(norm_mat,np.dot(dist_thresh,norm_mat))

#M = dist_thresh

for i in range(M.shape[0]):
    M[i] = M[i]/np.sum(M[i])

# after normalization, M is not sysmetric    
#M = np.transpose(M)
    
w,v = scipy.sparse.linalg.eigs(M,k=10)
v = np.dot(v,np.diag(w))

fig = plt.figure(6)
ax = fig.add_subplot(111,projection='3d')
ax.scatter(v[:,1],v[:,2],v[:,3],c=color, cmap=plt.cm.Spectral)

fig = plt.figure(8)
ax = fig.add_subplot(111,projection='3d')
ax.scatter(v[:,1],v[:,2],c=color, cmap=plt.cm.Spectral)

fig = plt.figure(7)
ax = fig.add_subplot(111)
ax.scatter(embedding[:,0],embedding[:,1],c=color, cmap=plt.cm.Spectral)

fig = plt.figure(9)
ax = fig.add_subplot(111,projection='3d')
ax.scatter(embedding[:,0],embedding[:,1],embedding[:,2],c=color, cmap=plt.cm.Spectral)
#
