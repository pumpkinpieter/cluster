#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 23:37:08 2022

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

main = os.path.relpath('~/local/convergence/arf_fiber/basic/embedding/\
fixed_tubes')
main = os.path.expanduser(main)

sub = main + '/subintervals/index_192_215'

plt.figure(figsize=(30, 16))

raw_sub = np.load(sub + '/outputs/all_e_subs.npy').imag
es_sub = np.load(sub + '/outputs/E_sub_192_215.npy')

base = np.zeros_like(es_sub)

for j in range(len(es_sub)):
    b = raw_sub[j, :]
    c = np.where((b > 0) * (np.abs(b) < 10) * (b > 0), 1, 0)
    base[j] = np.mean(b, where=list(c))

CL = 20 * base / np.log(10)

plt.plot(es_sub, CL, 'o-', linewidth=2.5, markersize=8)

raw = np.load(main + '/outputs/all_e.npy').imag
es = np.linspace(0.002, .9999, 250)

base = np.zeros_like(es)

for j in range(len(es)):
    b = raw[j, :]
    c = np.where((b > 0) * (np.abs(b) < 10) * (b > 0), 1, 0)
    base[j] = np.mean(b, where=list(c))

CL = 20 * base / np.log(10)

plt.plot(es[:192], CL[:192], 'o-', linewidth=2.5, markersize=8)


plt.title("Embedding Sensitivity Vector Method, Subinterval.\n")
# plt.xticks(np.linspace(min(es_sub), max(es_sub), 16))

plt.xlabel("\nFraction of Capillary Tube Embedded")
plt.ylabel("CL")
plt.yscale('log')
plt.grid()
plt.show()
