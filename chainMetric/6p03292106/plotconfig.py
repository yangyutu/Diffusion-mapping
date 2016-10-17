# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:01:08 2015

@author: yuugangyang
"""

import pylab
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


for i in range(5,9):
    folder = str(i)+'b/'
    filename = '03_29_2016-6p-2Hzb' + str(i) +'.txt'
    data = np.genfromtxt(folder+filename)[:,2:4]
    
    datalen = data.shape[0]
    npart=6
    nframe = datalen/npart
    windowsize = 15000
    plt.close('all')
    for i in range(0,nframe,200):
        startp = i*npart
        endp  = startp + npart
        rx =data[startp:endp,0]
        ry =data[startp:endp,1]
        center = [np.mean(rx),np.mean(ry)]
        plt.figure(i)
        plt.plot(rx,ry,linestyle='None',marker='o')
        plt.xlim((center[0]-windowsize,center[0]+windowsize))
        plt.ylim((center[1]-windowsize,center[1]+windowsize))
        plt.savefig(folder+str(i)+'.png')
        plt.close()
    
