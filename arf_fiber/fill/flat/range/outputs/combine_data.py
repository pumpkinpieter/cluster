#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

beta_suffix = '_betas.npy'

B = []

for p in range(400):
    try:
        b = np.load('fill_'+str(p)+beta_suffix)
        B.append(b)
    except FileNotFoundError:
        pass

B = np.array(B)

np.save('all_fills.npy', B)
