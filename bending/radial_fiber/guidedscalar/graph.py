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

z_exact = 3.7969194313378907-0.725805740812567j

path = os.path.relpath(
    '/home/pv/local/fiberamp/fiber/microstruct/pbg/convergence_code/leakyvec')


Zs = np.load(path + '/leakyvec_Zs.npy')
dofs = np.load(path + '/leakyvec_dofs.npy')

# Take mean of differences where not zero (and not too large)
diffs = np.mean(Zs-z_exact, axis=2,
                where=np.where((Zs != 0)*(np.abs(Zs-z_exact) < 1),
                               True, False))

plt.figure(figsize=(18, 16))

for i in range(1, len(Zs[1])):
    plt.plot(np.log10(dofs[:, i]), np.log10(
        np.abs(diffs[:, i])), 'o-', label='p='+str(i+1), linewidth=2.5,
        markersize=8)

plt.legend()

plt.xlabel('log of ndofs')
plt.ylabel('log of error')
plt.grid()
# plt.ylim(-16)
plt.title('Leaky Mode Convergence for Vectorial Solver\nNufern Ytterbium Fiber \
 (Fundamental Mode)\n')
