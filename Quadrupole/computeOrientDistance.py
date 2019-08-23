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
seq = np.random.choice(range(8148),4000)
seq = np.genfromtxt('random_seq_size_4074.txt').astype(np.int)
seq = seq - 1
dataSize = len(seq)
distance = np.zeros((dataSize,dataSize))
for i in range(dataSize):
    descriptorSet[seq[i]] = descriptorSet[seq[i]] / np.linalg.norm(descriptorSet[seq[i]])

for i in range(dataSize-1):
    des1 = descriptorSet[seq[i]]
    print i
#    plt.figure(i)
#    plt.plot(des1)    
    for j in range(i+1,dataSize):     
        des2 = descriptorSet[seq[j]]
#        plt.figure(j)
#        plt.plot(des2)
        corr = np.fft.ifft(np.fft.fft(des1) * np.conj(np.fft.fft(des2)))
        distance[i,j] = np.max(np.real(corr))
              
distance = distance + np.eye(dataSize) + np.transpose(distance)
distance = 2 - 2*distance
sort_dist = np.sort(distance)

np.savetxt('orient_dist.txt',distance)
np.savetxt('orient_dist_randomSeq.txt',seq)
#
#des1 = np.random.rand(128)
#des2 = np.roll(des1,100)
#des1 = des1 / np.linalg.norm(des1)
#des2 = des2 / np.linalg.norm(des2)
#corr = np.fft.ifft(np.fft.fft(des1) * np.conj(np.fft.fft(des2)))
#print np.max(np.real(corr))