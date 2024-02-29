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

main = os.path.expanduser('~/local/convergence/bragg_fiber/mode_convergence/\
vector/pml_N1/')
path = os.path.relpath(main + 'data/')

fig, ax = plt.subplots(1, figsize=(25, 15))

alphas8 = np.linspace(.1, 15, 201)
alphas9 = np.linspace(.1, 15, 101)

orders = [8, 9]
alpha_arrays = [alphas8, alphas9]

for i in range(len(orders)):
    errors = np.load(path+'/ref0p'+str(orders[i])+'T1.5e-05_alphas.npy')
    alphas = alpha_arrays[i]

    if i == 0:
        ax.plot(alphas, errors, linewidth=2, label='p=8')
    else:
        ax.plot(alphas, errors,  'o-', linewidth=0, markersize=4,
                label='p=9')

plt.xlabel('\nalpha', fontsize=25)
plt.ylabel('Relative Error (%) \n', fontsize=25)

plt.title('Bragg $N_1$ Fiber Fundamental Mode \n\
PML parameter dependence for order 8 and 9.\n', fontsize=30)

plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)

plt.yscale('log')
plt.legend(fontsize=25)
plt.grid(which='major', axis='y')
plt.grid(which='major', axis='x')
plt.grid(which='minor', axis='x', linestyle='--', linewidth=.5)
plt.grid(which='minor', axis='y', linestyle='--', linewidth=.5)

plt.show()
