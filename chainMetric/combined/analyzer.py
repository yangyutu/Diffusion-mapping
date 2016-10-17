# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:57:59 2015

@author: yuugangyang
"""

import sys
sys.path.append('../')

import pylab
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#from isomapReduction import *
from diffusemapReduction import *
import pickle

plt.close('all')

folder = ''

graph_dist = pickle.load(open(folder+'graph_dist_matrix_fullconnected.p','rb'))
y, result = diffusemapReduction(graph_dist,60)
time = range(len(y[:,0]))
fig = plt.figure(6)
plt.plot(result['eigenvalues'])
plt.xlabel('n')
plt.ylabel('lambda')

plt.figure(1)

plt.scatter(y[:,0],y[:,1],c=range(len(y[:,0])))
plt.xlabel('x1')
plt.ylabel('x2')
plt.colorbar()


fig = plt.figure(2)
ax = fig.add_subplot(111,projection='3d')
ax.scatter(y[:, 0], y[:, 1], time, c=time, cmap=plt.cm.Spectral)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('time')

fig = plt.figure(2)
ax = fig.add_subplot(111,projection='3d')
ax.scatter(y[:, 0], y[:, 1], time, c=time, cmap=plt.cm.Spectral)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('time')

fig = plt.figure(3)
ax = fig.gca(projection='3d')
ax.plot(y[:, 0], y[:, 1], time, c=[t/500.0 for t in time])
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('time')

plt.show()

fig = plt.figure(4)
ax = fig.add_subplot(111,projection='3d')
im = ax.scatter(y[:, 0], y[:, 1], y[:,2], c=time, cmap=plt.cm.Spectral)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')
# Add a colorbar
fig.colorbar(im, ax=ax)

np.savetxt('embedding.txt',y)
np.savetxt('lambda.txt',result['eigenvalues'])  

plt.figure(9)
plt.plot(y[0:600,2])
plt.figure(11)
plt.plot(y[600:1100,2])
plt.figure(12)
plt.plot(y[1100::,2])