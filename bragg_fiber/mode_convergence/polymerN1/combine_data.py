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
        if p == 0:
            raise ValueError('No matching files found.')
        break

D = np.array(D)
print('Last file prefix found: '+directory+'/ref'+ref +
      'p'+str(p)+'.\n')
print('Writing combined data files:')
print(directory+'/ref'+ref+'all_betas.npy, ')
print(directory+'/ref'+ref+'all_dofs.npy')

np.save(directory+'/ref'+ref+'all_betas.npy', B)
np.save(directory+'/ref'+ref+'all_dofs.npy', D)
