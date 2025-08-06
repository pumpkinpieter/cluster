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

main = os.path.expanduser('~/local/convergence/bragg_fiber/pml_studies/\
thickness/')

p = 8
alpha = float(7.5)

outdir = 'p'+str(p)+'_alpha'+str(alpha)
path = os.path.relpath(main + outdir)

exact = (np.load(main + 'exact_scaled_betas.npy')/15e-6)[0]

fig, ax = plt.subplots(1, figsize=(25, 15))
raw = np.load(path + '/all_Ts.npy')

means = np.zeros(len(raw), dtype=complex)
ts = np.linspace(5e-6, 40e-6, 21)

for i in range(len(raw)):

    means[i] = np.min(raw[i][np.where(raw[i, :] != 0)])


errors = np.abs(means-exact)
ax.plot(ts, errors, 'o-', linewidth=2, markersize=5)

plt.xlabel('\nPML Thickness ', fontsize=25)
plt.ylabel('Absolute Error (%) \n', fontsize=25)

plt.title('Bragg $N_1$ Fiber Fundamental Mode \n\
PML parameter dependence\nalpha=%0.2f, p=%i, ref=0' % (alpha, p), fontsize=30)

plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)

plt.yscale('log')

plt.grid(which='major', axis='y')
plt.grid(which='major', axis='x')
plt.grid(which='minor', axis='x', linestyle='--', linewidth=.5)
plt.grid(which='minor', axis='y', linestyle='--', linewidth=.5)

plt.show()

# # %%

# np.save(main+'data/ref0p8T1.5e-05_alphas.npy', errors)
