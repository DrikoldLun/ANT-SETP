#!/usr/bin/env python
import numpy as np
import obspy, os
from scipy.fftpack import fft,ifft
cc_fold = r'../ANTdata/stackFULL_SWC_X1TOX1_ZZ/'
egf_fold = r'../disp_mtm/data/'
infor_file = r'../background/infor_sorted.dat'
T=1023.
df=1./T

dirs = []
rsta = []
ssta = []
dist = []

ct=np.array([5.,10.,15.,20.,25.,30.])
ref=np.array([[0.,100.,250.,500.,1000.,2000.,4000.,20000.],[5.,8.,12.,20.,25.,35.,50.,75.]])

'''
def egf(seis0,M):
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
#    vgreen=np.zeros(len(green)-1)
#    for i in range(len(green)-1):
#        vgreen[i]=green[i+1]-green[i]
    seis.data=green[:M]
    return seis
'''

def gauss_filter(data,fc,dist):
    a=np.interp(dist,ref[0],ref[1])
    npts1=int(np.ceil(len(data)/2.))
    f=df*np.arange(0,npts1)
    gauss=np.zeros(len(data),dtype='float')
    gauss1=np.exp(-a*((f-fc)/fc)**2)
    fdata=fft(data)
    fdata1=np.zeros(len(data),dtype='complex')
    gauss[0:npts1]=gauss1
    gauss[npts1:]=np.flipud(gauss[:int(len(data)/2.)])
    fdata1=fdata*gauss
    data1=ifft(fdata1).real
    return data1
    
#egf
dirs=os.listdir(egf_fold)

for i in range(3000):
    name=dirs[i]
    seis = obspy.read(egf_fold+name+'/obs.sac')[0]
    dist = float(seis.stats.sac.dist)
    for j in range(len(ct)):
        targpath='filter1/'+str(int(ct[j]))+'s'
        if not os.path.exists(targpath):
            os.system('mkdir '+targpath)
        seis1=seis.copy()
        seis1.data=gauss_filter(seis.data.copy(),1/ct[j],dist)
        seis1.data/=np.abs(seis1.data).max()
        seis1.write(targpath+'/'+name+'.sac','SAC')
    print(str(i)+' succeed')
