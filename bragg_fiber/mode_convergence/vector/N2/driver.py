#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.bragg import Bragg

if not os.path.isdir('outputs'):
    print('Making directory: outputs')
    os.makedirs('outputs')

# Set result arrays
nspan = 4
betas = np.zeros(nspan, dtype=complex)
dofs = np.zeros(1, dtype=float)

# Get exact search centers
centers = np.load('exact_scaled_betas.npy')

# Embedding parameter array
wls = np.linspace(1.4, 2, 301) * 1e-6

# PML strength
alpha = 5

n_air = 1.00027717
n_glass = 1.4388164768221814
ts = [15*2.7183333333333333e-6, 15*2/3*1e-6,
              15*2.7183333333333333e-6, 15*1e-6, 15*2e-6]
ns = [lambda x: n_air, lambda x: n_glass, lambda x: n_air,
              lambda x: n_glass, lambda x: n_glass]
mats = ['core', 'glass', 'air', 'buffer', 'Outer']
maxhs = [.1, .02, .06, .015, .05]
scale = 15e-6

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    a = Bragg(ts=ts, scale=scale, maxhs=maxhs, ns=ns, wl=wls[i],
              ref=ref, mats=mats)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', wavelength: ' + str(wls[i]) +
          '#'*8 + '\n', flush=True)

    centers = a.sqrZfrom(centers/a.L).conjugate()
    center = centers[i]
    radius = 0.05
    npts = 4

    beta, _, _, _, Ro = a.leakyvecmodes(ctr=center,
                                        rad=radius,
                                        alpha=alpha,
                                        nspan=nspan,
                                        npts=npts,
                                        p=p,
                                        niterations=10,
                                        nrestarts=0,
                                        stop_tol=1e-10,
                                        inverse='pardiso')

    betas[: len(beta)] = beta[:]
    dofs[:] = Ro.XY.ndof

    print('method done, saving.\n', flush=True)
    np.save('outputs/ref' + str(ref) + 'p' + str(p) + 'betas', betas)
    np.save('outputs/ref' + str(ref) + 'p' + str(p) + 'dofs', dofs)
