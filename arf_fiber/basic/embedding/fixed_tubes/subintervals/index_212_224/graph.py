#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
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

raw = np.load('outputs/all_e_subs.npy').imag
es = np.load('outputs/E_sub_212_224.npy')

base = np.zeros_like(es)

for j in range(len(es)):
    b = raw[j, :]
    c = np.where((b != 0) * (np.abs(b) < 1.2) * (b > 0), 1, 0)
    base[j] = np.mean(b, where=list(c))

CL = 20 * base / np.log(10)

plt.plot(1-es, CL, 'o-', linewidth=2.5, markersize=8)

plt.title("Embedding Sensitivity Vector Method, Subinterval.\n")
plt.xticks(np.linspace(min(1-es), max(1-es), 16))

plt.xlabel("\nFraction of Capillary Tube Embedded")
plt.ylabel("CL")
plt.yscale('log')
plt.grid()
plt.show()

# Find updated refinement for interval
lower = es[35:]
middle = np.linspace(es[27], es[34], 26)
higher = es[14:27]
highest = np.linspace(es[1], es[13], 41)

new_es = np.concatenate((highest, higher, middle, lower))
plt.plot(1-new_es, .2 * np.ones_like(new_es), 'bo')
# mode limits .08593 .0887
