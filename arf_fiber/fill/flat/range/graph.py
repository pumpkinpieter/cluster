#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
import os
import matplotlib.pyplot as plt

plt.close()

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
main = os.path.expanduser('~/local/convergence/arf_fiber/fill/flat/range/\
outputs')
path = os.path.relpath(main)

raw = np.load(path + '/all_fills.npy').imag
fills = np.linspace(0.05, .6, 80)

base = np.zeros_like(fills)

for j in range(len(fills)):
    b = raw[j, :]
    c = np.where((b != 0) * (np.abs(b) < 1.2) * (b > 0), 1, 0)
    base[j] = np.mean(b, where=list(c))

CL = 20 * base / np.log(10)

plt.plot(fills, CL, 'o-', linewidth=2.5, markersize=8)

plt.title("Flat Fill Sensitivity\n")
plt.xticks(np.linspace(0.03, .6, 20))

plt.xlabel("\nFill depth (delta)")
plt.ylabel("CL")
plt.yscale('log')
plt.grid()
plt.show()
