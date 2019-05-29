#!/usr/bin/env python
import numpy as np
import matplotlib.pylab as plt
import os

def gauss(x, y, A, sig, x0, y0):
    return A*np.exp(-(pow(x-x0,2)+pow(y-y0,2))*0.5/pow(sig,2))

def map(A, sig, gridsize, step, blat, elat, blon, elon):
    lat0lst = np.arange(blat, elat+gridsize, gridsize)
    lon0lst = np.arange(blon, elon+gridsize, gridsize)
    latlst = np.arange(blat, elat, step)
    lonlst = np.arange(blon, elon, step)
    value = np.zeros([len(lonlst),len(latlst)], dtype='float')
    op = np.zeros([len(lon0lst), len(lat0lst)], dtype='float')
    lines = []
    for i in range(len(lon0lst)):
        if i%2 == 0:
            op[i,0] = -1
        else:
            op[i,0] = 1
    for j in range(1,len(lat0lst)):
        op[:,j] = -op[:,j-1]
    for x in range(len(lonlst)):
        for y in range(len(latlst)):
            value[x, y] = 3
            lon, lat = lonlst[x], latlst[y]
            for x0 in range(len(lon0lst)):
                for y0 in range(len(lat0lst)):
                    lon0, lat0 = lon0lst[x0], lat0lst[y0]
            #if np.sqrt(pow(lon-lon0,2)+pow(lat-lat0,2)) > 2*gridsize:
            #    continue
                    value[x, y] += op[x0, y0]*gauss(lon, lat, A, sig, lon0, lat0)
            lines += str(x)+' '+str(y)+' '+str(lon)+' '+str(lat)+' '+str(value[x, y])+'\n'
    with open('cbt_model3.2.dat', 'w+') as f:
        f.writelines(lines)
        f.close()
    os.system('sh plot.sh')

    #fig = plt.figure()
    #ax = fig.add_subplot(1,1,1)
    #extent = [0, x, 0, y]
    #levels = np.arange(2.5,3.5,0.01)
    #cs = ax.contourf(value, levels, origin='lower', extent=extent, cmap=plt.cm.prism)
    #plt.show()

#map(0.7, 0.3, 0.6, 0.025, 20.5, 29.5, 97, 108) #0.4
#map(0.7, 0.5, 1, 0.025, 20.5, 29.5, 97, 108) #0.8
#map(0.7, 0.9, 1.8, 0.025, 20.5, 29.5, 97, 108) #1.6
map(0.7, 1.7, 3.4, 0.025, 20.5, 29.5, 97, 108) #3.2
