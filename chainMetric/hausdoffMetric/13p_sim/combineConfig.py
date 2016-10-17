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
folders = ['1/','2/','3/']
names = ['02_16_2016d-13p-2Hz1.txt','02_16_2016d-13p-2Hz2.txt','02_16_2016d-13p-2Hz3.txt']
X_set =[]
nframe = [40000,40000,40000]
skip = [100,100,100]

testFlag = 1
if testFlag:
    nfrmae = [12000,0,0]
    skip = [500,0,0]
adj_mat_set=[]
Xset = []
npart = 13
radius = 1400
configMat = np.empty((0,2))
for ii in range(3):
    filename = folders[ii] + names[ii]
#    filename = '2\\' + names[1]
    data = np.genfromtxt(filename)[:,2:4]
    for i in range(0,nframe[ii],skip[ii]):
        startp = i*npart
        endp  = startp + npart
        X = data[startp:endp,0:2]/radius
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


pickle.dump(Xset,open('combine_config.p','wb'))

