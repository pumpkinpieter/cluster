#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct import ARF

main = os.path.expanduser('~/local/convergence/arf_fiber')
studyname = 'embedding_sensitivity'

path = main + '/' + studyname + '/outputs'

if not os.path.isdir(os.path.relpath(path)):
    print('Making directory: ' + path)
    os.makedirs(os.path.relpath(path))

# Center, radius and span
center = 5.066       # center of circle to search for Z-resonance values
radius = .05      # search radius
nspan = 5
npts = 4

# Embedding parameter array

E = np.linspace(0.001, 1, 40)

# PML strength
alpha = 5

# Set result arrays
betas = np.zeros(nspan, dtype=complex)

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),

    a = ARF(name='poletti', outermaterials='air', freecapil=False,
            refine=ref, e=E[i])

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', e: ' + str(E[i]) + '#'*8 + '\n',
          flush=True)

    a.curve(max(p+1, 3))  # set curvature based on p

    beta, _, _, _, Robj = a.leakyvecmodes(ctr=center,
                                          rad=radius,
                                          alpha=alpha,
                                          nspan=nspan,
                                          npts=npts,
                                          p=p,
                                          niterations=30,
                                          nrestarts=0,
                                          stop_tol=1e-10,
                                          inverse='umfpack')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)
    np.save(os.path.relpath(path + '/e' + str(i)), betas)

    del a, Robj, beta, i, center, radius, nspan, npts
    del main, studyname, path, np, betas, os, sys, ARF
