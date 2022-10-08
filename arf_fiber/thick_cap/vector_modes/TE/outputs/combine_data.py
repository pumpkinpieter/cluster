#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys

ref = sys.argv[1]

beta_suffix = 'betas.npy'
dofs_suffix = 'dofs.npy'

B = []
D = []

for p in range(100):
    try:
        b = np.load('ref'+ref+'p'+str(p)+beta_suffix)
        d = np.load('ref'+ref+'p'+str(p)+dofs_suffix)
        B.append(b.imag)
        D.append(d[0])
    except FileNotFoundError:
        pass

B = np.array(B)
D = np.array(D)

np.save('ref'+ref+'all_betas.npy', B)
np.save('ref'+ref+'all_dofs.npy', D)

del b, d, beta_suffix, dofs_suffix, ref, np, p, sys
