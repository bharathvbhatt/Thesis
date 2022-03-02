#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:16:18 2022

@author: bharathvbhatt
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import signal
from scipy.fft import fftshift

fs=2e6
N = 1024

img = Image.open("/home/bharathvbhatt/Downloads/ihf_neu_farbe.png").convert('L')
a = list(img.getdata())
a = np.reshape(a,(274,887))


sig = np.array([])
for i in range(0,274):
   ifft = np.fft.ifftshift(np.fft.ifft(a[i]))    
   sig = np.append(sig,ifft)
   


#sig = np.reshape(sig, (450,800))


f, t, Sxx = signal.spectrogram(sig,2000,return_onesided=False)
plt.pcolormesh(t, fftshift(f), Sxx, shading='gouraud')
#powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(sig, Fs=20)
plt.show()