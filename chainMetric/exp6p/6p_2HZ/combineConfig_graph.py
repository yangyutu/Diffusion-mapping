# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 23:38:22 2015

@author: yuguangyang
"""
import numpy as np
from calAdjmat import *
import pickle
folders = ['A01132016_2Hz_6p1','A01132016_2Hz_6p2','A01132016_2Hz_6p4']
names = ['stackge.txt','stackge.txt','stackge.txt']
X_set =[]
nframe = [1200,1200,1200]
skip = [2,2,2]
pixel = 111.12
adj_mat_set=[]
npart = 6
radius = 1400
for ii in range(3):
    filename = folders[ii] + '/' + names[ii]
#    filename = '2\\' + names[1]	
    data = np.genfromtxt(filename)[:,2:4]
    for i in range(0,nframe[ii],skip[ii]):
        startp = i*6
        endp  = startp + npart
        rx =data[startp:endp,0]
        ry =data[startp:endp,1]
        X = data[startp:endp,0:2]*pixel
        adj_mat = getAdjMat(X,radius)
        adj_mat_set.append(adj_mat)


pickle.dump(adj_mat_set,open('combine_adj_mat.p','wb'))

getGraphDistMatrix(adj_mat_set,'graph_dist_matrix_fullconnected.p')