# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 23:38:22 2015

@author: yuguangyang
"""
import numpy as np
import pylab
import matplotlib
import matplotlib.pyplot as plt
import pickle
folders = ['A01132016_2Hz_6p1','A01132016_2Hz_6p2','A01132016_2Hz_6p4']
names = ['stackge.txt','stackge.txt','stackge.txt']
X_set =[]
nframe = [1200,1200,1200]
skip = [2,2,2]
pixel = 111.12
testFlag = 0
if testFlag:
    nfrmae = [1200,0,0]
    skip = [60,0,0]
adj_mat_set=[]
Xset = []
npart = 6
radius = 1400
configMat = np.empty((0,2))
for ii in range(3):
    filename = folders[ii-1] + '/' + names[ii-1]
#    filename = '2\\' + names[1]
    data = np.genfromtxt(filename)[:,2:4]
    for i in range(0,nframe[ii],skip[ii]):
        startp = i*6
        endp  = startp + npart
        X = data[startp:endp,0:2]/radius*pixel
        X[:,0] = X[:,0] - np.mean( X[:,0])
        X[:,1] = X[:,1] - np.mean( X[:,1])
        Cov = np.dot(np.transpose(X),X)
        w, v = np.linalg.eig(Cov)
        maxIdx = np.argmax(w)
        if maxIdx == 0:
            transMat = v
        else:
            transMat = np.concatenate(([v[:,1]],[v[:,0]]),axis=0)
        tranX = np.dot(np.transpose(transMat),np.transpose(X))
        tranX = np.transpose(tranX)
        configMat = np.vstack((configMat,tranX))
        Xset.append(tranX)

        if testFlag:
            plt.figure(i)
            plt.plot(X[:,0],X[:,1],color='k',marker='o')
            plt.plot(tranX[:,0],tranX[:,1],color='r',marker='o')
            plt.xlim((-10,10))
            plt.ylim((-10,10))
            plt.savefig('config'+str(i)+'.png')

np.savetxt('combine_config6p.txt',configMat)
pickle.dump(Xset,open('combine_config.p','wb'))

