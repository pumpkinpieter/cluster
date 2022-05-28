#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import os
import numpy as np
import matplotlib.pyplot as plt

plt.close()

plt.rc('axes', titlesize=30)    # fontsize of the axes title
plt.rc('figure', titlesize=30)  # fontsize of the figure title


path = os.path.relpath(
    os.path.expanduser('~/local/convergence/\
arf_fiber/vector_modes/outputs'))

plt.figure(figsize=(22, 16))

for r in range(3):

    betas = np.load(path + '/ref'+str(r)+'all_betas.npy')
    dofs = np.load(path + '/ref'+str(r)+'all_dofs.npy')

    # Filter out bad values

    B = np.where(betas != 0, betas, 1e99)
    BB = np.min(B, axis=1)
    BBB = np.where(BB != 1e99, BB, 0)

    CL = 20 * BBB / np.log(10)

    plt.plot(dofs, CL, 'o-', label='ref='+str(r), linewidth=2.5, markersize=8)

plt.legend()

plt.title('Convergence for ARF fiber\n Vectorial Solver (no Static Condensatio\
n)\n')
plt.xlabel('ndof')
plt.ylabel('CL')
plt.yscale('log')
plt.xscale('log')
plt.grid()
plt.show()
