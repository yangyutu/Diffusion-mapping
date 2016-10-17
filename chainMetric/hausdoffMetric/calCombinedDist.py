# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:02:53 2015

@author: yuugangyang
"""
import numpy as np

haud_dist = np.genfromtxt('Hausdoff_dist_rot.txt')
ori_dist = np.genfromtxt('orient_dist.txt')


haud_norm = np.linalg.norm(haud_dist)
ori_norm = np.linalg.norm(ori_dist)

ratio = haud_norm / ori_norm


print ratio

print haud_norm, ori_norm


#ratio = haud_norm / ori_norm

haud_dist = haud_dist / ratio


combined_dist = np.sqrt((haud_dist)**2 + 1.0*ori_dist**2)

np.savetxt('combined_dist.txt',combined_dist)

print np.linalg.norm(combined_dist)


