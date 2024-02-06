#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

B = []
D = []
I = []
for p in range(301):
    try:
        b = np.load('e'+str(p)+'.npy')
        B.append(b)
        I.append(p)
    except FileNotFoundError:
        D.append(p)
        pass

B = np.array(B)
print(*D)
np.save('all_wl.npy', B)
np.save('index.npy', I)
