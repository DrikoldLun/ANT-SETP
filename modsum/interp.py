#!/usr/bin/env python
import numpy as np
hstep=0.5
with open('W1.d','r') as f:
    tmp=f.readlines()
    f.close()
lines1=tmp[:12]
lines2=tmp[12:-1]
lines3=[tmp[-1]]
nlayer=[]
lines=[]
final=[]

for line in lines2:
    line1=line.replace('\n','').split()
    h=float(line1[0])
    nlayer.append(int(h/hstep))
    prefix=line.split(line1[0])[0]
    suffix=line.split(line1[0])[1]
    lines.append(prefix+'%.4f'%hstep+suffix)

for i in range(len(nlayer)):
    for j in range(nlayer[i]):
        final.append(lines[i])

with open('W3.d','w') as f:
    f.seek(0)
    f.writelines(lines1+final+lines3)
    f.close()
