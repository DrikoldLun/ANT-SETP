#!/usr/bin/env python
from scipy.signal import windows, freqz
from scipy.fftpack import fft,ifft
import matplotlib.pylab as plt 
import numpy as np
fn = 8196
M = 1024
NW = 4
win, eigvals = windows.dpss(M, NW, 8, return_ratios=True)
w,h=np.zeros([len(win),fn]),np.zeros([len(win),fn],dtype='complex')
for i in range(len(win)):
    w[i],h[i]=freqz(win[i],worN=fn)
fig = plt.figure(figsize=(16,6))
rect1 = [0.05,0.1,0.35,0.8]
rect2 = [0.45,0.1,0.35,0.8]
ax1 = plt.axes(rect1)
ax2 = plt.axes(rect2)
'''
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(221)
'''
ax1.plot(win.T, linewidth=1.)
for i in range(len(win)):
    ax2.plot(w[i][1:]/(2*np.pi),20*np.log10(np.abs(h[i][1:])),linewidth=1.)
ax1.set(xlim=[0, M-1], xlabel='Time',title='DPSS, N=%d, NW0=%0.1f' % (M, NW))
ax2.set(xlim=[0,0.01],ylim=[-200,50],xlabel='Frequency',ylabel='Magnitude(dB)',title='Amp Spectrum')
ax1.legend(['win[%d] (%0.4f)' % (ii, ratio)
for ii, ratio in enumerate(eigvals)])
ax2.legend(['win[%d] (%0.4f)' % (ii, ratio)
for ii, ratio in enumerate(eigvals)])
plt.savefig('dpss.pdf')
plt.show()
