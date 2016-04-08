#! /usr/bin/env python

"""
File: unstable_ODE
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: C.4
Date: April 7th, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Demonstrates the instability of an ODE
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def euler(alpha, u0, step, lowerbound, upperbound):
    """
    Implements the forward Euler's method
    """
    x = np.linspace(lowerbound, upperbound, (upperbound - lowerbound) / step + 1)
    u = np.zeros(len(x))
    u[0] = u0
    for i in range(len(x) - 1):
        du = alpha * u[i]
        u[i + 1] = u[i] + du * step
    return x, u

def graph(alpha, u0, step, lb, ub):
    fig = plt.figure(1)
    plt.plot(euler(alpha, u0, step, lb, ub)[0], euler(alpha, u0, step, lb, ub)[1], 'b-')
    plt.xlabel('k')
    plt.ylabel('u')
    plt.title('u(k)')
    plt.show()