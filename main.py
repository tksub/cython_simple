import numpy as np
import time 
from function_calc_distance import calc_distance
from function_calc_distance_cython import calc_distance_cpython 


natoms = 10000
#natoms = 619236
r = np.random.rand(3, natoms)
lbox = np.array([1.0, 1.0, 1.0])

# python only
start_time = time.process_time()
distance = calc_distance(natoms, r, lbox)
print('calculated distance = ', distance)
end_time = time.process_time()
elapsed_time = end_time - start_time
print('elapsed time = ', elapsed_time)

# cython + numpy
start_time = time.process_time()
distance = calc_distance_cpython(natoms, r, lbox)
print('calculated distance = ', distance)
end_time = time.process_time()
elapsed_time = end_time - start_time
print('elapsed time = ', elapsed_time)