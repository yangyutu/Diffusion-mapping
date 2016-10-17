# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:12:15 2015

@author: yuugangyang
"""

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


numY = 100
Y = np.linspace(0,10,num=numY).reshape(numY,1)

dist_Y = euclidean_distances(Y,Y)
UY,SY,VY = np.linalg.svd(dist_Y)
H = np.eye(numY) - 1.0/numY
S = dist_Y**2
tao_dist = -np.dot(H,np.dot(S,H))
UY2,SY2,VY2 = np.linalg.svd(tao_dist)


#using diffusion mapping to do this
epi =20
dist_thresh = np.exp(-dist_Y**2/epi/2.0)
M = dist_thresh
for i in range(M.shape[0]):
    M[i] = M[i]/np.sum(M[i])
    
M = np.transpose(M)


w,v = np.linalg.eig(M)

U,S,V = np.linalg.svd(M)

plt.figure(1)
plt.plot(np.real(v[:,1]))

plt.figure(2)
plt.plot(np.real(v[:,2]))

plt.figure(3)
plt.plot(np.real(v[:,3]))
#S_M = M**2
#
#tao_M = -np.dot(H,np.dot(S_M,H))
#
#w2,v2 = np.linalg.eig(tao_M)
