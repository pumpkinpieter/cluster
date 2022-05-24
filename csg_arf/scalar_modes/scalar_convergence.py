#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

main = os.path.expanduser('~/local/convergence/csg_arf')
studyname = 'scalar_modes'

path = main + '/' + studyname + '/outputs'

if not os.path.isdir(os.path.relpath(path)):
    print('Making directory: ' + path)
    os.makedirs(os.path.relpath(path))

# Center, radius and span
center = 2.24       # center of circle to search for Z-resonance values
radius = .02      # search radius
nspan = 2
npts = 4

# PML strength
alpha = 5

# Set result arrays
betas = np.zeros(nspan, dtype=complex)
dofs = np.zeros(1, dtype=float)

if __name__ == '__main__':

    ref, p = int(sys.argv[1]), int(sys.argv[2])

    a = AR2(refine=ref, curve=max(p+1,3))

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

    _, _, _, beta, P, _ = a.leakymode(p=p, ctr=center, rad=radius, alpha=alpha,
                                      nspan=nspan, npts=npts,
                                      niterations=20, nrestarts=0,
                                      stop_tol=1e-11, inverse='pardiso')

    betas[: len(beta)] = beta[:]
    dofs[:] = P.fes.ndof

    print('method done, saving.\n', flush=True)
    np.save(os.path.relpath(path + '/ref' + str(ref) + 'p' + str(p)
                            + 'betas'), betas)
    np.save(os.path.relpath(path + '/ref' + str(ref) + 'p' + str(p)
                            + 'dofs'), dofs)

    del a, P, beta, ref, p, center, radius, nspan, npts
    del main, studyname, path, np, os, sys, ARF
