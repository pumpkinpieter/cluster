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

plt.rc('font', size=MEDIUM_SIZE)         # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)   # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

main = os.path.expanduser('~/local/convergence/bending/radial_fiber/\
scalar_modes/outputs')
path = os.path.relpath(main)

plt.figure(figsize=(18, 16))

for r in range(4):

    nus = np.load(path + '/ref'+str(r)+'all_nus.npy')
    dofs = np.load(path + '/ref'+str(r)+'all_dofs.npy')

    CL = 20 * (nus[1:, 0]).imag / np.log(10)

    plt.plot(dofs[1:], CL, 'o-', label='ref='+str(r), linewidth=2.5,
             markersize=8)

plt.legend()

plt.xlabel('log of ndofs')
plt.ylabel('CL')
plt.title('Bending Convergence for Nufern Fiber\n Bend \
Radius = 1333*r_core\nCL = 0.0095717362')
# plt.yscale('log')
plt.xscale('log')
plt.grid()
