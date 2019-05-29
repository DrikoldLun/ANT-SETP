#!/usr/bin/env python
from scipy.signal import windows, freqz
from scipy.fftpack import fft,ifft
import matplotlib.pylab as plt 
import numpy as np
fn = 8192
M = 64
NW = 4
win, eigvals = windows.dpss(M, NW, 8, return_ratios=True)
newin = np.zeros([len(win),M])
w = np.zeros([len(win),fn])
h = np.zeros([len(win),fn],dtype='complex')

for i in range(0,len(win)):
    for j in range(0,i+1):
        newin[i]+=win[j]/eigvals[j]
    newin[i]/=(j+1)
    
for i in range(len(win)):
    w[i],h[i]=freqz(newin[i],worN=fn)

fig = plt.figure(figsize=(14,5))
ax=[]
for i in range(len(win)):
    rect = [0.05+(i%4)*0.2,0.55-0.5*(i/4),0.15,0.4]
    ax.append(plt.axes(rect))
#    ax.append(fig.add_subplot(len(win),1,i+1))
    ax[i].plot(w[i]/(2*np.pi),20*np.log10(np.abs(h[i])),linewidth=1.)
    ax[i].set(xlim=[0,0.2],ylim=[-150,30],title='stack number:'+str(i+1))

plt.savefig('stack.pdf')
plt.show()

'''
ax1.plot(win.T, linewidth=1.)
for i in range(len(win)):
    ax2.plot(w[i]/(2*np.pi),20*np.log10(np.abs(h[i])),linewidth=1.)
ax1.set(xlim=[0, M-1], xlabel='Time',title='DPSS, M=%d, NW0=%0.1f' % (M, NW))
ax2.set(xlim=[0,0.5],ylim=[-200,50],xlabel='Frequency',ylabel='Magnitude(dB)',title='Amp Spectrum')
ax1.legend(['win[%d] (%0.4f)' % (ii, ratio)
for ii, ratio in enumerate(eigvals)])
ax2.legend(['win[%d] (%0.4f)' % (ii, ratio)
for ii, ratio in enumerate(eigvals)])
fig.tight_layout()
plt.savefig('dpss.pdf')
plt.show()
'''
