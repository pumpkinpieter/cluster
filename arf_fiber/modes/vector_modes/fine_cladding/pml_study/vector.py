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


# Set result arrays
betas = np.zeros(nspan, dtype=complex)
dofs = np.zeros(1, dtype=float)

alphas = np.linspace(1, 10, 37)

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    a = ARF2(name='fine_cladding', refine=ref, curve=max(p+1, 8),
             poly_core=True)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

    beta, _, _, _, _ = a.leakyvecmodes(p=p, ctr=center, rad=radius,
                                       alpha=alphas[i],
                                       nspan=nspan, npts=npts,
                                       niterations=10, nrestarts=0,
                                       stop_tol=1e-10, inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)
    np.save(outputs + '/ref%i_p%i_alpha%.2f' % (ref, p, alphas[i]) + '_betas',
            betas)
