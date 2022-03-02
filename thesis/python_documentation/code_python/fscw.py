#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:43:50 2021

@author: bharathvbhatt
"""

## Constant phase can be obtained by keeping delta f = 1/(4* Ts)

import numpy as np
import math
import scipy
import matplotlib.pyplot as plt
from scipy.signal import chirp,hilbert
#######  FSK ####
fs = 5e6
fc=100
N=5000
t = np.arange(0,1,1/fs)
data = np.arange(0,N,1)
symb = np.array(np.repeat(data,fs/N))
#symb.resize(int(fs))
sig = np.cos(2*np.pi*t*(fc+symb*400))
#f = np.fft.fftfreq(len(sig))
f= np.arange(0,fs,1)
fft_sig = np.fft.fft(sig)
#plt.plot(f,np.abs(fft_sig))

plt.plot(t,sig)
#plt.plot(t,data/N)
#############################################################

# f_sig= 750e3
# fs=10e6
# N= 10
# t= np.arange(0,1,1/10e6)
# f = np.arange(-fs/2,fs/2,fs)
# sig = np.cos(2*np.pi*f_sig*t)

# fft = np.fft.fftshift(np.fft.fft(sig))
# plt.plot(f,np.abs(fft))
#################################FSCW##########################################
# fs =50e6
# ts =1/fs
# f = np.arange(0,1e6,100e3)
# t_sig = np.arange(0,2e-6,ts)
# signal = np.array([])
# for fc in f:
#     signal = np.append(signal,np.sin(2*np.pi*fc*t_sig))
#     signal = np.append(signal,np.zeros(400))

# signal = hilbert(signal)
# signal = signal.astype(np.complex64)
# t = np.arange(5000)*ts
# fft = np.fft.fftshift(np.fft.fft(signal))
# f_sig = np.arange(-fs/2,fs/2,fs/5000)
# #plt.plot(f_sig,np.abs(fft))
# plt.plot(t,signal)

