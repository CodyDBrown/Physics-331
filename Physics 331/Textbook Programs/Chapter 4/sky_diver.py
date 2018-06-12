#!/usr/bin/env python3
"""
Created on Mon May 28 12:12:20 2018

@author: cody
"""
from numpy import sqrt
def sky_diver(v,t):
    g = 9.8         # Acceleration from gravity (m/s/s)
    rho = 1.2       # Mass density of the air they're falling in (kg/m**3)
    a = 1.0         # cross-sectional area of the sky diver (m**2)
    C_d = 1.0       # coefficient of drag
    M = 100.0       # mass of the diver (kg)
    alpha = 0.5 * rho * a * C_d / M
    return g - alpha * abs(v)*v
    