#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:03:45 2022

@author: bharathvbhatt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
fs = 100e3
tb= 1e-3
t = np.arange(0,8*tb,1/fs)
b = 2*np.random.randint(2,size=8)-1
fc=5e3
h=1

b = np.tile(b, (100,1)).flatten('F')
b_integrated = lfilter([1.0],[1.0,-1.0],b)/fs #Integrate b using filter
theta= np.pi*h/tb*b_integrated

s = np.cos(2*np.pi*fc*t + theta) # CPFSK signal
f = np.arange(-fs/2,fs/2,fs/800)
plt.plot(f,b_integrated)
