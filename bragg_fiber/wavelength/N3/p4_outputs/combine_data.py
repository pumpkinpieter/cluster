#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

B = []

for p in range(301):
    try:
        b = np.load('e'+str(p)+'.npy')
        B.append(b)
    except FileNotFoundError:
        pass

B = np.array(B)

np.save('all_wl.npy', B)
