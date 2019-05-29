#!/usr/bin/env python
import numpy as np
v=2.878
lines=[]
for i in np.arange(-89,90):
    for j in np.arange(0,360):
        lines.append(str(j)+' '+str(i)+' '+str(v)+'\n')

with open('init.mod','w') as f:
    f.seek(0)
    f.writelines(lines)
    f.close()
