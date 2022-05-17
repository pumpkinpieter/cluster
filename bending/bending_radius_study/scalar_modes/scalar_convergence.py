#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp import FiberMode

main = os.path.expanduser('~/local/convergence/bending/pml_study')
studyname = 'scalar_modes'

path = main + '/' + studyname + '/outputs'

if not os.path.isdir(os.path.relpath(path)):
    print('Making directory: ' + path)
    os.makedirs(os.path.relpath(path))

# Bend Radius
R_bend = 4000

# Center, radius and span
center = 11468
radius = 1
nspan = 4
npts = 6

# Set result arrays
nus = np.zeros(nspan, dtype=complex)
alphas = np.zeros(1, dtype=float)

if __name__ == '__main__':

    ref, p, alpha = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])

    a = FiberMode(fibername='Nufern_Yb', R=3, Rout=5, h=80, refine=ref,
                  curveorder=max(p, 3))

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

    Nusqrs, _, P, _ = a.bentscalarmodes(rad=radius, ctr=center, R_bend=R_bend,
                                        alpha=alpha, p=p, nspan=nspan,
                                        npts=npts, niterations=12)

    nus[: len(Nusqrs)] = ((Nusqrs ** .5) * R_bend)[:]
    alphas[:] = alpha

    print('method done, saving.\n', flush=True)
    np.save(os.path.relpath(path + '/ref' + str(ref) + 'p' + str(p)
                            + 'nus'), nus)
    np.save(os.path.relpath(path + '/ref' + str(ref) + 'p' + str(p)
                            + 'alpha'), alphas)
