# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:21:12 2015

@author: yuugangyang
"""

import numpy as np
import math
def getCornerPlane(N):
    xMax = int(math.floor(math.sqrt(N)));
    yMax = int(math.ceil(N/xMax));        
    liftAngle = 45
    cornerPoint = yMax/2;
    color = []
    X = np.empty((0,3))
    for x in range(xMax):
        for y in range(yMax):
            if y <= cornerPoint:
                X = np.append(X,[[x,y,0]],axis=0)
                color.append(y)
            else:
                X = np.append(X,[[x,cornerPoint+(y-cornerPoint)*math.cos(math.pi*liftAngle/180.0),(y-cornerPoint)*math.sin(math.pi*liftAngle/180)]],axis=0)
                color.append(y)
    length = len(color)
    color = np.array(color,dtype=np.float).reshape(length,1)
    
    return X,color
    
def getTwinPeaks(N):
    inc = 1.5 / math.sqrt(N)
    seq = np.arange(-1,1,inc)
    [xx,yy] = np.meshgrid(seq,seq)
    zz = np.sin(math.pi*xx)*np.tanh(3*yy);
    noise= (1-2*np.random.rand(len(seq),len(seq)))*0.1;
    zz = zz + noise
    n_elm = xx.size
    xx = xx.flatten().reshape(n_elm,1)
    yy = yy.flatten().reshape(n_elm,1)
    zz = zz.flatten().reshape(n_elm,1)
    color = zz
    return np.concatenate((xx,yy,zz),axis=1),color
    
if __name__ == '__main__':
    X,Y = getCornerPlane(800)
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    fig = plt.figure(1)
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(X[:,0],X[:,1],X[:,2],c=Y, cmap=plt.cm.Spectral)
    
    fig = plt.figure(2)
    X,Y = getTwinPeaks(800)
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(X[:,0],X[:,1],X[:,2],c=Y, cmap=plt.cm.Spectral)
        
    