#!/usr/bin/env python
import os
import numpy as np

lamda = 0.1
sigma = 200
alpha = 1000
period = np.array([5.,10.,15.,20.,25.,30.])
step=[]
for i in range(len(period)):
    if i == 0:
       step.append([2.4,1.2,0.6,0.3])
    elif i== 5:
        step.append([1.5,1,0.5])
    else:
        step.append([1.6,0.8,0.4])

for i in range(len(period)):
    os.system('python initmod.py -M1 -P0')
    name='TEST_'+str(lamda)+'_'+str(sigma)+'_'+str(alpha)+'_'+str(int(period[i]))
    for j in range(len(step[i])):
        os.system('./RUNtest '+str(lamda)+' '+str(sigma)+' '+str(alpha)+' '+str(int(period[i]))+' '+str(step[i][j])+' > run.log')
        os.system('python initmod.py -M0 -P'+name)
    os.system('mv resomatrix.dat '+'reso'+str(int(period[i]))+'s.dat')
    print(name+' succeed!')
