#Created on Mon Oct 26 23:38:22 2015

#@author: yuguangyang

import numpy as np
from calAdjmat import *
import pickle
folders = [1,4,6]
names = ['SD/13p/1/11.04.2015-10G2Hz1.txt','BD/13p/1/11.05.2015-10G2Hz13p.txtskip20.txt']
X_set =[]
nframe = [30000,15000]
skip = [50,50]
adj_mat_set=[]
npart = 13
radius = 1400
for ii in range(2):
    filename = names[ii]
#    filename = '2\\' + names[1]	
    data = np.genfromtxt(filename)[:,2:4]
    for i in range(0,nframe[ii],skip[ii]):
        startp = i*npart
        endp  = startp + npart
        rx =data[startp:endp,0]
        ry =data[startp:endp,1]
        X = data[startp:endp,0:2]
        adj_mat = getAdjMat(X,radius)
        adj_mat_set.append(adj_mat)


pickle.dump(adj_mat_set,open('combined_13p/combine_adj_mat.p','wb'))

getGraphDistMatrix(adj_mat_set,'combined_13p/graph_dist_matrix_fullconnected_fast.p','inexact')