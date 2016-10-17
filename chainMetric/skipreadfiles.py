# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:34:25 2015

@author: yuugangyang
"""

folder = 'BD/13p/1/'
names = ['09.23.2015-10G2Hz121.txt','09.23.2015-10G2Hz122.txt',
'09.23.2015-10G2Hz123.txt','09.23.2015-10G2Hz124.txt',
'09.23.2015-10G2Hz125.txt','09.23.2015-10G2Hz726.txt',
'08.09.2015-10G50Hz-16p-300.txt',
'08.13.2015-10G2Hz-16p.txt']

name_dict = {}
name_dict['BD/16p/1/'] = '06.19.2015-10G50Hz-16p-line60.txt'
name_dict['BD/9p/1/'] = '06.19.2015-10G50Hz-9p-line60.txt'
name_dict['BD/13p/1/'] = '11.05.2015-10G2Hz13p.txt'
#data = np.genfromtxt(folder+name_dict[folder])[:,2:4]
skip = 20
npart = 13
files = open(folder+name_dict[folder],'r')
output = folder+name_dict[folder] + 'skip'+str(skip)+'.txt'
outputfile = open(output,'w')
counter = 0
for line in files:
    res = counter % (skip*npart)
    mult = res / npart
    counter = counter + 1    
    if mult < 1:
        outputfile.write(line)
print counter
files.close()
outputfile.close()        
