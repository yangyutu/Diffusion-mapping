# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:36:17 2015

@author: yuugangyang
"""

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
from thresholdDistanceMatrix import *
from compute_diffusion_map import *
from sklearn.manifold.spectral_embedding_ import _graph_is_connected
def diffusemapReduction(dist, epi=0.5, mode='manual',n_neighbors=10,n_components=10):
    if mode == 'auto':
        dist_thresh,epi = thresholdDistanceMatrix(dist)
    else:        
        dist_thresh,epi = thresholdDistanceMatrix(dist,epi=epi,mode='manual')
    plt.figure(10)
    plt.imshow(dist_thresh)
    plt.colorbar()
    if not _graph_is_connected(dist_thresh):
        raise ValueError('Graph is disconnected')
    embedding, result = compute_diffusion_map(dist_thresh,alpha=0.,n_components=n_components)
    
    result['epi'] = epi    
    
    return embedding, result