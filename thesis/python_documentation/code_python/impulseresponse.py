#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 13:17:57 2022

@author: bharathvbhatt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp,hilbert
import tikzplotlib
fs = 500
f0 = 10
t = np.arange(0,1,1/fs)
f = np.arange(0,fs,fs/500)
sig1 = chirp(t,0,1,20,'linear')
sig2 = np.roll(sig1,50)*np.exp(-1j*np.pi/3)
sig3 = np.roll(sig1,20)
sig4 = sig1*np.exp(-1j*np.pi*f0*t)
y = sig1+sig4+sig2+sig3


x_fft = np.fft.fft(sig1)
y_fft = np.fft.fft(y)
h_fft = y_fft/x_fft

#plt.plot(f,h_fft)

new=np.array([])
h = np.fft.ifft(h_fft)
new = np.abs(h)>0.5
h=h*new
#phase = np.arctan2(np.imag(h),np.real(h))*180/np.pi
#plt.plot(t,sig1)
#plt.plot(t,sig4)
plt.plot(t,h)
#plt.plot(f,phase)
