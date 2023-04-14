#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys

ref = sys.argv[1]

beta_suffix = 'betas.npy'
dofs_suffix = 'dofs.npy'
zs_suffix = 'Zs.npy'

B = []
D = []
Z = []

for p in range(35):
    try:
        b = np.load('ref'+ref+'p'+str(p)+beta_suffix)
        z = np.load('ref'+ref+'p'+str(p)+zs_suffix)
        d = np.load('ref'+ref+'p'+str(p)+dofs_suffix)
        B.append(b)
        D.append(d[0])
        Z.append(z)
    except FileNotFoundError:
        pass

B = np.array(B)
D = np.array(D)
Z = np.array(Z)

np.save('ref'+ref+'all_betas.npy', B)
np.save('ref'+ref+'all_Zs.npy', Z)
np.save('ref'+ref+'all_dofs.npy', D)
