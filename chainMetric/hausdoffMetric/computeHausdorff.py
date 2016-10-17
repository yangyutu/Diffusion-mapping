# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:09:18 2015

@author: yuugangyang
"""

import numpy as np
import pickle
import pylab
import matplotlib
import matplotlib.pyplot as plt
import math
n_rot = 36;
rot_set = []

for i in range(n_rot):
    theta = (i)*math.pi/n_rot
    rot_set.append(np.array([[math.cos(theta),math.sin(theta)],[-math.sin(theta),math.cos(theta)]]))


def compute_dist(A, B):
    dim= A.shape[1]
    dist = []
    for k in range(A.shape[0]):
        C = np.dot(np.ones((B.shape[0], 1)), A[k,:].reshape(1,A.shape[1]))
        D = (C-B) * (C-B)
        D = np.sqrt(np.dot(D,np.ones((dim,1))))
        dist.append(np.min(D))
    dist = max(np.array(dist))
    return dist

def computeHausdorffDistance(A,B):
# ** A and B may have different number of rows, but must have the same number of columns. **
#
    if not A.shape[1] == B.shape[1]:
        print "dimension not matched!"
        return
    d1 = compute_dist(A, B)
    d2 = compute_dist(B, A)
    dH = max(d1,d2)
    return dH


if __name__ == '__main__':
    dataset = pickle.load(open('combine_config.p'))
    n = len(dataset)
    dist = np.zeros((n,n))
    for i in range(len(dataset)-1):
        print i
        for j in range(i+1,len(dataset)):
            s1 = dataset[i]
            s2 = dataset[j]
            dist_set = []
            for rot in rot_set:
                s2 = np.dot(s2,rot)
                dist_temp = computeHausdorffDistance(s1,s2)
                dist_set.append(dist_temp)
            dist[i,j] = np.min(dist_set)

    dist = dist + np.transpose(dist)
np.savetxt('Hausdoff_dist_rot2.txt',dist)