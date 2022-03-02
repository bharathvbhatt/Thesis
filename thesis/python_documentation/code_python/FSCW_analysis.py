#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:01:31 2021

@author: bharathvbhatt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp,hilbert

fmcw_array=np.array([])
fc = 2.415e9
fs = 50e6 #50e6
ts=1/fs
T = 1e-3
N=5000 #5050
len_zero = int(N-(fs*T))
t = np.arange(0,1e-3,1/fs)
f = np.arange(-fs/2,fs/2,fs/N)
raw_data = np.fromfile("raw_data.iq",np.complex64)
raw_data=raw_data/(2**14)

#############fft averaging#####################################################
bin_fft=list()
start_f =0
end_f = 0

for i in range(0,500000,5000):
    start_f = i
    end_f = i+5000
    samp = np.array([])
    samp = np.append(samp,raw_data[start_f:end_f])
    sig = samp
    sig_index = np.abs(samp)>0.01
    sig = sig*sig_index
    index = np.where(sig_index==True)
    index = index[0][0:113]
    sig_index[index]=False
    sig = sig*sig_index
    fft_mag = np.abs((np.fft.fft(sig)))
    bin_fft.append(np.argmax(fft_mag))
fft_value = np.array([])
fft_value=np.append(fft_value,bin_fft)
#fft_value.astype(np.int64)
fft_value.tofile("fft_val.txt")

freq_avg = sum(bin_fft)/len(bin_fft)
res_freq = freq_avg*fs/N+fc
print(res_freq/1.0e9)