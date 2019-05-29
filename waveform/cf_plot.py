#!/usr/bin/env python
import numpy as np
import matplotlib.pylab as plt
import obspy,os

ct=np.array([5.,10.,15.,20.,25.,30.])
umin=1.5
umax=5
fig=plt.figure()
tmin=[0,1000/umax]
tmax=[0,1000/umin]
y=[0,1000]
norm_fac=5
x=np.arange(0,700,1)
for i in range(len(ct)):
    fig=plt.figure(figsize=(7,16))
    ax=fig.add_subplot(111)
    path='filter1/'+str(int(ct[i]))+'s'+'/*'
    seislst=obspy.read(path)
    for seis in seislst:
        dist=float(seis.stats.sac.dist)
        data=seis.data[:700]*norm_fac+dist
        ax.plot(x,data,color='black',linewidth=0.1,alpha=0.1)
    ax.plot(tmin,y,color='red')
    ax.plot(tmax,y,color='red')
    ax.set(xlabel='t(s)',ylabel='Distance(km)',ylim=[0,1000],title='Period:'+str(int(ct[i]))+'s')
    plt.savefig('filterfig/'+str(int(ct[i]))+'s.pdf')
    #plt.show()
    plt.close('all')
