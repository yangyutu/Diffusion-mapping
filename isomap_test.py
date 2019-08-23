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

plt.close('all')
npoint = 1000
n_components = 3
n_neighbors = 10
X, color = getCornerPlane(1000)
X, color = getTwinPeaks(1000)
npoint = len(color)
solver = manifold.Isomap(n_neighbors, n_components)
Y = solver.fit_transform(X)
fig = plt.figure(2)
ax = fig.add_subplot(111)
plt.scatter(Y[:, 0], Y[:, 1], c=color[:,0], cmap=plt.cm.Spectral)

#ax.xaxis.set_major_formatter(NullFormatter())
#ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')

geodesic_distance = solver.dist_matrix_ 
#kernal is -0.5 * (I - 1/n_samples) * D^2 * (I - 1/n_samples)
#kernel = solver.kernel_pca_
#gd_transformed = kernel.transform(geodesic_distance)
#w,v = scipy.sparse.linalg.eigs(gd_transformed,k=10)

print('absolute reconstruct error')
error = solver.reconstruction_error()
print(error)
print(math.sqrt(error) / np.linalg.norm(geodesic_distance)) 

# now I do the eigendecomposition by myself
H = np.eye(npoint) - 1.0/npoint
S = geodesic_distance**2
tao_gdist = -np.dot(H,np.dot(S,H))/2.0
w,v = scipy.sparse.linalg.eigs(tao_gdist,k=10)
for i in range(v.shape[1]):
    if np.real(w[i]) > 0:
        v[:,i] = np.real(v[:,i]*math.sqrt(np.real(w[i])))

        
fig = plt.figure(3)
ax = fig.add_subplot(111)
plt.scatter(v[:, 0], v[:, 1], c=color[:,0], cmap=plt.cm.Spectral)
#ax.xaxis.set_major_formatter(NullFormatter())
#ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')
