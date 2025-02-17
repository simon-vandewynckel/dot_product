#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for C++ module dot_product.cpp_dot_product.
"""

import sys

sys.path.insert(0, ".")

import time
import numpy as np

import dot_product.cpp_dot_product as dp


def test_cpp_dot_product():
    print("| size | runtime |")
    print("| --- | --- |")
    for size in range(24):
        v1 = np.arange(1 << size)
        v2 = np.arange(0, 1 << (size + 1), 2)
        start = time.process_time()
        _ = dp.dot_product(v1, v2)
        end = time.process_time()
        print("|", 1 << size, "|", end - start, "s", "|")


# ===============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
# ===============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_cpp_dot_product

    print(f"__main__ running {the_test_you_want_to_debug} ...")
    the_test_you_want_to_debug()
    print("-*# finished #*-")
# ===============================================================================
