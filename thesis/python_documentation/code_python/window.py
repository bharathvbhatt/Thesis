#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 17:44:33 2022

@author: bharathvbhatt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import hamming,hann,blackman,blackmanharris,bartlett,exponential
from scipy.signal import hilbert

fs = 50e6
N =5000
ts = 1/fs
fc=  1e6
t = np.arange(0,2e-6,ts)
f = np.arange(-fs/2,fs/2,fs/N)
t_sig = np.arange(5000)*ts
sig = np.cos(2*np.pi*fc*t)


sig_exp = sig*exponential(100)

sig_ham = sig*hamming(100)
sig_ham = np.append(sig_ham,np.zeros(4900))
sig_han = sig*hann(100)
sig_han = np.append(sig_han,np.zeros(4900))
sig_bart = sig*bartlett(100)
sig_bart = np.append(sig_bart,np.zeros(4900))
sig_black = sig*blackman(100)
sig_black = np.append(sig_black,np.zeros(4900))
sig_blachar = sig*blackmanharris(100)
sig_blachar = np.append(sig_blachar,np.zeros(4900))

sig_exp = np.append(sig_exp,np.zeros(4900))
sig = np.append(sig,np.zeros(4900))


fft = np.fft.fftshift(np.fft.fft(sig_han))
plt.plot(f,(np.abs(fft)))

#plt.plot(t,sig_exp)