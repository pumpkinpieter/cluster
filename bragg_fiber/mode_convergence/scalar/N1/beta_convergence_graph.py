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

main = os.path.expanduser('~/local/convergence/bragg_fiber/mode_convergence/')
path = os.path.relpath(main + 'N1/outputs')

exact = (np.load(main + 'N1/exact_scaled_betas.npy')/15e-6)[0]

fig, ax = plt.subplots(1, figsize=(20, 16))

all_means = []
refs = 2

for r in range(refs+1):

    betas = np.load(path + '/ref'+str(r)+'all_betas.npy')
    dofs = np.load(path + '/ref'+str(r)+'all_dofs.npy')
    means = np.zeros(len(betas), dtype=complex)

    for i in range(len(betas)):

        # Filter out bad values

        means[i] = np.mean(betas[i][np.where(betas[i, :] != 0)])

    ax.plot(dofs, np.abs(means-exact.conj()), 'o-',
            label='refinement: '+str(r),
            linewidth=2.5, markersize=9,
            markerfacecolor='white')

    all_means.append(list(means))

xmin, xmax = ax.get_xlim()


plt.legend(fontsize=18)

plt.xlabel('\nndofs', fontsize=25)
plt.ylabel('Absolute Error\n', fontsize=25)

plt.title('Hollow Core Bragg Fiber: $N_1$ Configuration\n\
Fundamental Mode Convergence\n', fontsize=35)

plt.yscale('log')
plt.xscale('log')

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(which='major', axis='y')
plt.grid(which='major', axis='x')
plt.grid(which='minor', axis='x', linestyle='--', linewidth=.5)
plt.grid(which='minor', axis='y', linestyle='--', linewidth=.5)

plt.show()
