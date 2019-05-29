#!/usr/bin/env python
import os
import obspy
lat={}
lon={}
path=r'../ANTdata/stackFULL_SWC_X1TOX1_ZZ/'
for dir in os.listdir(path):
    seis=obspy.read(path+dir+'/*.sac')[0]
    sta1=int(seis.stats.sac.kstnm)
    sta2=int(seis.stats.sac.kevnm.split()[1])
    lat[sta1]=float(seis.stats.sac.stla)
    lat[sta2]=float(seis.stats.sac.evla)
    lon[sta1]=float(seis.stats.sac.stlo)
    lon[sta2]=float(seis.stats.sac.evlo)

index=lat.keys()
index.sort()
lines=[]
for sta in index:
    lines.append(str(sta)+' '+str(lat[sta])+' '+str(lon[sta])+'\n')

with open('ANTsta.lst','w') as f:
    f.writelines(lines)
    f.close()
