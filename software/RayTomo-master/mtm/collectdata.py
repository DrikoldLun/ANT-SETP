#!/usr/bin/env python
import os
centra_t=[12.,15.,18.,20.,24.]
for i in range(len(centra_t)):
    os.system('nohup python -u datapre1.1.py -T'+str(int(centra_t[i]))+' 1> run'+str(i)+'.log 2> run'+str(i)+'.err &')
