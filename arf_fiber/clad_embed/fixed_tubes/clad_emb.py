#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

if not os.path.isdir('outputs'):
    print('Making directory: outputs')
    os.makedirs('outputs')

if not os.path.isdir('modes'):
    print('Making directory: modes')
    os.makedirs('modes')

# Set search center, radius and contour points
center = 5.066
radius = .007
npts = 4

# Set result arrays
nspan = 4
betas = np.zeros(nspan, dtype=complex)

# Embedding parameter array
E = np.linspace(0.002, .9999, 240)
T = np.linspace(10, 10.01, 11)

# PML strength
alpha = 5

if __name__ == '__main__':

    ref, p = int(sys.argv[1]), int(sys.argv[2])
    i, t = int(sys.argv[3]), int(sys.argv[4])

    if len(sys.argv) > 5:
        L, R = float(sys.argv[4]), float(sys.argv[5])
        save_index = np.where((L < E) * (E < R))[0]

    a = ARF2(name='fine_cladding', poly_core=True, refine=ref,
             curve=max(p+1, 8), shift_capillaries=False, e=E[i],
             T_cladding=T[t])

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', T: ' + str(T[t]) + '#'*8 + '\n',
          flush=True)

    beta, _, Es, _, _ = a.leakyvecmodes(ctr=center,
                                        rad=radius,
                                        alpha=alpha,
                                        nspan=nspan,
                                        npts=npts,
                                        p=p,
                                        niterations=12,
                                        nrestarts=0,
                                        stop_tol=1e-9,
                                        inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)

    np.save('outputs/e' + str(i) + '_T' + str(t), betas)

    if len(sys.argv) > 5 and i in save_index:
        a.save_mesh('modes/mesh_e' + str(i) + '_T' + str(t))
        a.save_modes(Es, 'modes/mode_e' + str(i) + '_T' + str(t))
