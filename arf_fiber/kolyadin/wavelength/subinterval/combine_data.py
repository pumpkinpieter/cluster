#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys

directory = sys.argv[1]

B = []

for p in range(800):
    try:
        b = np.load(directory+'/e'+str(p)+'.npy')
        B.append(b)
    except FileNotFoundError:
        print('file e%i.npy not found. Breaking loop.' % p)
        break

B = np.array(B)

np.save(directory+'/all_e.npy', B)
