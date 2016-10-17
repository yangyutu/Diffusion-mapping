# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:02:32 2015

@author: yuugangyang
"""
import pylab
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
import scipy
import math
import numpy as np
from sklearn import manifold, datasets
from sampleDataExample import *

def isomapReduction(X, n_neighbors=10,n_components=10):
    npoint = X.shape[0]
    solver = manifold.Isomap(n_neighbors, n_components)
    Y = solver.fit_transform(X)   
    geodesic_distance = solver.dist_matrix_ 
    result = {}
    
    result['embedding'] = Y
    error = solver.reconstruction_error()    
    
    result['absolute reconstruct error'] = error 
    result['relative reconstruct error'] = math.sqrt(error) / np.linalg.norm(geodesic_distance) 
    # now I do the eigendecomposition by myself
    # first  -0.5 * (I - 1/n_samples) * D^2 * (I - 1/n_samples)
    H = np.eye(npoint) - 1.0/npoint
    S = geodesic_distance**2
    tao_gdist = -np.dot(H,np.dot(S,H))/2.0
    w,v = scipy.sparse.linalg.eigs(tao_gdist,k=n_components)
    for i in range(v.shape[1]):
        if np.real(w[i]) > 0:
            v[:,i] = np.real(v[:,i]*math.sqrt(np.real(w[i])))
    
    result['eigenvalues'] = w
    
    return Y, result