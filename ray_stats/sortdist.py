#!/usr/bin/env python

sorted_lines=sorted(open('dist.lst'),key=lambda s: float(s.split()[2]))
with open('dist_sorted.lst','w+') as f:
    f.writelines(sorted_lines)
    f.close()
