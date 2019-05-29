#!/usr/bin/env python
import os
import numpy as np
for t in np.arange(3.,42.,3.):
    os.system('sh arange.sh '+str(t))
