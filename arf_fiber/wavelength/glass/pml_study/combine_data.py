#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys
import os

ref, p, alpha = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])

T = 10
if len(sys.argv) > 4:
    T = float(sys.argv[4])

dirname = 'ref%i_p%i/alpha%.2f_T%.2f/' % (ref, p, alpha, T)

if not os.path.isdir(dirname):
    raise FileNotFoundError('No directory called %s' % dirname)

B = []

N = len(os.listdir(dirname))

if N == 0:
    raise ValueError('Directory %s is empty.' % dirname)

for i in range(N):
    try:
        b = np.load(dirname+str(i)+'.npy')
        B.append(b)
    except FileNotFoundError:
        pass

B = np.array(B)
np.save(dirname + 'all.npy', B)
