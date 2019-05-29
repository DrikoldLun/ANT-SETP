#!/usr/bin/env python
import subprocess, os, obspy
import numpy as np
dir=r'400/'

def vegf(seis0,M):
        seis=seis0.copy()
        npts=int(seis.stats.npts)
        data1=seis.data[:int(npts/2)]
        data2=seis.data[int(npts/2)+1:]
        data2=data2+data1[::-1]
        data2=data2/2
        data=np.hstack((np.array(seis.data[int(npts/2)+1]),data2))
        green=np.zeros(len(data)-1)
        for i in range(len(data)-1):
            green[i]=-data[i+1]+data[i]
        vgreen=np.zeros(len(green)-1)
        for i in range(len(green)-1):
            vgreen[i]=green[i+1]-green[i]
        seis.data=vgreen[:M]
        return seis

for seisname in os.popen('ls 400*.sac').read().split('\n')[:-1]:
    seis0=obspy.read(seisname)[0]
    seis=vegf(seis0,1024)
    seis.write(dir+seisname,'SAC')

os.putenv("SAC_DISPLAY_COPYRIGHT",'0')
p=subprocess.Popen(['sac'],stdin=subprocess.PIPE)
s='r '+dir+'*\n'
s+='ch b 0\n'
s+='wh\n'
s+='q\n'
p.communicate(s.encode())
