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

# Set outer materials
scaling = 15
n_glass = 1.4388164768221814
n_air = 1.00027717

n_soft_polymer = 1.44
n_hard_polymer = 1.56

T_soft_polymer = 30 / scaling
T_hard_polymer = 30 / scaling

T_outer = 30 / scaling
T_buffer = 10 / scaling

n0 = n_glass  # Sets buffer and outer region refractive index.

outer_materials = [

    # {'material': 'soft_polymer',
    #  'n': n_soft_polymer,
    #  'T': T_soft_polymer,
    #  'maxh': 2},

    # {'material': 'hard_polymer',
    #  'n': n_hard_polymer,
    #  'T': T_hard_polymer,
    #  'maxh': 2},

    {'material': 'buffer',
     'n': n0,
     'T': T_buffer,
     'maxh': 2},

    {'material': 'Outer',
     'n': n0,
     'T': T_outer,
     'maxh': 4}
]

# Center, radius and span
center = 5.066
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

    a = ARF2(refine=ref, curve=max(p+1, 3), poly_core=True,
             outer_materials=outer_materials)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

    beta, _, _, _, Robj = a.leakyvecmodes(p=p, ctr=center, rad=radius,
                                          alpha=alpha,
                                          nspan=nspan, npts=npts,
                                          niterations=30, nrestarts=0,
                                          stop_tol=1e-11, inverse='pardiso')

    betas[: len(beta)] = beta[:]
    dofs[:] = Robj.XY.ndof

    print('method done, saving.\n', flush=True)
    np.save(outputs + '/ref' + str(ref) + 'p' + str(p) + 'betas', betas)
    np.save(outputs + '/ref' + str(ref) + 'p' + str(p) + 'dofs', dofs)
