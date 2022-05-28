#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

main = os.path.expanduser('~/local/convergence/csg_arf')
studyname = 'capillary_embed'

path = main + '/' + studyname + '/outputs'

if not os.path.isdir(os.path.relpath(path)):
    print('Making directory: ' + path)
    os.makedirs(os.path.relpath(path))

# Center, radius and span
center = 5.066       # center of circle to search for Z-resonance values
radius = .01         # search radius
nspan = 4
npts = 4

# Embedding parameter array

E = np.linspace(0.002, .9999, 240)

# PML strength
alpha = 5

# Set result arrays
betas = np.zeros(nspan, dtype=complex)

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),

    a = ARF2(poly_core=True, refine=ref, curve=max(p+1, 3), e=E[i])

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', e: ' + str(E[i]) + '#'*8 + '\n',
          flush=True)

    beta, _, _, _, _ = a.leakyvecmodes(ctr=center,
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
