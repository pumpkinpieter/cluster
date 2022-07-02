#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
import os
import matplotlib.pyplot as plt

plt.close('all')

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

main = os.path.expanduser('~/local/convergence/arf_fiber/basic/embedding/\
fixed_tubes/subintervals/range_0.26_0.28/outputs')
path = os.path.relpath(main)

plt.figure(figsize=(30, 16))

raw = np.load(path + '/all_e_subs.npy').imag
es = np.load(path + '/E_sub_104_111.npy')

base = np.zeros_like(es)

for j in range(len(es)):
    b = raw[j, :]
    c = np.where((b > 0) * (np.abs(b) < 1000) * (b > 0), 1, 0)
    base[j] = np.mean(b, where=list(c))

CL = 20 * base / np.log(10)

plt.plot(es, base, 'o-', linewidth=2.5, markersize=6)

plt.title("Embedding Sensitivity Vector Method, Subinterval.\n")
plt.xticks(np.linspace(min(es), max(es), 16))

plt.xlabel("\nFraction of Capillary Tube Embedded")
plt.ylabel("CL")
plt.yscale('log')
plt.grid()
plt.show()
