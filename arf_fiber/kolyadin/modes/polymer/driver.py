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
center = 5.16       # center of circle to search for Z-resonance values
radius = .1      # search radius
nspan = 4
npts = 4

n_poly = 1.5 + .1j
n_buffer = 1.00027717
n0 = n_buffer

scaling = 59.5
T_cladding = 1.2 * 25.5 / scaling

T_poly = .5 * T_cladding
T_buffer = .5 * T_cladding
T_outer = .75 * T_cladding

# PML strength
alpha = 5

# Set result arrays
betas = np.zeros(nspan, dtype=complex)
dofs = np.zeros(1, dtype=float)

if __name__ == '__main__':

    ref, p = int(sys.argv[1]), int(sys.argv[2])

    outer_materials = [

        {'material': 'poly',
         'n': n_poly,
         'T': T_poly,
         'maxh': .03},

        {'material': 'buffer',
         'n': n_buffer,
         'T': T_buffer,
         'maxh': .2},

        {'material': 'Outer',
         'n': n0,
         'T': T_outer,
         'maxh': .2}
    ]

    a = ARF2(name='kolyadin', refine=ref, curve=max(p+1, 8), poly_core=True,
             wl=3.25e-6, outer_materials=outer_materials)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

    beta, _, _, _, Robj = a.leakyvecmodes(p=p, ctr=center, rad=radius,
                                          alpha=alpha,
                                          nspan=nspan, npts=npts,
                                          niterations=10, nrestarts=0,
                                          stop_tol=1e-9, inverse='pardiso')

    betas[: len(beta)] = beta[:]
    dofs[:] = Robj.XY.ndof

    print('method done, saving.\n', flush=True)
    np.save(outputs + '/ref' + str(ref) + 'p' + str(p) + 'betas', betas)
    np.save(outputs + '/ref' + str(ref) + 'p' + str(p) + 'dofs', dofs)
