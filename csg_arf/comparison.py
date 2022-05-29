#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import os
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

plt.rc('axes', labelsize=20)    # fontsize of the axes title
plt.rc('figure', titlesize=40)  # fontsize of the figure title

path1 = os.path.relpath(os.path.expanduser('~/local/convergence/csg_arf/\
capillary_embed/outputs'))

path2 = os.path.relpath(os.path.expanduser('~/local/convergence/csg_arf/\
embedding_sensitivity/outputs'))


raw1 = np.load(path1 + '/all_e.npy').imag
raw2 = np.load(path2 + '/all_e.npy').imag

es = np.linspace(0.002, .9999, 240)

base1 = np.zeros_like(es)
base2 = np.zeros_like(es)

for j in range(len(es)):
    b = raw1[j, :]
    c = np.where((b != 0) * (np.abs(b) < 2) * (b > 0), 1, 0)
    base1[j] = np.mean(b, where=list(c))
    b = raw2[j, :]
    c = np.where((b != 0) * (np.abs(b) < 1.5) * (b > 0), 1, 0)
    base2[j] = np.mean(b, where=list(c))

CL1 = 20 * base1 / np.log(10)
CL2 = 20 * base2 / np.log(10)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False, figsize=(30, 30))

ax1.plot(es, CL1, 'o-', color='blue',
         label='shifting_capillaries',
         linewidth=2.5, markersize=3)

ax2.plot(es, CL2, 'o-', color='green',
         label='fixed_capillaries',
         linewidth=2.5, markersize=3)

fig.suptitle("Comparison of Embedding Sensitivity.")

ax1.set_xticks(np.linspace(0, 1, 21))
ax2.set_xticks(np.linspace(0, 1, 21))

ax1.set_title('Shifting Capillaries, Fixed Cladding Position:\n')
ax2.set_title('Fixed Capillaries, Shifting Cladding Position:\n')

ax1.set_ylabel("CL"), ax2.set_ylabel("CL")
ax1.set_yscale('log'), ax2.set_yscale('log')

ax1.grid(), ax2.grid()

ax2.set_xlabel("\nFraction of Capillary Tube Embedded")

plt.show()
