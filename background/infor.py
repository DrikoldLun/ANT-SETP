#!/usr/bin/env python
import os
import obspy
import numpy as np

def day2date(year,day):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if ( year%4 == 0 and year%100 != 0) or (year%400 == 0): 
        days[1] = 29
    month=0
    while day>0:
        month+=1
        day-=days[month-1]
    monthday=day+days[month-1]
    return month,monthday

def egf(seis):
    npts=int(seis.stats.npts)
    data1=seis.data[:int(npts/2)]
    data2=seis.data[int(npts/2)+1:]
    data2=data2+data1[::-1]
    data2=data2/2
    data=np.hstack((np.array(seis.data[int(npts/2)+1]),data2))
    green=np.zeros(len(data)-1)
    for i in range(len(data)-1):
        green[i]=data[i+1]-data[i] 
    seis.data=green
    return seis

def snr(seis,vmin,vmax):
    data=seis.data
    dist=float(seis.stats.sac.dist)
    tmin=int(dist/vmax)
    tmax=int(dist/vmin)
    S=np.abs(data[tmin:tmax]).max()
    noi=data[tmax+500:tmax+1000]
    N=np.sqrt((noi**2).sum()/len(noi))
    return S/N

path=r'../ANTdata/stackFULL_SWC_X1TOX1_ZZ/'
lines=[]

for dir in os.listdir(path):
    seis=obspy.read(path+dir+'/*.sac')[0].copy()
    star=int(seis.stats.sac.kstnm)
    stas=int(seis.stats.sac.kevnm.split()[1])
    dist=float(seis.stats.sac.dist)
    #year=int(seis.stats.sac.nzyear)
    #day=int(seis.stats.sac.nzjday)
    #hour=int(seis.stats.sac.nzhour)
    #minu=int(seis.stats.sac.nzmin)
    #sec=int(seis.stats.sac.nzmsec)
    #month,monthday=day2date(year,day)
    SNR=snr(egf(seis),1.5,5)
    line=dir+' '+str(star)+' '+str(stas)+' '+str(dist)+' '+str(SNR)+'\n'
    #line=dir+' '+str(star)+' '+str(stas)+' '+str(year)+' '+str(day)+' '+str(month)+' '+str(monthday)+' '+str(hour)+':'+str(minu)+':'+str(sec)+' '+str(SNR)+'\n'
    lines.append(line)

with open('infor.dat','w') as f:
    f.seek(0)
    f.writelines(lines)
    f.close()
