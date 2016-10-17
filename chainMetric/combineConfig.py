# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 23:38:22 2015

@author: yuguangyang
"""
import numpy as np
from calAdjmat import *
import pickle
folders = [1,4,6]
names = ['09.23.2015-10G2Hz121.txt','09.23.2015-10G2Hz122.txt',
'09.23.2015-10G2Hz123.txt','09.23.2015-10G2Hz124.txt','09.23.2015-10G2Hz125.txt','09.23.2015-10G2Hz726.txt']
X_set =[]
nframe = [12000,20000,14000]
skip = [20,40,20]
adj_mat_set=[]
npart = 6
radius = 1400
for ii in range(3):
    filename = str(folders[ii]) + '/' + names[folders[ii]-1]
#    filename = '2\\' + names[1]	
    data = np.genfromtxt(filename)[:,2:4]
    for i in range(0,nframe[ii],skip[ii]):
        startp = i*6
        endp  = startp + npart
        rx =data[startp:endp,0]
        ry =data[startp:endp,1]
        X = data[startp:endp,0:2]
        adj_mat = getAdjMat(X,radius)
        adj_mat_set.append(adj_mat)


pickle.dump(adj_mat_set,open('combine_adj_mat.p','wb'))

getGraphDistMatrix(adj_mat_set,'combined/graph_dist_matrix_fullconnected_fast.p')