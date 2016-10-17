# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:12:30 2015

@author: yuugangyang
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

def cconv(a, b):
    '''
    Computes the circular convolution of the (real-valued) vectors a and b.
    '''
    return np.fft.ifft(np.fft.fft(a) * np.fft.fft(b)).real
    
#gau = scipy.ndimage.filters.gaussian_filter1d()

plt.close('all')


descriptorSet = np.genfromtxt('orient_hist.txt')
dataSize = descriptorSet.shape[0]
distance = np.zeros((dataSize,dataSize))
for i in range(dataSize):
    descriptorSet[i] = descriptorSet[i] / np.linalg.norm(descriptorSet[i])

for i in range(dataSize-1):
    des1 = descriptorSet[i]
    print i
#    plt.figure(i)
#    plt.plot(des1)    
    for j in range(i+1,dataSize):     
        des2 = descriptorSet[j]
#        plt.figure(j)
#        plt.plot(des2)
        corr = np.fft.ifft(np.fft.fft(des1) * np.conj(np.fft.fft(des2)))
        distance[i,j] = np.max(np.real(corr))
 
# now create symmetric matrix and revert the scale, since large correlation means small distance            
distance = distance + np.eye(dataSize) + np.transpose(distance)
distance = 2 - 2*distance
sort_dist = np.sort(distance)

np.savetxt('orient_dist.txt',distance)
#np.savetxt('orient_distq.txt',seq)
#
#des1 = np.random.rand(128)
#des2 = np.roll(des1,100)
#des1 = des1 / np.linalg.norm(des1)
#des2 = des2 / np.linalg.norm(des2)
#corr = np.fft.ifft(np.fft.fft(des1) * np.conj(np.fft.fft(des2)))
#print np.max(np.real(corr))