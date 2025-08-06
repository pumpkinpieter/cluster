#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys

directory = sys.argv[1]

B = []

for i in range(21):
    try:
        b = np.load(directory+'T'+str(i)+'.npy')
        B.append(b)
    except FileNotFoundError:
        print(str(i)+' ')
        pass

B = np.array(B)

np.save(directory+'all_Ts.npy', B)
