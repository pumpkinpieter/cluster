#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import PBG
from fiberamp.fiber.microstruct.pbg.fiber_dicts.lyr6cr2 import params

main = '/~/local/convergence/pbg_fiber'
studyname = 'vector_modes'

path = main + '/' + studyname + '/outputs'

if not os.path.isdir(os.path.relpath(path)):
    print('Making directory: ' + path)
    os.makedirs(os.path.relpath(path))

# Center, radius and span

center = 3.034
radius = .1
nspan = 4
npts = 4

# PML strength
alpha = 5

# Set result arrays
betas = np.zeros(nspan, dtype=complex)
dofs = np.zeros(1, dtype=float)

if __name__ == '__main__':

    ref, p = int(sys.argv[1]), int(sys.argv[2])

    a = PBG(params, refine=ref, curve=max(p+1, 3))

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

    a.curve(max(p+1, 3))  # set curvature based on p

    beta, _, _, _, Robj = a.leakyvecmodes(rad=radius, ctr=center, alpha=alpha,
                                          p=p, niterations=30,
                                          npts=npts, stop_tol=1e-11,
                                          nspan=nspan, nrestarts=0,
                                          inverse='pardiso')

    betas[: len(beta)] = beta[:]
    dofs[:] = Robj.XY.ndof

    print('method done, saving.\n', flush=True)
    np.save(os.path.relpath(path + '/ref' + str(ref) + 'p' + str(p)
                            + 'betas'), betas)
    np.save(os.path.relpath(path + '/ref' + str(ref) + 'p' + str(p)
                            + 'dofs'), dofs)

    del a, Robj, beta, ref, p, center, radius, nspan, npts
    del main, studyname, path, np, os, sys, PBG
