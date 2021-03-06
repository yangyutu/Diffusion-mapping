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

folder = '1/'
names = ['09.23.2015-10G2Hz121.txt','09.23.2015-10G2Hz122.txt',
'09.23.2015-10G2Hz123.txt','09.23.2015-10G2Hz124.txt',
'09.23.2015-10G2Hz125.txt','09.23.2015-10G2Hz726.txt',
'08.09.2015-10G50Hz-16p-300.txt',
'08.13.2015-10G2Hz-16p.txt']

name_dict = {}
name_dict['1/'] = '02_16_2016d-13p-2Hz1.txt'
name_dict['2/'] = '02_16_2016d-13p-2Hz2.txt'
name_dict['3/'] = '02_16_2016d-13p-2Hz3.txt'
name_dict['4/'] = '02_16_2016d-13p-2Hz4.txt'
name_dict['5/'] = '02_16_2016d-13p-2Hz5.txt'
name_dict['6/'] = '02_16_2016d-13p-2Hz6.txt'
data = np.genfromtxt(folder+name_dict[folder])[:,2:4]

datalen = data.shape[0]
npart=13
nframe = datalen/npart
windowsize = 25000
plt.close('all')
for i in range(0,nframe,500):
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
    