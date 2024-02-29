#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys

directory = sys.argv[1]
n_alpha = int(sys.argv[2])

B = []

for i in range(n_alpha):
    try:
        b = np.load(directory+'alpha'+str(i)+'.npy')
        B.append(b)
    except FileNotFoundError:
        print(str(i)+' ')
        pass

B = np.array(B)

np.save(directory+'all_alphas.npy', B)
