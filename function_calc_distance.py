import numpy as np

def calc_distance(natoms, r, lbox):
    
    for ind in range(0, natoms - 1):
        xi = r[0, ind]
        yi = r[1, ind]
        zi = r[2, ind]

        for jnd in range(ind, natoms):
            dx = xi - r[0, jnd]
            dy = yi - r[1, jnd]
            dz = zi - r[2, jnd]

            dx = dx - lbox[0] * np.ceil(dx / lbox[0])
            dy = dy - lbox[1] * np.ceil(dy / lbox[1])
            dz = dz - lbox[2] * np.ceil(dz / lbox[2])

            distance = np.sqrt(dx * dx + dy * dy + dz * dz)
            #print(ind, jnd, distance)

    return distance 