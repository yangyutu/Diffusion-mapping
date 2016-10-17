# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:16:02 2015

@author: yuugangyang
"""

import numpy as np
import scipy
node = 5
E1 = [(0,1),(1,0),(1,2),(2,1),(2,3),(3,2),(2,4),(4,2)]
E2 = [(0,1),(1,0),(1,2),(2,1),(2,3),(3,2),(2,4),(4,2)]
N1 = [1.0,2.0,3.0,1.0,1.0]
N2 = [1.0,2.0,3.0,1.0,1.0]
A = np.zeros((node**2,node**2))

mapindex = np.zeros((node**2,node**2),dtype=np.int)


for i in range(node**2):
    mapindex[i/node,i%node] = i

for i in range(node):
    for j in range(node):        
        for u in range(node):
            for v in range(node):
                if (i,u) in E1 and (j,v) in E2:
                    A[mapindex[i,j],mapindex[u,v]] = 1.0/N1[u]/N2[v]
                    
                    
w,v = scipy.sparse.linalg.eigs(A,10)
w = np.real(w)
                
w2,v2 = np.linalg.eig(A)
        
node = 3
E1 = [(0,1),(1,0),(1,2),(2,1)]
E2 = [(0,1),(1,0),(1,2),(2,1)]
N1 = [1.0,2.0,1.0]
N2 = [1.0,2.0,1.0]
A = np.zeros((node**2,node**2))

mapindex = np.zeros((node**2,node**2),dtype=np.int)


for i in range(node**2):
    mapindex[i/node,i%node] = i

for i in range(node):
    for j in range(node):        
        for u in range(node):
            for v in range(node):
                if (i,u) in E1 and (j,v) in E2:
                    A[mapindex[i,j],mapindex[u,v]] = 1.0/N1[u]/N2[v]
                    
                    
                
w2,v2 = np.linalg.eig(A)