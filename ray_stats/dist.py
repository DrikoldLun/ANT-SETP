#!/usr/bin/env python
import os
import obspy
lat={}
lon={}
lines=[]
path=r'/c/zhang_lun/data/ANTdata/stackFULL_SWC_X1TOX1_ZZ/'
for dir in os.listdir(path):
    seis=obspy.read(path+dir+'/*.sac')[0]
    sta1=seis.stats.sac.kstnm
    sta2=seis.stats.sac.kevnm.split()[1]
    dist=float(seis.stats.sac.dist)
    arc=float(seis.stats.sac.gcarc)
    line=sta1+' '+sta2+' '+str(dist)+' '+str(arc)+'\n'
    lines.append(line)

with open('dist.lst','w') as f:
    f.seek(0)
    f.writelines(lines)
    f.close()
