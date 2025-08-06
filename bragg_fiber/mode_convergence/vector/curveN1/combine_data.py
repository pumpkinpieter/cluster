#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys

ref = sys.argv[1]

beta_suffix = 'betas.npy'
dofs_suffix = 'dofs.npy'

B = []
D = []

for p in range(35):
    try:
        b = np.load('outputs/ref'+ref+'p'+str(p)+beta_suffix)
        d = np.load('outputs/ref'+ref+'p'+str(p)+dofs_suffix)
        B.append(b)
        D.append(d[0])
    except FileNotFoundError:
        pass

B = np.array(B)
D = np.array(D)

np.save('outputs/ref'+ref+'all_betas.npy', B)
np.save('outputs/ref'+ref+'all_dofs.npy', D)
