#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
import os
import matplotlib.pyplot as plt

# plt.close('all')

SMALL_SIZE = 18
MEDIUM_SIZE = 25
BIGGER_SIZE = 40

plt.rc('font', size=MEDIUM_SIZE)         # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)   # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

plt.figure(figsize=(30, 16))

main = os.path.expanduser('~/local/convergence/arf_fiber/embedding/air/\
fixed_tubes/subintervals/index_212_224')
path = os.path.relpath(main + '/outputs')


raw = np.load(path + '/all_e_subs.npy').imag
es = np.load(path + '/E_sub_212_224.npy')

base = np.zeros_like(es)

for j in range(len(es)):
    b = raw[j, :]
    c = np.where((b != 0) * (np.abs(b) < 1.2) * (b > 0), 1, 0)
    base[j] = np.mean(b, where=list(c))

CL = 20 * base / np.log(10)
mask = ~np.isnan(CL)

plt.plot(es[mask], CL[mask], 'o-', linewidth=2.5, markersize=8)

plt.title("Embedding Sensitivity Vector Method, Subinterval.\n")
plt.xticks(np.linspace(min(es), max(es), 16))

plt.xlabel("\nFraction of Capillary Tube Embedded")
plt.ylabel("CL")
plt.yscale('log')
plt.grid()
plt.show()

# # Find updated refinement for interval
# lower = es[35:]
# middle = np.linspace(es[27], es[34], 26)
# higher = es[14:27]
# highest = np.linspace(es[1], es[13], 41)

# new_es = np.concatenate((highest, higher, middle, lower))
# plt.plot(1-new_es, .2 * np.ones_like(new_es), 'bo')
# mode limits .08593 .0887


# Save to .dat file for pgfplots

# paper_path = os.path.relpath(os.path.expanduser('~/papers/arf_embedding/\
# figures'))

# mask = ~np.isnan(CL)

# # both = np.concatenate((es[mask][np.newaxis], CL[mask][np.newaxis]), axis=1)
# both = np.column_stack((es[mask], CL[mask]))
# # both = np.column_stack((x,y))
# np.savetxt(paper_path + '/subinterval.dat', both, fmt='%.8f')
