# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:10:53 2015

@author: yuugangyang
"""

import pylab
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from isomapReduction import *
from diffusemapReduction import *

def isomapAnalyzer(data, random_seq, orderdata):

    psi6 = orderdata[random_seq-1,4]
    rg = orderdata[random_seq-1,3]
    y, result = isomapReduction(data)

    fig = plt.figure(1)
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(y[:, 0], y[:, 1], np.ones(y[:,0].shape), c=rg, cmap=plt.cm.Spectral)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')
    
    fig = plt.figure(2)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 0], y[:, 1], c=rg, cmap=plt.cm.Spectral)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    
    fig = plt.figure(3)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 0],rg)
    ax.set_xlabel('x1')
    ax.set_ylabel('rg')
    
    fig = plt.figure(4)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 0],psi6)
    ax.set_xlabel('x1')
    ax.set_ylabel('psi6')
    
    fig = plt.figure(6)
    plt.plot(result['eigenvalues'])
    plt.xlabel('n')
    plt.xlabel('lambda')
    
    fig = plt.figure(7)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 1],rg)
    ax.set_xlabel('x2')
    ax.set_ylabel('rg')
    
    fig = plt.figure(8)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 1],psi6)
    ax.set_xlabel('x2')
    ax.set_ylabel('psi6')

    fig = plt.figure(8)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 1] + y[:,0],psi6)
    ax.set_xlabel('x2')
    ax.set_ylabel('psi6')
    
    fig = plt.figure(9)
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(y[:, 0], y[:, 1],  np.ones(y[:,0].shape), c=psi6, cmap=plt.cm.Spectral)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')

def diffusemapAnalyzer(data, random_seq, orderdata):
    psi6 = orderdata[random_seq-1,4]
    rg = orderdata[random_seq-1,3]
    y, result = diffusemapReduction(data,0.5)
    
 
    fig = plt.figure(1)
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(y[:, 0], y[:, 1], np.ones(y[:,0].shape), c=rg, cmap=plt.cm.Spectral)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')
    
    fig = plt.figure(2)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 0], y[:, 1], c=rg, cmap=plt.cm.Spectral)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    
    fig = plt.figure(3)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 0],rg)
    ax.set_xlabel('x1')
    ax.set_ylabel('rg')
    
    fig = plt.figure(4)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 0],psi6)
    ax.set_xlabel('x1')
    ax.set_ylabel('psi6')
    
    fig = plt.figure(6)
    plt.plot(result['eigenvalues'])
    plt.xlabel('n')
    plt.ylabel('lambda')
    
    fig = plt.figure(7)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 1],rg)
    ax.set_xlabel('x2')
    ax.set_ylabel('rg')
    
    fig = plt.figure(8)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 1] + y[:,0],psi6)
    ax.set_xlabel('x2')
    ax.set_ylabel('psi6')
    
    fig = plt.figure(9)
    ax = fig.add_subplot(111)
    ax.scatter(y[:, 0], y[:, 1], c=psi6, cmap=plt.cm.Spectral)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    
    fig = plt.figure(11)
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(y[:, 0], y[:, 1],y[:,2], c=rg, cmap=plt.cm.Spectral)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')
    
    
    fig = plt.figure(12)
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(y[:, 0], y[:, 1], y[:,2], c=psi6, cmap=plt.cm.Spectral)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')
#    plt.colorbar()
    
    np.savetxt('rg_sample.txt',rg)
    np.savetxt('psi6_sample.txt',psi6)
    np.savetxt('embedding.txt',y)
    np.savetxt('lambda.txt',result['eigenvalues'])    
    
    return result



if __name__ == '__main__':
    plt.close('all')
    data = np.genfromtxt('combined_dist_size_4074.txt')
#    data = np.genfromtxt('orient_dist.txt')   
    random_seq = np.genfromtxt('random_seq_size_4074.txt').astype(np.int)
#    random_seq = np.genfromtxt('orient_dist_randomSeq.txt').astype(np.int)
    orderdata = np.genfromtxt('info.txt')
#    result1 = isomapAnalyzer(data,random_seq,orderdata)
    result2 = diffusemapAnalyzer(data,random_seq,orderdata)

