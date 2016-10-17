# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 21:32:32 2015

@author: yuugangyang
"""
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.utils.linear_assignment_ import linear_assignment
def fastMatching(g1,g2):
    # g1 and g2 are adj matrix for graph 1 and graph2
	n_row = g1.shape[0]
	edge_sum_1 = np.sum(g1,axis=1).reshape(n_row,1)
	edge_sum_2 = np.sum(g2,axis=1).reshape(n_row,1)
	Eud_dist = euclidean_distances(edge_sum_1,edge_sum_2)
	assignment = linear_assignment(Eud_dist)
	diff = 0.0   
	for i,j in assignment:
		diff = diff + Eud_dist[i,j]/2.0
        
#    g1_trans = np.dot(H,np.dot(g1,np.transpose(H)))
#    diff = np.sum(np.abs(g1_trans - g2))/2
	return diff
    
    

    
    
    
    
    