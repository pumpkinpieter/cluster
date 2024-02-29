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
path = os.path.relpath(main + 'ref0p9T1.5e-05/outputs/')

exact = (np.load(main + 'exact_scaled_betas.npy')/15e-6)[0]

fig, ax = plt.subplots(1, figsize=(25, 15))
raw = np.load(path + '/all_alphas.npy')

means = np.zeros(len(raw), dtype=complex)
alphas = np.linspace(.1, 15, 101)

for i in range(len(raw)):

    means[i] = np.mean(raw[i][np.where(raw[i, :] != 0)])

errors = 100*np.abs(means-exact)/np.abs(exact)
ax.plot(alphas, errors, linewidth=2)

plt.xlabel('\nalpha', fontsize=25)
plt.ylabel('Relative Error (%) \n', fontsize=25)

plt.title('Bragg $N_1$ Fiber Fundamental Mode \n\
PML parameter dependence at order 9\n', fontsize=30)

plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)

plt.yscale('log')

plt.grid(which='major', axis='y')
plt.grid(which='major', axis='x')
plt.grid(which='minor', axis='x', linestyle='--', linewidth=.5)
plt.grid(which='minor', axis='y', linestyle='--', linewidth=.5)

plt.show()

# %%

np.save(main+'data/ref0p9T1.5e-05_alphas.npy', errors)
