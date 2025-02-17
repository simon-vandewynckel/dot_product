This file documents a python module built from C++ code with pybind11.
You should document the Python interfaces, *NOT* the C++ interfaces.

Module dot_product.cpp_dot_product
**************************

Module :py:mod:`cpp_dot_product` built from C++ code in dot_product.cpp_dot_product
cpp`.

.. function:: add(x,y,z)
   :module: dot_product.cpp_dot_product
   
   Compute the sum of *x* and *y* and store the result in *z* (overwrite).

   :param x: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param y: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param z: 1D Numpy array with ``dtype=numpy.float64`` (output)
   