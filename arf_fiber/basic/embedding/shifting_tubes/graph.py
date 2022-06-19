#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close()

plt.rc('axes', labelsize=20)    # fontsize of the axes title
plt.rc('figure', titlesize=40)  # fontsize of the figure title

plt.figure(figsize=(22, 16))

raw = np.load('outputs/all_e.npy').imag
es = np.linspace(0.002, .9999, 240)

base = np.zeros_like(es)

for j in range(len(es)):
    b = raw[j, :]
    c = np.where((b != 0) * (np.abs(b) < 2) * (b > 0), 1, 0)
    base[j] = np.mean(b, where=list(c))

CL = 20 * base / np.log(10)

plt.plot(1-es, CL, 'o-', linewidth=2.5, markersize=8)

plt.title("Embedding Sensitivity Vector Method, Constant Cladding Radius.\n\
 Capillary Tubes Shift into Cladding.\n")

plt.xlabel("\nFraction of Capillary Tube Embedded")
plt.ylabel("CL")
plt.yscale('log')
# plt.xscale('log')
plt.grid()
plt.show()
