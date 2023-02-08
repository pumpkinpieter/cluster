#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys

directory, ref = sys.argv[1], sys.argv[2]

beta_suffix = 'betas.npy'
dofs_suffix = 'dofs.npy'

B = []
D = []

for p in range(35):
    try:
        b = np.load(directory+'/ref'+ref+'p'+str(p)+beta_suffix)
        d = np.load(directory+'/ref'+ref+'p'+str(p)+dofs_suffix)
        B.append(b)
        D.append(d[0])
    except FileNotFoundError:
        print('No file %s/ref%ip%i.npy found,\
 breaking out of loop.' % (directory, ref, p))

D = np.array(D)

np.save(directory+'/ref'+ref+'all_betas.npy', B)
np.save(directory+'/ref'+ref+'all_dofs.npy', D)
