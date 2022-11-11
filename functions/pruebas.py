import sympy as smp
import numpy as np
import matplotlib.pyplot as plt


"""from platform import java_ver
import mpmath
from decimal import *

z_1 = 4
z_2 = 2+1j

theta_t = mpmath.asin((z_1/z_2)*mpmath.si(mpmath.pi/6))
print(theta_t)
print(type(theta_t))


alpha = ((mpmath.cos(theta_t))) / ((35))
print(alpha)"""

x = smp.symbols('x')
m = x**2
y = smp.sin(x)
p = x**2-y
print(p)
