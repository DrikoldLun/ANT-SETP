#!/usr/bin/env python
from scipy.signal import windows, freqz
from scipy.fftpack import fft,ifft
import matplotlib.pylab as plt 
import numpy as np

#theoretical spectrum
a=2.7607
b=-3.8106
c=2.6535
d=-0.9238
dt=1
x=np.zeros(1028)
w=np.arange(0,np.pi/dt,0.001)
f=w/(2*np.pi/dt)
z=np.exp(-1j*w*dt)
X=1/(1-a*z-b*pow(z,2)-c*pow(z,3)-d*pow(z,4))
PX=np.abs(X)
LPX=20*np.log10(PX)

x[0:4]=np.random.randn(4)
for i in range(4,1028):
    x[i]=a*x[i-1]+b*x[i-2]+c*x[i-3]+d*x[i-4]+np.random.randn(1)
x=x[4:1028]

fn = 8196
M = 1024
NW = 4
win, eigvals = windows.dpss(M, NW, 8, return_ratios=True)
newin = np.zeros([len(win),M])
w, wsum, wnew = np.zeros([len(win),fn]),np.zeros([len(win),fn]),np.zeros([len(win),fn])
h, hsum, hnew = np.zeros([len(win),fn],dtype='complex'), np.zeros([len(win),fn],dtype='complex'),np.zeros([len(win),fn],dtype='complex')
RC = np.zeros([len(win),M])

w0,h0=freqz(x,worN=fn)

fig=plt.figure(figsize=(14,10))
wid1=0.15
wid2=0.25
hei=0.18
ax=[]
for i in range(0,len(win)):
    bx1 = 0.05+(i%2)*0.5
    by1 = 0.75-(i/2)*0.22
    bx2 = bx1+0.18
    by2 = by1
    rect1=[bx1,by1,wid1,hei]
    rect2=[bx2,by2,wid2,hei]
    ax.append(plt.axes(rect1))
    ax.append(plt.axes(rect2))
    w[i],h[i]=freqz(win[i]*x,worN=fn)
    for j in range(0,i+1):
        hsum[i]+=h[j]/np.sqrt(eigvals[j])
        newin[i]+=win[j]/np.sqrt(eigvals[j])
    hsum[i]/=(i+1)
    wnew[i],hnew[i]=freqz(newin[i],worN=fn)
    newin[i]/=(j+1)

    ax[2*i].plot(w[i]/(2*np.pi),20*np.log10(np.abs(hnew[i])),linewidth=.5)
    ax[2*i].set(xlim=[0,0.01],ylim=[-100,40])
    ax[2*i+1].plot(w[i]/(2*np.pi),20*np.log10(np.abs(hsum[i]*np.sqrt(NW))),'b-',linewidth=.5)
    ax[2*i+1].plot(f,LPX,'r-',linewidth=.5)
    ax[2*i+1].set(ylim=[-50,50])
    ax[2*i+1].text(0.4,25,'K='+str(i+1))
    
#    ax[i].set(xlim=[0,0.02],title='stack number:'+str(i+1))

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
