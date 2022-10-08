#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

B = []
M = []
for p in range(200):
    try:
        b = np.load('e'+str(p)+'.npy')
        B.append(b)
    except FileNotFoundError:
        print("Missing data for index ", p, '\n')
        M.append(p)
        pass

B = np.array(B)
print(M)
np.save('all_e.npy', B)
