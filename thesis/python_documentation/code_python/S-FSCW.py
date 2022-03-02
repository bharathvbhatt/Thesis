#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:23:42 2021

@author: bharathvbhatt
"""

import numpy as np
import matplotlib.pyplot as plt

frequency = np.arange(100,3200,100)
power= [8.1726e-13,
        1.63713e-11,
        2.733e-11,
        1.841e-11,
        1.21e-11,
        7.49e-12,
        3.739e-11,
        3.55e-11,
        3.862e-11,
        3.758e-11,
        4.318e-11,
        3.4e-11,
        7.4803e-11,
        5.711e-11,
        3.4784e-11,
        1.608e-10,
        1.6242e-11,
        2.65404e-11,
        2.075e-11,
        1.404e-11,
        1.73e-11,
        1.774e-10,
        1.375e-11,
        8.92e-12,
        5.633e-12,
        8.3632e-12,
        3.8190e-12,
        1.40285e-11,
        5.362e-12,
        4.068e-12,
        5.077e-12]

plt.plot(frequency,power)