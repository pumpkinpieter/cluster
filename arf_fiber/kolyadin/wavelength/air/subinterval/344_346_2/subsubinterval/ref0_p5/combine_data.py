#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

B = []
D = []

for p in range(400):
    try:
        b = np.load('e'+str(p)+'.npy')
        B.append(b)
    except FileNotFoundError:
        D.append(p)
        pass

B = np.array(B)

np.save('all_e.npy', B)
print(*D)
