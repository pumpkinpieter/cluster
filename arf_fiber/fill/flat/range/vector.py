#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

outputs = 'outputs'

if not os.path.isdir(outputs):
    print('Making directory: ' + outputs)
    os.makedirs(outputs)

# Center, radius and span
center = 5.066       # center of circle to search for Z-resonance values
radius = .1      # search radius
nspan = 4
npts = 4

# PML strength
alpha = 5

# Set result arrays
betas = np.zeros(nspan, dtype=complex)
dofs = np.zeros(1, dtype=float)

fill_range = np.linspace(.05, .6, 201)

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    fill = {'delta': fill_range[i], 'sigma': 0}

    a = ARF2(refine=ref, curve=max(p+1, 3), fill=fill, poly_core=True)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

    beta, _, _, _, Robj = a.leakyvecmodes(p=p, ctr=center, rad=radius,
                                          alpha=alpha,
                                          nspan=nspan, npts=npts,
                                          niterations=9, nrestarts=0,
                                          stop_tol=1e-9, inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)
    np.save(outputs + '/fill_' + str(i) + '_betas', betas)
