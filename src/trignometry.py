import math
import cmath

PI = math.pi


def sin(x):
    z = math.sin(PI / x)
    return z


def cos(x):
    n = math.cos(PI / x)
    return n


def tan(x, y, z):
    m = math.tan(PI / x)
    h = math.hypot(y, z)
    return m, h


def a_sin(x):
    a = math.asin(x)
    return a


def a_cos(x):
    b = math.acos(x)
    return b


def a_tan(x):
    c = math.atan(x)
    return c


def sin_h(x, y):
    z = complex(x, y)
    d = cmath.sinh(z)
    return d


def cos_h(x, y):
    z = complex(x, y)
    e = cmath.cosh(z)
    return e


def tan_h(x, y):
    z = complex(x, y)
    f = cmath.tanh(z)
    return f


def a_sin_h(x, y):
    z = complex(x, y)
    g = cmath.asinh(z)
    return g


def a_cos_h(x, y):
    z = complex(x, y)
    h = cmath.acosh(z)
    return h


def a_tan_h(x, y):
    z = complex(x, y)
    i = cmath.atanh(z)
    return i
