#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

B = []
where = []
for p in range(500):
    try:
        b = np.load('wl'+str(p)+'.npy')
        B.append(b)
        where.append([p])
    except FileNotFoundError:
        pass

B = np.array(B)
W = np.array(where)
np.save('all_wl.npy', B)
np.save('mask.npy', W)
