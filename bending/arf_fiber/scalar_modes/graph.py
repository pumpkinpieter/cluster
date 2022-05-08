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
    '/~/local/convergence/bending/\
arf_fiber/vector_modes/outputs')

betas = np.load(path + '/betas.npy').imag
dofs = np.load(path + '/dofs.npy')

# Filter out bad values

B = np.where(betas != 0, betas, 1e99)
BB = np.min(B, axis=2)
BBB = np.where(BB != 1e99, BB, 0)

CL = 20 * BBB / np.log(10)

plt.figure(figsize=(18, 16))

for i in range(0, CL.shape[0]-1):
    plt.plot(np.log(dofs[i, :]), CL[i, :],
             'o-', label='ref='+str(i),
             linewidth=2.5, markersize=8)

betas = np.load(path + '/betas2.npy').imag
dofs = np.load(path + '/dofs2.npy')

# Filter out bad values

B = np.where(betas != 0, betas, 1e99)
BB = np.min(B, axis=2)
BBB = np.where(BB != 1e99, BB, 0)

CL = 20 * BBB / np.log(10)


for i in range(0, CL.shape[0]):
    plt.plot(np.log(dofs[i, :]), CL[i, :],
             'o-', label='ref='+str(2),
             linewidth=2.5, markersize=8)

betas = np.load(path + '/betas3.npy').imag
dofs = np.load(path + '/dofs3.npy')

# Filter out bad values

B = np.where(betas != 0, betas, 1e99)
BB = np.min(B, axis=2)
BBB = np.where(BB != 1e99, BB, 0)

CL = 20 * BBB / np.log(10)


for i in range(0, CL.shape[0]):
    plt.plot(np.log(dofs[i, :]), CL[i, :],
             'o-',
             linewidth=2.5, markersize=8)


plt.legend()

plt.xlabel('log of ndofs')
plt.ylabel('log of error')
plt.grid()
