#!/usr/bin/env python
import os
import numpy as np
import matplotlib.pylab as plt
c0=3.
T=np.arange(2,41)
raynum=np.zeros(len(T))
with open('distcut.lst','r') as f:
    lines=f.readlines()
    f.close()
dist=[]
stats=[]
for line in lines:
    dist.append(float(line.split()[2]))
dist=np.array(dist)
for i in range(len(T)):
    t=T[i]
    for j in range(len(dist)):
        if c0*t<=dist[j]/3:
            raynum[i]+=1

raynum=np.array([26457,43095,46937,45201,37830,26550])
T=np.array([5,10,15,20,25,30])

fig = plt.figure(figsize=(4.5,4.5))
plt.bar(left=T,height=raynum,width=2,facecolor='black',edgecolor='white')
plt.xticks(np.arange(0,31,5))
plt.xlabel('period/s')
plt.ylabel('number of dispersion curves')
plt.savefig('nt.pdf')
plt.show()
