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

folder = ['A01212016_2Hz_13p1/','A01212016_2Hz_13p2/','A01212016_2Hz_13p3/',
		'A01212016_2Hz_13p4/','A01212016_2Hz_13p5/','A01212016_2Hz_13p7/','A01212016_2Hz_13p8/']

folderpath=folder[6]
data = np.genfromtxt(folderpath+'stackge.txt')[:,2:4]*111.0/1400.0


datalen = data.shape[0]
npart=13
nframe = datalen/npart
windowsize = 15
plt.close('all')
for i in range(0,nframe,50):
    startp = i*npart
    endp  = startp + npart
    rx =data[startp:endp,0]
    ry =data[startp:endp,1]
    center = [np.mean(rx),np.mean(ry)]
    plt.figure(i)
    plt.plot(rx,ry,linestyle='None',marker='o')
    plt.xlim((center[0]-windowsize,center[0]+windowsize))
    plt.ylim((center[1]-windowsize,center[1]+windowsize))
    plt.savefig(folderpath+str(i)+'.png')
    plt.close()
    