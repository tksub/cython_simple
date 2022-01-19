import numpy as np
cimport numpy as np
import cython 
cimport cython 

from libc.math cimport sqrt, ceil

def calc_distance_cpython(int natoms,
                          np.ndarray[double, ndim=2] r, 
                          np.ndarray[double, ndim=1] lbox):
                          
    cdef int ind, jnd 
    cdef double xi, yi, zi, dx, dy, dz, distance
    cdef double hlx = 0.5 * lbox[0]
    cdef double hly = 0.5 * lbox[1]
    cdef double hlz = 0.5 * lbox[2]

    for ind in range(0, natoms - 1):
        xi = r[0, ind]
        yi = r[1, ind]
        zi = r[2, ind]
        
        for jnd in range(ind, natoms): 
            dx = xi - r[0, jnd]
            dy = yi - r[1, jnd]
            dz = zi - r[2, jnd]

            #dx = dx - lbox[0] * ceil(dx / lbox[0])
            #dy = dy - lbox[1] * ceil(dy / lbox[1])
            #dz = dz - lbox[2] * ceil(dz / lbox[2])

            if dx >= hlx:
                dx = dx - hlx
            elif dx <= -hlx:
                dx = dx + hlx
            
            if dy >= hly:
                dy = dy - hly
            elif dy <= -hly:
                dy = dy + hly

            if dz >= hlz:
                dz = dz - hlz
            elif dz <= -hlz:
                dz = dz + hlz

            distance = sqrt(dx * dx + dy * dy + dz * dz)

    return distance