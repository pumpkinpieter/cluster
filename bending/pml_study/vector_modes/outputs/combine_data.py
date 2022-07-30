#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys

ref = sys.argv[1]

nus_suffix = 'nus.npy'
dofs_suffix = 'dofs.npy'

B = []
D = []

for p in range(35):
    try:
        b = np.load('ref'+ref+'p'+str(p)+nus_suffix)
        d = np.load('ref'+ref+'p'+str(p)+dofs_suffix)
        B.append(b)
        D.append(d[0])
    except FileNotFoundError:
        pass

B = np.array(B)
D = np.array(D)

np.save('ref'+ref+'all_nus.npy', B)
np.save('ref'+ref+'all_dofs.npy', D)
