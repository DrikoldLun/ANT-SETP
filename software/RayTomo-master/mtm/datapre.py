#!/usr/bin/env python
import sys,getopt
def Usage():
    print('python datapre.py -Tperiod(s)')
    sys.exit(1)
try:
    opts, args=getopt.getopt(sys.argv[1:],'T:')
except:
    print('Arguments are not found!')
    Usage()
if opts==[]:
    Usage()
for op,value in opts:
    if op=='-T':
        T=float(value)
    else:
        Usage()

import numpy as np
import os,obspy
from scipy.interpolate import splrep,splev

path=r'../../../disp_mtm/data_filtered1/'
i=1
lines=[]
for dir in os.listdir(path):
    dispfile = path+dir+'/disp.dat'
    if not os.path.exists(dispfile):
        continue
    tobs=[]
    vobs=[]
    err=[]
    with open(dispfile,'r') as f:
        for line in f.readlines():
            line=line.replace('\n','').split()
            tobs.append(1/float(line[0]))
            vobs.append(float(line[1]))
            err.append(float(line[2]))
        f.close()
    paixu=np.zeros([3,len(tobs)])
    paixu[0]=np.array(tobs)
    paixu[1]=np.array(vobs)
    paixu[2]=np.array(err)
    paixu=paixu.T[np.lexsort(paixu[::-1,:])].T
    tobs=paixu[0]
    vobs=paixu[1]
    err=paixu[2]
    tck1=splrep(tobs,vobs,k=3,s=0)
#    tck2=splrep(tobs,err,k=3,s=0)
    v0=splev(T,tck1,der=0)
#    err0=splev(T,tck2,der=0)
    err0 = np.mean(err)
    weight = 1/err0
    if v0 < 6 and v0 > 1 :
        seis=obspy.read(path+dir+'/*.sac')[0]
        stla=float(seis.stats.sac.stla)
        stlo=float(seis.stats.sac.stlo)
        evla=float(seis.stats.sac.evla)
        evlo=float(seis.stats.sac.evlo)
        line=str(i)+' '+str(evla)+' '+str(evlo)+' '+str(stla)+' '+str(stlo)+' '+str(v0)+' '+str(weight)+' 1'
        i+=1
        lines.append(line+'\n')
        print(i)

with open('data'+str(T)+'s.dat','w+') as f:
    f.writelines(lines)
    f.close()
