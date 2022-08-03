#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

for i in range(11):

    B = []

    for p in range(251):
        try:
            b = np.load('e' + str(p) + '_T' + str(i) + '.npy')
            B.append(b)
        except FileNotFoundError:
            pass

    B = np.array(B)

    np.save('T_' + str(i) + 'all_e.npy', B)
