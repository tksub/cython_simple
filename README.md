# cython_simple

This is an instruction for setup and running a simple code of cython. 

```
├── README.md
├── function_calc_distance.py
├── function_calc_distance_cython.pyx
├── main.py
└── setup.py
```

The main code `main.py` randomly generates three-dimensional points and gets distances between them through python and python+cython. The python and cython codes for calculating two-particle distances under periodic boundary condition are as follows;

- Python code: `function_calc_distance.py`
- Cython code: `function_calc_distance_cpython.pyx` 

## Test the code

Before testing this code, please check that `numpy` and `cython` libraries are already installed. 

1. Compile the cython code through  

    ```
    python3 setup.py build_ext --inplace
    ```
    By referring the [website](https://stackoverflow.com/questions/2379898/make-distutils-look-for-numpy-header-files-in-the-correct-place/2379912#2379912), `setup.py` is edited. 

2. `python3 main.py`

## Tips for coding a cython script

- Mathematical division is usually slow and reduces the computational performance. If you need a division in multiple lines, you should reduce the mathematical steps of use of division as much as possible. 
- If you call built-in-functions of python library like numpy in cython, the performance decreases significantly. Instead of using libraries, you should use built-in-functions in C via `from libc.math cimport ***`. 
- In the cython code, you should define local variables by `cdef`, which largely increases the computational performance. 