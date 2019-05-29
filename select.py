#!/usr/bin/env python
import os
with open('disp/distcut.lst','r') as f:
    for line in f.readlines():
        line=line.split()
        os.system('cp -r /c/zhang_lun/data/ANTdata/stackFULL_SWC_X1TOX1_ZZ/*'+line[1]+'*'+line[0]+'* waveform/data1/'+line[1]+'to'+line[0])
    f.close()
