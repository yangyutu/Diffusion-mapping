# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:09:18 2015

@author: yuugangyang
"""

import numpy as np

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
    A = np.random.randn(5,5)    
    B = np.random.randn(5,5)
    dh = computeHausdorffDistance(A,B)
    print dh