#!/usr/bin/env python
import os
import numpy as np

lamda = 0.1
sigma = 500
alpha = 1000
period = np.array([12.,15.,18.,20.,24.])
step=[1.6,0.8,0.4]

for i in range(len(period)):
    os.system('python initmod.py -M1 -P0')
    name='TEST_'+str(lamda)+'_'+str(sigma)+'_'+str(alpha)+'_'+str(int(period[i]))
    for j in range(len(step)):
        os.system('./RUNtest '+str(lamda)+' '+str(sigma)+' '+str(alpha)+' '+str(int(period[i]))+' '+str(step[j])+' > run.log')
        os.system('python initmod.py -M0 -P'+name)
    os.system('mv resomatrix.dat '+name+'_reso.dat')
    print(name+' succeed!')
