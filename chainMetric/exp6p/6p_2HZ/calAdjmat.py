# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:28:01 2015

@author: yuugangyang
"""

import numpy as np
import scipy
import sklearn
from sklearn.metrics.pairwise import euclidean_distances
import pickle
from sklearn.utils.linear_assignment_ import linear_assignment
from fastMatching import *
permutationMatrix_set = pickle.load(open('permutation.p','rb'))

def getAdjMat(X,radius):
    thresh = 2.5
    Eud_dist = euclidean_distances(X,X)    
#    adj_mat = np.where(Eud_dist < radius*thresh, 1, 0)
    adj_mat = Eud_dist / radius   
#    adj_mat[Eud_dist > 3.0*radius] = 0
#    edge_weight = np.where(Eud_dist < radius*thresh, 1.0, np.exp(-(Eud_dist-thresh)/(0.5*radius)))
#    weight_adj_mat = edge_weight * adj_mat
#    adj_mat = adj_mat/radius
#    adj_mat = adj_mat - np.eye(npart,dtype=np.int)    
    return adj_mat


#folder = '16p_1/'
#names = ['09.23.2015-10G2Hz121.txt','09.23.2015-10G2Hz122.txt',
#'09.23.2015-10G2Hz123.txt','09.23.2015-10G2Hz124.txt',
#'09.23.2015-10G2Hz125.txt','09.23.2015-10G2Hz726.txt',
#'08.09.2015-10G50Hz-16p-300.txt',
#'08.13.2015-10G2Hz-16p.txt']
#data = np.genfromtxt(folder+names[6])[:,2:4]


def enumerateMatch(g1,g2):
    diff_set = []
    for H in permutationMatrix_set:
        g1_trans = np.dot(H,np.dot(g1,np.transpose(H)))
        diff = np.sum(np.abs(g1_trans - g2))/2
        diff_set.append(diff)
        if diff < 1e-6:
            break
    min_diff = np.min(np.array(diff_set))
    min_dix = np.argmin(np.array(diff_set))
    return min_diff

def getGraphDistMatrix(adj_mat_set,filename):
    graph_num = len(adj_mat_set)
#    graph_dist_matrix = np.zeros((graph_num,graph_num))
    graph_dist_matrix = np.zeros((graph_num,graph_num))
    for i in range(graph_num-1):
        for j in range(i+1,graph_num):
            print i,j
            g1 = adj_mat_set[i]
            g2 = adj_mat_set[j]        	                
            graph_dist_matrix[i,j] = enumerateMatch(g1,g2)
 #           if method == 'inexact':
 #               graph_dist_matrix_fast[i,j] = fastMatching(g1,g2)
 #           else:
 #               exit
            
    graph_dist_matrix = graph_dist_matrix + np.transpose(graph_dist_matrix)
#    graph_dist_matrix_fast = graph_dist_matrix_fast + np.transpose(graph_dist_matrix_fast)
#    print graph_dist_matrix - graph_dist_matrix_fast
#    print np.linalg.norm(graph_dist_matrix - graph_dist_matrix_fast)/graph_num
    pickle.dump(graph_dist_matrix,open(filename,'wb'))
	
if __name__ == '__main__':
	datalen = data.shape[0]
	npart=6
	nframe = datalen/npart
	radius = 1400
	adj_mat_set=[]
	Eud_mat_set=[]
	for i in range(0,nframe,20):
	    startp = i*6
	    endp  = startp + npart
	    rx =data[startp:endp,0]
	    ry =data[startp:endp,1]
	    X = data[startp:endp,0:2]
	    adj_mat = getAdjMat(X,radius)
	    adj_mat_set.append(adj_mat)
	#    Eud_mat_set.append(Eud_mat)
	
	bonds = [np.sum(adj)/2 for adj in adj_mat_set]
	getGraphDistMatrix(adj_mat_set,folder+'graph_dist_matrix_fullconnected_fast.p')