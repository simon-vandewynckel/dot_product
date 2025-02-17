# -*- coding: utf-8 -*-

"""Tests for dot_product package."""

import sys

sys.path.insert(0, ".")
import time
import dot_product.dot_product as dp
import numpy as np


def test_dot_product_benchmark():
    # make sure dot_product is jitted
    v1 = np.arange(1 << 16)
    v2 = np.arange(0, 1 << (16 + 1), 2)
    _ = dp.dot_product(v1, v2)

    print("| size | runtime |")
    print("| --- | --- |")
    for size in range(24):
        v1 = np.arange(1 << size)
        v2 = np.arange(0, 1 << (size + 1), 2)
        start = time.process_time()
        _ = dp.dot_product(v1, v2)
        end = time.process_time()
        print("|", 1 << size, "|", end - start, "s", "|")


# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (otherwise all tests are normally run with pytest)
# Make sure that you run this code with the project directory as CWD, and
# that the source directory is on the path
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_dot_product_benchmark

    print("__main__ running", the_test_you_want_to_debug)
    the_test_you_want_to_debug()
    print("-*# finished #*-")

# eof
