/*
 *  C++ source file for module dot_product.cpp_dot_product
 */

// See http://people.duke.edu/~ccc14/cspy/18G_C++_Python_pybind11.html for examples on how to use pybind11.
// The example below is modified after http://people.duke.edu/~ccc14/cspy/18G_C++_Python_pybind11.html#More-on-working-with-numpy-arrays
#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h> // add support for multi-dimensional arrays

namespace nb = nanobind;

double dot_product(nb::ndarray<double> a, nb::ndarray<double> b)
{
    assert(a.shape() == b.shape());
    double result = 0;
    for (size_t i = 0; i < a.shape(0); i++)
    {
        result += a.data()[i] * b.data()[i];
    }
    return result;
}

NB_MODULE(cpp_dot_product, m)
{
    m.doc() = "A simple example python extension";

    m.def("dot_product", &dot_product, "");

    m.def("inspect", [](nb::ndarray<> a)
          {
                printf("Array data pointer : %p\n", a.data());
                printf("Array dimension : %zu\n", a.ndim());
                for (size_t i = 0; i < a.ndim(); ++i) {
                    printf("Array dimension [%zu] : %zu\n", i, a.shape(i));
                    printf("Array stride    [%zu] : %zd\n", i, a.stride(i));
                }
                printf("Device ID = %u (cpu=%i, cuda=%i)\n"
                , a.device_id()
                , int(a.device_type() == nb::device::cpu::value)
                , int(a.device_type() == nb::device::cuda::value)
                );
                printf("Array dtype: int16=%i, uint32=%i, float32=%i, float64=%i\n"
                , a.dtype() == nb::dtype<int16_t>()
                , a.dtype() == nb::dtype<uint32_t>()
                , a.dtype() == nb::dtype<float>()
                , a.dtype() == nb::dtype<double>()
                ); }, "inspect an array");
}