#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from fiberamp.fiber.microstruct import ARF

main = '/~/local/convergence/arf_fiber'
studyname = 'vector_modes'

path = main + '/' + studyname + '/outputs'

if not os.path.isdir(os.path.relpath(path)):
    print('Making directory: ' + path)
    os.makedirs(os.path.relpath(path))

# Center, radius and span
center = 5       # center of circle to search for Z-resonance values
radius = .2            # search radius
nspan = 6

# PML strength
alpha = 3

# Polynomial Degrees and Refinements to cycle through. #################
refs = [0]
ps = [1]

if __name__ == '__main__':

    for i, ref in enumerate(refs):

        a = ARF(name='poletti', outermaterials='air', freecapil=False,
                refine=ref)
        for j, p in enumerate(ps):

            print('\n' + '#'*8 + ' refinement: ' + str(ref) +
                  ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

            a.curve(max(p+1, 3))  # set curvature based on p

            beta, Zs, E, phi, Robj = a.leakyvecmodes(ctr=center,
                                                     rad=radius,
                                                     alpha=alpha,
                                                     nspan=nspan,
                                                     npts=6,
                                                     p=p,
                                                     niterations=20,
                                                     nrestarts=0,
                                                     stop_tol=1e-12,
                                                     inverse='pardiso')

            print('method done, saving.\n', flush=True)

            a.savemodes('arf_E_p'+str(p) + '_ref' + str(ref),
                        E, p, beta, Zs, None)
            a.savemodes('arf_phi_p'+str(p) + '_ref' + str(ref),
                        phi, p, beta, Zs, None)

            del Robj, beta, E, phi, Zs
