#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import os
import numpy as np
import matplotlib.pyplot as plt

SMALL_SIZE = 14
MEDIUM_SIZE = 18
BIGGER_SIZE = 22

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


path = os.path.relpath(
    '/~/local/convergence/\
pbg_fiber/vector_modes/outputs')

plt.figure(figsize=(18, 16))

for r in range(3):

    betas = np.load(path + '/ref'+str(r)+'all_betas.npy')
    dofs = np.load(path + '/ref'+str(r)+'all_dofs.npy')

    # Filter out bad values

    B = np.where(betas != 0, betas, 1e99)
    BB = np.min(B, axis=1)
    BBB = np.where(BB != 1e99, BB, 0)

    CL = 20 * BBB / np.log(10)

    plt.plot(dofs[1:], CL[1:], 'o-', label='ref='+str(r),
             linewidth=2.5, markersize=8)

plt.legend()

plt.xlabel('log of ndofs')
plt.ylabel('log of error')
plt.yscale('log')
plt.xscale('log')
plt.title('PBG Fiber Vectorial Modesolver Loss Plot\n Final loss\
 CL = 0.000137572')
plt.grid()
