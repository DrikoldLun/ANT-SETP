#!/usr/bin/env python
import numpy as np
import obspy
from scipy.fftpack import fft,ifft
import matplotlib.pylab as plt

def analsig(data):
    fdata=fft(data)
    npts=np.ceil(0.5*len(data))
    f=np.zeros(len(data),dtype='complex')
    f[:npts]=2*fdata[:npts]
    analdata=np.abs(ifft(f))
    return analdata

seis=obspy.read('test.sac')[0]
t=np.arange(0,201,1)
envelop=analsig(seis.data[3601:3802])
plt.plot(t,seis.data[3601:3802],'r')
plt.plot(t,envelop,'b')
plt.show()
