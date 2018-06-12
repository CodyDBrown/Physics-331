#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:44:57 2018

@author: cody
"""
import numpy as np
def efld(x):
    eps0 = 8.8542e-12
    #Charge 'a'
    xa = np.array([0.0, 0.0])    # possitions of 'a'
    qa = 1.0                # Charge of 'a'
    
    xb = np.array([1.0, 0.0])    
    qb = 3.0
    
    xc = np.array([0.0, 0.5])
    qc = -4.0
    
    ra = x - xa
    rb = x - xb
    rc = x - xc
    
    ra_mag = np.sqrt(ra[0]**2 + ra[1]**2) 
    rb_mag = np.sqrt(rb[0]**2 + rb[1]**2)
    rc_mag = np.sqrt(rc[0]**2 + rc[1]**2)
    
    e = (qa * ra / ra_mag**3 + qb * rb / rb_mag**3 + qc * rc / rc_mag**3) / (4 * np.pi * eps0)
    return e