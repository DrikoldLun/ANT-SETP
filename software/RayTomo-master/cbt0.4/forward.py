#!/usr/bin/env python
import numpy as np
from numpy import sin, cos, arcsin, arccos, arctan2, deg2rad, rad2deg, pi

stalst = r'../../../background/ANTsta.lst'

def km2deg(km):
    radius = 6371
    circum = 2*pi*radius
    conv = circum / 360
    return km/conv

def deg2km(deg):
    radius = 6371
    circum = 2*pi*radius
    conv = circum / 360
    return deg*conv

def distance(lat1, lon1, lat2, lon2):
    radius = 6371
    lat1, lon1, lat2, lon2 = map(deg2rad, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat*0.5)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    dis = rad2deg(2*arcsin(np.sqrt(a)))

    y = sin(lon2-lon1)*cos(lat2)
    x = cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(lon2-lon1)
    brng = rad2deg(arctan2(y,x))
    azi = (brng+360.0)%360.0

    return dis, azi

def latlon_from(lat1,lon1,azimuth,distance):
    #distance must be an array
    gcarc_dist = km2deg(distance)
    lat1, lon1, azimuth, gcarc_dist = map(deg2rad, [lat1, lon1, azimuth, gcarc_dist])
    lat2 = arcsin((sin(lat1)*cos(gcarc_dist))+(cos(lat1)*sin(gcarc_dist)*cos(azimuth)))
    lon2 = np.zeros(len(gcarc_dist))
    for n in range(len(gcarc_dist)):
        if cos(gcarc_dist[n]) >= cos(pi/2-lat1)*cos(pi/2-lat2[n]):
            lon2[n] = lon1 + arcsin(sin(gcarc_dist[n])*sin(azimuth)/cos(lat2[n]))
        else:
            lon2[n] = lon1 + arcsin(sin(gcarc_dist[n])*sin(azimuth)/cos(lat2[n]))+pi
    return rad2deg(lat2), rad2deg(lon2)

sta=[]
with open(stalst, 'r') as f:
    for line in f.readlines():
        line = line.replace('\n','').split()
        sta.append([float(line[1]),float(line[2])])
    f.close()
sta = np.array(sta)

xx = []
yy = []
vv = []
with open('cbt_model.dat', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n','').split()
        xx.append(int(line[0]))
        yy.append(int(line[1]))
        vv.append(float(line[4]))
    f.close()
c0 = np.zeros([max(xx)+1, max(yy)+1],dtype='float')
for i in range(len(xx)):
    c0[xx[i], yy[i]] = vv[i]

blat, blon, elat, elon = 20.5, 97, 29.5, 108
step = 0.025
ninter = 1000
i = 0
lines = []
for sta1 in range(len(sta)-1):
    for sta2 in range(sta1+1, len(sta)):
        i+=1
        print(i)
        dis, azi = distance(sta[sta1][0],sta[sta1][1],sta[sta2][0],sta[sta2][1])
        dis = deg2km(dis)
        line_width = dis/(ninter -1)
        line_range = np.arange(0,dis,line_width)
        line_lat, line_lon = latlon_from(sta[sta1][0],sta[sta1][1],azi,line_range)
        path_c0 = np.zeros(len(line_lat))
        for index in range(len(line_lat)):
            path_c0[index] = c0[int((line_lon[index]-blon)/step),int((line_lat[index]-blat)/step)]
        dt = (1./path_c0).sum()*line_width
        c_mixed = dis/dt
        line = str(int(i))+' '+str(sta[sta1][0])+' '+str(sta[sta1][1])+' '+str(sta[sta2][0])+' '+str(sta[sta2][1])+' '+str(c_mixed)+' 1.0 1\n'
        lines.append(line)
with open('cbt_forward_data.dat','w+') as f:
    f.writelines(lines)
    f.close()
