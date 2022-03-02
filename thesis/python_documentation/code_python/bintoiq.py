#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:20:38 2021

@author: bharathvbhatt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp,hilbert
import scipy as sy


fp = open("rx.bin","r")
data_real=np.array([])
data_imag=np.array([])
for i in range(0,25000):
   val=fp.readline().split(" ")
   if(i==9640):
       val[0]=-14
   if(i==14339):
       val[0]=-8

   data_real=np.append(data_real,int(val[0]))
   data_imag=np.append(data_imag,int(val[1]))
   
   
   
#data =np.array([])
#data = np.fromfile("rx.bin",sep=" ")
#len_array = len(data)
# data_real = data[0:len_array-1:2]
# data_imag = data[1:len_array:2]

complex_data = data_real+1j*data_imag
complex_data=complex_data.astype(np.complex64)
complex_data.tofile("plutorx.iq")

#fft_mag=np.abs(complex_data)
#fft_bin = np.argmax(fft_mag)
