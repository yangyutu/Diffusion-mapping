# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:02:53 2015

@author: yuugangyang
"""
import numpy as np

haud_dist = np.genfromtxt('BD_data_dist_randomsample_size_4074.txt')
ori_dist = np.genfromtxt('orient_dist.txt')

sort_haud_dist = np.sort(haud_dist)
neighbor_sum_haud_dist = np.sum(sort_haud_dist[:,0:21],axis=1)
sort_ori_dist = np.sort(ori_dist)
neighbor_sum_ori_dist = np.sum(sort_ori_dist[:,0:21],axis=1)

neighbor_norm_haud = np.linalg.norm(neighbor_sum_haud_dist)
neighbor_norm_ori = np.linalg.norm(neighbor_sum_ori_dist)

ratio = neighbor_norm_haud / neighbor_norm_ori 

print ratio

haud_norm = np.linalg.norm(haud_dist)
ori_norm = np.linalg.norm(ori_dist)

ratio = haud_norm / ori_norm 


print ratio

print haud_norm, ori_norm


#ratio = haud_norm / ori_norm

haud_dist = haud_dist / ratio

print np.linalg.norm(haud_dist)


combined_dist = np.sqrt((haud_dist)**2 + 2.0*ori_dist**2)

np.savetxt('combined_dist_size_4074.txt',combined_dist)

print np.linalg.norm(combined_dist)


