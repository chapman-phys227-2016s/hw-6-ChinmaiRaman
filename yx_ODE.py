#! /usr/bin/env python

"""
File: yx_ODE
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: C.3
Date: April 4th, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Uses a forward Euler method to solve an ODE problem for a varying step size in x
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def euler(step, y0):
    """
    Implements Euler's method for the differential equation dy/dx = 1/(2(y-1)) on the interval [0,4]
    """
    x = [0]
    index_x = 0
    while x[index_x] < 4:
        x.append(x[index_x] + step)
        index_x += 1
    index_y = 0
    y = [y0]
    def yprime(y):
        yprime = 1 / (2 * (y - 1))
        return yprime
    while index_y < index_x:
        y.append(y[index_y] + step * yprime(y[index_y]))
        index_y += 1
    return x, y

def graph_euler():
    """
    Graphs the differential equation dy/dx = 1/(2(y-1)) given y(0) = 1 + sqrt(epsilon) for vary
    """
    fig = plt.figure(1)
    x1 = euler(1, 1 + np.sqrt(1e-3))[0]
    y1 = euler(1, 1 + np.sqrt(1e-3))[1]
    x2 = euler(0.25, 1 + np.sqrt(1e-3))[0]
    y2 = euler(0.25, 1 + np.sqrt(1e-3))[1]
    x3 = euler(0.01, 1 + np.sqrt(1e-3))[0]
    y3 = euler(0.01, 1 + np.sqrt(1e-3))[1]
    x_actual = np.linspace(0, 6, 1001)
    y_actual = 1 + np.sqrt(x_actual + 1e-3)
    plt.plot(x1, y1, 'r-', label = "line 1")
    plt.plot(x2, y2, 'g-')
    plt.plot(x3, y3, 'b-')
    plt.plot(x_actual, y_actual, 'y-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)')
    plt.show()
    
def sym_solve():
    x = sp.symbols('x')
    f = sp.Function('f')
    return sp.dsolve(sp.Eq(sp.Derivative(f(x), x), 1 / (2 * (f(x) - 1))))[1]
    
def sym_euler(step, y0):
    x = np.linspace(0, 4, 4 / step)

def test_euler():
    assert euler(0.0001, 1 + np.sqrt(1e-3))[1][-1] - 3.0003019764418086 < 1e-10