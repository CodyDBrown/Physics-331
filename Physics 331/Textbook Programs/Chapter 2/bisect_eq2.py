#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 20:16:10 2018

@author: cody
"""
import numpy as np

def bisect_eq2(x_left, x_rigt):
    """
    Find a solution to the equation f(x) = e^x - 3*x^2 using a bisection method.
    Starts with the interval between x_left, x_right and returns a solution. 
    The Solution will be accurate to 0.5e-5
    """
    f_left = np.exp(x_left) - 3*x_left**2
    f_rigt = np.exp(x_rigt) - 3*x_rigt**2
    
    while x_rigt - x_left > 1.0e-7:
        x_mp = 0.5*(x_left + x_rigt)    # Mid-point
        f_mp = np.exp(x_mp) - 3*x_mp**2 # Function evaluated at the mid point
        
        if f_mp * f_left > 0.0:         # mp value has same sign as left
            x_left = x_mp               # Reset the left to be the mp
            f_left = f_mp
        else:
            x_rigt = x_mp               # or set right value to mp

    return 0.5*(x_left + x_rigt)
            