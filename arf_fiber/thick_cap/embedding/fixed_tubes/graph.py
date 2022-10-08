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

plt.figure(figsize=(30, 15))

main = os.path.expanduser('~/local/convergence/arf_fiber/basic/embedding/\
fixed_tubes/outputs')
path = os.path.relpath(main)

raw = np.load(path + '/all_e.npy').imag
es = np.linspace(0.002, .9999, 400)

base = np.zeros_like(es)

for j in range(len(es)):
    if es[j] < .24:
        b = raw[j, :]
        c = np.where((b > 0.01) * (np.abs(b) < .25) * (b > 0), 1, 0)
        base[j] = np.mean(b, where=list(c))

    elif (es[j] >= .24) * (es[j] < .44):
        b = raw[j, :]
        c = np.where((b > 0.01) * (np.abs(b) < 3.1) * (b > 0), 1, 0)
        base[j] = np.mean(b, where=list(c))

    elif (es[j] >= .5) * (es[j] < .52):
        b = raw[j, :]
        c = np.where((b > 0.01) * (np.abs(b) < 10) * (b > 0), 1, 0)
        base[j] = np.mean(b, where=list(c))

    elif (es[j] >= .52) * (es[j] < .54):
        b = raw[j, :]
        c = np.where((b > 0.01) * (np.abs(b) < .4) * (b > 0), 1, 0)
        base[j] = np.mean(b, where=list(c))

    elif (es[j] >= .62) * (es[j] < .68):
        b = raw[j, :]
        c = np.where((b > 0.01) * (np.abs(b) < .13) * (b > 0), 1, 0)
        base[j] = np.mean(b, where=list(c))

    elif (es[j] >= .76) * (es[j] < .78):
        b = raw[j, :]
        c = np.where((b > 0.01) * (np.abs(b) < 16) * (b > 0), 1, 0)
        base[j] = np.mean(b, where=list(c))

    elif (es[j] >= .78) * (es[j] < .8):
        b = raw[j, :]
        c = np.where((b > 0.01) * (np.abs(b) < 7) * (b > 0), 1, 0)
        base[j] = np.mean(b, where=list(c))

    else:
        b = raw[j, :]
        c = np.where((b > 0.01) * (np.abs(b) < 31) * (b > 0), 1, 0)
        base[j] = np.mean(b, where=list(c))

CL = 20 * base / np.log(10)

plt.plot(es, base, 'o-', linewidth=2.5, markersize=5)

plt.title("Embedding Sensitivity 'Basic' ARF Fiber\n")
plt.xticks(np.linspace(0, 1, 26))

plt.subplots_adjust(top=0.88, bottom=0.11, left=0.075, right=0.965,
                    hspace=0.2, wspace=0.2)

plt.xlabel("\nFraction of Capillary Tube Embedded")
plt.ylabel("CL")
plt.yscale('log')
plt.grid()
plt.show()
