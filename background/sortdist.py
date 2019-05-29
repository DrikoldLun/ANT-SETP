#!/usr/bin/env python

sorted_lines=sorted(open('infor.dat'),key=lambda s: float(s.split()[3]))
with open('infor_sorted.dat','w+') as f:
    f.writelines(sorted_lines)
f.close()

