#!/usr/bin/env python
import os
import numpy as np

lamda = 0.1
sigma = np.arange(25,300,25)
alpha = 100
period = 20
for s in sigma:
    os.system('./RUNtest '+str(lamda)+' '+str(s)+' '+str(alpha)+' '+str(period)+' > run.log')
    os.system('sh station.sh '+str(lamda)+' '+str(s)+' '+str(alpha)+' '+str(period)+' >> run.log')

