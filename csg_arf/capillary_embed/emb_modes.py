#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

main = os.path.expanduser('~/local/convergence/csg_arf')
studyname = 'capillary_embed'

path = main + '/' + studyname + '/outputs'
modes = main + '/' + studyname + '/modes'

if not os.path.isdir(os.path.relpath(path)):
    print('Making directory: ' + path)
    os.makedirs(os.path.relpath(path))

if not os.path.isdir(os.path.relpath(modes)):
    print('Making directory: ' + modes)
    os.makedirs(os.path.relpath(modes))

# Center, radius and span
radius = .007         # search radius
nspan = 4
npts = 4

# Embedding parameter array

E = np.linspace(0.002, .9999, 240)

# Linear fit for finding search centers
m, b = -0.2758566730320395, 5.07341374920433

# Seach centers
center = b + m * E

# PML strength
alpha = 5

# Set result arrays
betas = np.zeros(nspan, dtype=complex)

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    if len(sys.argv) > 4:
        L, R = float(sys.argv[4]), float(sys.argv[5])
        save_index = np.where((L < E) * (E < R))[0]

    a = ARF2(poly_core=True, refine=ref, curve=max(p+1, 3),
             shift_capillaries=True, e=E[i])

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', e: ' + str(E[i]) + '#'*8 + '\n',
          flush=True)

    beta, _, Es, _, _ = a.leakyvecmodes(ctr=center[i],
                                        rad=radius,
                                        alpha=alpha,
                                        nspan=nspan,
                                        npts=npts,
                                        p=p,
                                        niterations=9,
                                        nrestarts=0,
                                        stop_tol=1e-9,
                                        inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)
    np.save(os.path.relpath(path + '/e' + str(i)), betas)
    if len(sys.argv) > 4 and i in save_index:
        a.save_mesh(os.path.relpath(modes + '/mesh_e' + str(i)))
        a.save_modes(Es, os.path.relpath(modes + '/mode_e' + str(i)))
