#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues, June 7, 11:40:15 2022

@author: pv
"""
import ngsolve as ng
import numpy as np
from fiberamp.fiber import ModeSolver
import netgen.geom2d as geom2d


class SquareFiber(ModeSolver):

    def __init__(self, scale=1e-6, ts=[1e-6, 1e-6, 1e-6],
                 ns=[1.04, 1.4, 1.04], maxhs=[1, 1, 1],
                 bcs=None, mats=None,  wl=1.8e-6,
                 ref=0, curve=3):

        self.scale = scale
        self.rhos = np.array([sum(ts[:i]) for i in range(1, len(ts)+1)])
        self.Rs = self.rhos / self.scale

        self.R = self.Rs[-2]
        self.Rout = self.Rs[-1]

        if bcs is not None:
            self.bcs = bcs
        else:
            self.bcs = ['r'+str(i+1) for i in range(len(self.Rs))]
            self.bcs[-1] = 'OuterCircle'
        if mats is not None:
            self.mats = mats
        else:
            self.mats = ['m'+str(i+1) for i in range(len(self.Rs))]
            self.mats[-1] = 'Outer'
        self.wavelength = wl
        self.ns = ns
        self.maxhs = maxhs
        self.L = scale
        self.create_geometry()
        self.create_mesh(ref=ref, curve=curve)
        self.set_material_properties()

    def create_geometry(self):
        """Construct and return Non-Dimensionalized geometry."""
        self.geo = geom2d.SplineGeometry()
        Rs = self.Rs
        for i, R in enumerate(Rs[:-1]):
            self.geo.AddRectangle((-R, -R), (R, R), leftdomain=i+1,
                                  rightdomain=i+2, bc=self.bcs[i])

        self.geo.AddRectangle((-Rs[-1], -Rs[-1]), (Rs[-1], Rs[-1]),
                              leftdomain=len(Rs),
                              bc=self.bcs[-1])

        for i, (mat, maxh) in enumerate(zip(self.mats, self.maxhs)):
            self.geo.SetMaterial(i+1, mat)
            self.geo.SetDomainMaxH(i+1, maxh)

    def create_mesh(self, ref=0, curve=8):
        """
        Create mesh from geometry.
        """
        self.mesh = ng.Mesh(self.geo.GenerateMesh())

        self.refinements = 0
        for i in range(ref):
            self.mesh.ngmesh.Refine()

        self.refinements += ref
        self.mesh.ngmesh.SetGeometry(self.geo)
        self.mesh = ng.Mesh(self.mesh.ngmesh.Copy())
        self.mesh.Curve(curve)

    def set_material_properties(self):
        """
        Set k0, refractive indices, and V function.
        """

        self.k = 2 * np.pi / self.wavelength
        self.refractive_indices = [self.ns[i](self.wavelength)
                                   if callable(self.ns[i])
                                   else self.ns[i]
                                   for i in range(len(self.ns))]
        self.index = ng.CF(self.refractive_indices)
        self.n0 = self.refractive_indices[-1]

        n0sq = ng.CF([self.n0**2 for i in range(len(self.ns))])
        self.V = (self.L * self.k)**2 * (n0sq - self.index ** 2)

        super().__init__(self.mesh, self.L, self.n0)
