#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

SMALL_SIZE = 14
MEDIUM_SIZE = 18
BIGGER_SIZE = 22

plt.rc('font', size=MEDIUM_SIZE)         # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)   # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

outputs = 'outputs'

plt.figure(figsize=(18, 16))

for r in range(1):
    betas = np.load(outputs + '/ref'+str(r)+'all_betas.npy')
    Zs = np.load(outputs + '/ref'+str(r)+'all_Zs.npy')

    dofs = np.load(outputs + '/ref'+str(r)+'all_dofs.npy')

    # Filter out bad values

    B = np.where(betas.imag != 0, betas.imag, 1e99)
    BB = np.min(B, axis=1)

    CL = 20 * BB / np.log(10)
    plt.plot(dofs[1:], CL[1:], 'o-', label='ref='+str(r),
             linewidth=2.5, markersize=8)

plt.legend()

plt.xlabel('ndofs')
plt.ylabel('CL')
plt.title('CSG Arf Poletti Vector Convergence, High Order Mode')
plt.yscale('log')
plt.xscale('log')
plt.grid()
plt.show()
