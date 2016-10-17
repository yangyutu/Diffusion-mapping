# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:55:58 2015

@author: yuugangyang
"""

import numpy as np
import matplotlib.pyplot as plt
import math
def thresholdDistanceMatrix(dist_mat, epi = 1, mode = 'auto'):
    if mode == 'auto':
        epis = np.logspace(-5,5)
        sum_vec = []
        for epi in epis:
            dist_thresh = np.exp(-dist_mat**2/epi/2.0)
            sum_temp = math.log10(np.sum(dist_thresh))
            sum_vec.append(sum_temp)
        plt.figure(20)
        plt.plot(np.log10(epis),np.array(sum_vec))
        plt.xlabel('log(epsilon)')
        plt.ylabel('log(sum of M)')
        middle_sum = (sum_vec[0] + sum_vec[-1])/2.0
        sum_vec = np.array(sum_vec)
        diff = np.abs(sum_vec-middle_sum)
        idx = np.argmin(diff)
        epi = epis[idx]
                
    dist_thresh = np.exp(-dist_mat**2/epi/2.0)

    return dist_thresh,epi      
        
    