#!/usr/bin/env python
import sys,getopt
def Usage():
    print('python datapre1.1.py -Tperiod(s)')
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

j=0
path=r'../../../disp_mtm/data_filtered2/'
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
            tobs.append(float(line[0]))
            vobs.append(float(line[1]))
            err.append(float(line[6]))
        f.close()
    v0=0
    if len(tobs) == 0:
        continue
    for i in range(len(tobs)):
        if tobs[i] == T:
            v0=vobs[i]
            if err[i]<0.1:
                err[i]=0.1
            weight=1/err[i]
    if v0>1 and v0<6:
        j+=1
        seis=obspy.read(path+dir+'/*.sac')[0]
        stla=float(seis.stats.sac.stla)
        stlo=float(seis.stats.sac.stlo)
        evla=float(seis.stats.sac.evla)
        evlo=float(seis.stats.sac.evlo)
        line=str(j)+' '+str(evla)+' '+str(evlo)+' '+str(stla)+' '+str(stlo)+' '+str(v0)+' '+str(weight)+' 1'
        print(line)
        lines.append(line+'\n')

with open('data'+str(T)+'s.dat','w+') as f:
    f.writelines(lines)
    f.close()
