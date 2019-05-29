#!/usr/bin/env python
from scipy.signal import windows, freqz
from scipy.fftpack import fft,ifft
import matplotlib.pylab as plt 
import numpy as np
import obspy
M = 512
NW = 4
win, eigvals = windows.dpss(M, NW, 5, return_ratios=True)
fig, ax = plt.subplots(1)
ax.plot(win.T, linewidth=1.)
ax.set(xlim=[0, M-1], ylim=[-0.1, 0.1], xlabel='Samples',title='DPSS, M=%d, NW=%0.1f' % (M, NW))
ax.legend(['win[%d] (%0.4f)' % (ii, ratio)
for ii, ratio in enumerate(eigvals)])
fig.tight_layout()
plt.savefig('dpss.pdf')
plt.show()
