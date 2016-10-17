# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:11:45 2015

@author: yuugangyang
"""

import numpy as np
import sklearn.metrics
import math
import pylab as P
import matplotlib.pyplot as plt
import pickle
import scipy

def cconv(a, b):
    '''
    Computes the circular convolution of the (real-valued) vectors a and b.
    '''
    return np.fft.ifft(np.fft.fft(a) * np.fft.fft(b)).real

#gau = scipy.ndimage.filters.gaussian_filter1d()


from math import pi, sqrt, exp

def gauss(n=11,sigma=1):
    r = range(-int(n/2),int(n/2)+1)
    return [1 / (sigma * sqrt(2*pi)) * exp(-float(x)**2/(2*sigma**2)) for x in r]

plt.close('all')
descriptorSet = []

dataset = pickle.load(open('combine_config.p'))
addGauFlag = 1
nbin=127
Gaufilter = gauss(nbin);
for ii in range(len(dataset)):
#for ii in [1,7674]:
#for i in [7414,7674]:
    print ii
    data = dataset[ii]
    dist = sklearn.metrics.pairwise.euclidean_distances(data);
    angle = []
    for i in range(data.shape[0]):
        x0 = data[i,0]
        y0 = data[i,1]
        for j in range(data.shape[0]):
            if dist[i,j] < 2.85 and j != i:
                x1 = data[j,0]
                y1 = data[j,1]
                angle.append(math.atan2(y1-y0,x1-x0)*180.0/math.pi)


    angle[angle<0] += 360
    descriptor,edges = np.histogram(angle,bins=nbin,range=(0,180.0))
    if addGauFlag:
        descriptor_Gau = cconv(descriptor,Gaufilter)
    descriptorSet.append(descriptor_Gau)

descriptorSet = np.array(descriptorSet)
np.savetxt('orient_hist.txt',descriptorSet)
#P.hist(np.array(angle))
#P.figure(2)
#P.scatter(data[:,0],data[:,1])
# 7598 grain boundary
#seq = [7598,7674]
#for des in seq:
#    plt.figure
#    plt.plot(edges[:-1],descriptorSet[des])
#    plt.xlabel('angle')
#    plt.ylabel('normalized count')