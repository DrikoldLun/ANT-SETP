import obspy
import numpy as np
ZDD=obspy.read('*ZDD.sac')[0]
ZEX=obspy.read('*ZEX.sac')[0]
tmp=ZDD.copy()
tmp.data=ZDD.data/3.+ZEX.data/3.
tmp.write('Mzz.sac','SAC')
