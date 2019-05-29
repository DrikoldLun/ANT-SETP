#!/usr/bin/env python
import numpy as np
import obspy,os
from scipy.fftpack import fft,ifft,hilbert
import matplotlib.pylab as plt
dt=1.
T=7200.
df=1/T
trange=np.arange(3.,43.,3.)
ref=np.array([[0.,100.,250.,500.,1000.,2000.,4000.,20000.],[5.,8.,12.,20.,25.,35.,50.,75.]])
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

def analsig(data):
    fdata=fft(data)
    npts=np.ceil(0.5*len(data))
    f=np.zeros(len(data),dtype='complex')
    f[:npts]=2*fdata[:npts]
    analdata=np.abs(ifft(f))
    return analdata

def groupvel(seis,dist):
    umax=5.
    umin=1.5
    tmin=dist/umax
    tmax=dist/umin
    wave=analsig(seis.data)[3600:]
    wave[:tmin]=0
    wave[tmax:]=0
    t=wave.argmax()
    return dist/t

def snr(data,tmin,tmax):
    S=data[tmin:tmax].max()
    noi=data[tmax+500:tmax+1000]
    N=np.sqrt((noi**2).sum()/len(noi))
    return 20*np.log(S/N)

for file in os.listdir('data/'):
    seis=obspy.read('data/'+file)[0]
    dist=float(seis.stats.sac.dist)
    u=np.zeros(len(trange))
    seislst=[]
    i=0
    for t in trange:
        fc=1./t
        seistmp=seis.copy()
        seistmp.data=gauss_filter(seis.data,fc,dist)
        u[i]=groupvel(seistmp,dist)
        i+=1
        seislst.append(seistmp)

    tmax=int(dist/u.min()+2*t.max())
    tmin=int(dist/u.max()-t.max())
    if tmin<0:
        tmin=int(dist/(u.max()+1))
        i=0
        for seismo in seislst:
            y=seismo.data[3600:3800]
            plt.plot(np.arange(200),y/np.abs(y).max()+2.*i)
            i+=1
        plt.vlines(tmin,-1,2*i+1)
        plt.vlines(tmax,-1,2*i+1)
        plt.show()
        plt.close('all')
    for i in range(len(trange)):
        SNR=snr(seislst[i].data[3600:],tmin,tmax)
        if SNR >= 5:
            path='filter1/'+str(trange[i])+'s'
            if not os.path.exists(path):
                os.system('mkdir '+path)
            seislst[i].write(path+'/'+file,'SAC')
