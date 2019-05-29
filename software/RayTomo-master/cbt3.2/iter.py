#!/usr/bin/env python
import os
import numpy as np

lamda = np.array([0.1,0.5,1,5,10,50,100])
sigma = np.arange(20,300,20)
alpha = np.arange(50,500,50)
period = 20

for l in lamda:
    for s in sigma:
        for a in alpha:
            os.system('./RUNtest '+str(l)+' '+str(s)+' '+str(a)+' '+str(period)+' > run.log')
            os.system('sh station.sh '+str(l)+' '+str(s)+' '+str(a)+' '+str(period)+' >> run.log')
            os.system('rm TEST*')

