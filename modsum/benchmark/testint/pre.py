import obspy,os
import numpy as np

for file in os.popen('ls *.sac').read()[:-1].split('\n'):
    tmp = obspy.read(file)[0]
    tmp.data=tmp.data/abs(tmp.data).max()
    tmp.write(file,'SAC')
