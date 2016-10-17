# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:47:49 2015

@author: yuugangyang
"""

from itertools import permutations
import numpy as np
import pickle

items = range(6)
permutation_set = [p for p in permutations(items)]

permutationMatrix_set = []


for idx in range(len(permutation_set)):
    H = np.zeros((6,6),dtype=np.int)
    for i,j in zip(items,permutation_set[idx]):
        H[i,j] = 1
    permutationMatrix_set.append(H)
    
pickle.dump(permutationMatrix_set,open('permutation.p','wb'))
