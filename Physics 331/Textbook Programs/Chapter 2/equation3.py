#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 21:59:20 2018

@author: cody
"""
import numpy as np
def equation3(theta):
    """
    Evalueate equation 3. Input should be in degrees.
    """
    th_rad = np.pi*theta/180.0;    # Convert the input into radian
    
    return 250*np.cos(th_rad)* (np.sin(th_rad) + np.sqrt( np.sin(th_rad)**2 + 0.08 ) ) - 200