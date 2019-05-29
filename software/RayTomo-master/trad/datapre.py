#!/usr/bin/env python
import sys,getopt
def Usage():
    print('python datapre.py -Pperiod(s) -Sminsnr(dB)')
    sys.exit(1)
try:
    opts, args=getopt.getopt(sys.argv[1:],'P:S:')
except:
    print('Arguments are not found!')
    Usage()
if opts==[]:
    Usage()
for op,value in opts:
    if op=='-P':
        T=float(value)
    elif op=='-S':
        SNR=float(value)
    else:
        Usage()

import numpy as np
import os,obspy
from scipy.interpolate import splrep,splev

path=r'../../aftan-1.1/aftan-1.1/TEST2/ANTdata/stack/'
i=1
lines=[]
for dir in os.listdir(path):
    tobs=[]
    vobs=[]
    snr=[]
    filename=os.popen('ls '+path+dir+'/*_1_DISP.0').read().replace('\n','')
    with open(filename,'r') as f:
        for line in f.readlines():
            line=line.split()
            tobs.append(float(line[2]))
            vobs.append(float(line[3]))
            snr.append(float(line[7]))
        f.close()
    paixu=np.zeros([3,len(tobs)])
    paixu[0]=np.array(tobs)
    paixu[1]=np.array(vobs)
    paixu[2]=np.array(snr)
    paixu=paixu.T[np.lexsort(paixu[::-1,:])].T
    tobs=paixu[0]
    vobs=paixu[1]
    snr=paixu[2]
    tck1=splrep(tobs,vobs,k=3,s=0)
    tck2=splrep(tobs,snr,k=3,s=0)
    v0=splev(T,tck1,der=0)
    snr0=splev(T,tck2,der=0)
    if v0!=0 and snr0>SNR:
        seis=obspy.read(path+dir+'/*.sac')[0]
        stla=float(seis.stats.sac.stla)
        stlo=float(seis.stats.sac.stlo)
        evla=float(seis.stats.sac.evla)
        evlo=float(seis.stats.sac.evlo)
        line=str(i)+' '+str(evla)+' '+str(evlo)+' '+str(stla)+' '+str(stlo)+' '+str(v0)+' 1.0 1\n'
        i+=1
        lines.append(line)
        print(line)

with open('data'+str(T)+'s.dat','w') as f:
    f.seek(0)
    f.writelines(lines)
    f.close()
