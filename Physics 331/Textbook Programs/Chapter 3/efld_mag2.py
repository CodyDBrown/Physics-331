#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:56:38 2018

@author: cody
"""

def efld_mag2(x):
    e = efld(x)
    mag = e[0]**2 + e[1]**2
    return mag