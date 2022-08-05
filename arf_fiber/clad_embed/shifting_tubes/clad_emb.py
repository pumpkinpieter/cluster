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


# Set result arrays
nspan = 4
betas = np.zeros(nspan, dtype=complex)

# Embedding parameter array
E = np.linspace(0.002, .9999, 240)
T = np.linspace(10, 11, 11)

# Linear fit for finding search centers
m, b = -0.28106463,  5.0825956

# Seach centers
centers = b + m * E

if __name__ == '__main__':

    ref, p = int(sys.argv[1]), int(sys.argv[2])
    i, t = int(sys.argv[3]), int(sys.argv[4])

    if len(sys.argv) > 5:
        L, R = float(sys.argv[4]), float(sys.argv[5])
        save_index = np.where((L < E) * (E < R))[0]

    a = ARF2(name='fine_cladding', poly_core=True, refine=ref,
             curve=max(p+1, 8), shift_capillaries=True, e=E[i],
             T_cladding=T[t])

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', T: ' + str(T[t]) + '#'*8 + '\n',
          flush=True)

    center = centers[i]
    radius = .01
    npts = 4
    alpha = 5

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
