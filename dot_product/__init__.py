# -*- coding: utf-8 -*-

"""
## Python package dot_product
"""

__version__ = "0.0.0"

import numba


@numba.jit
def dot_product(a: list, b: list):
    assert len(a) == len(b)
    result = 0
    for ai, bi in zip(a, b):
        result += ai * bi
    return result
