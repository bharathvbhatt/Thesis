#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:25:43 2021

@author: bharathvbhatt
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import chirp,hilbert
import time
import scipy as sy
from scipy.signal import kaiserord, lfilter, firwin, freqz
from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show
##################### Exponential Decay #######################################
N_sig =500 #500
sensor_fs =50e6 #50e6
sensor_ts =1/sensor_fs

sensor_t = np.arange(1*sensor_ts,10e-6,sensor_ts)
tau = 1e-6
#sensor_fc = 1526e3

sensor_fc1 = 1e6
#sensor_fc2 = 18.6e6

sensor_sig1 = np.cos(2*np.pi*sensor_fc1*sensor_t)
#sensor_sig2 = np.cos(2*np.pi*sensor_fc2*sensor_t)
sensor_a = np.exp(-sensor_t/tau)
sensor_sig = sensor_a*sensor_sig1#+sensor_a*sensor_sig2

#nq_rate = sensor_fs/2
#width = 50000.0/nq_rate
#cutoff_hz = 20.0e6
#ripple_db = 60.0
#N, beta = kaiserord(ripple_db, width)
#taps = firwin(N, cutoff_hz/nq_rate)#,window=('kaiser', beta))
#filtered_x = lfilter(taps, 1.0, sensor_sig)


sensor_sig[200:]=0

#sensor_sig2 = 0.5*np.roll(sensor_sig,-10)

#corr = sy.signal.signaltools.correlate(sensor_sig,sensor_sig2)
#dt = np.arange(1-N, N)
#t_shift = dt[corr.argmax()]
#plt.plot(sensor_t,(filtered_x))
#plt.plot(sensor_t,(sensor_sig))


#***************** Fourier Transform ********************************#
sensor_f = np.arange(-sensor_fs/2,sensor_fs/2,sensor_fs/N_sig)
sensor_fft_mag = np.abs(np.fft.fftshift(np.fft.fft(sensor_sig)))
#sensor_db= 10*np.log10(sensor_fft_mag)
#sensor_fft_phase = np.angle(np.fft.fftshift(np.fft.fft(sensor_sig)))
#freq = np.argmax(sensor_fft_mag)*sensor_fs/N
#plt.plot(sensor_f,sensor_fft_phase)
plt.plot(sensor_f,sensor_fft_mag)
###############################################################################


# fs =5e6
# T = 0.001
# ts =1/fs
# N =5000
# len_zero = int(N - (fs*T))

# f = np.arange(-fs/2,fs/2,fs/N)

# t_sig = np.arange(0,0.001,ts)



# tx_fmcw = chirp(t_sig,0,0.001,2e6,'linear')
# tx_fmcw_bb = np.array([])
# tx_fmcw_bb = np.append(tx_fmcw_bb,hilbert(tx_fmcw))

# delay1 = 1
# delay2 = 3
# delay3 = 4
# delay4 = 8

# rx_sig1 = np.array([])
# rx_sig1 = np.append(rx_sig1,hilbert(np.zeros(5000)))
# rx_sig1 = np.insert(rx_sig1,delay1,tx_fmcw_bb)
# #rx_sig1[100:150]=rx_sig1[100:150]+hilbert(sensor_sig)


# rx_sig2 = np.array([])
# rx_sig2 = np.append(rx_sig2,hilbert(np.zeros(5000)))
# rx_sig2 = np.insert(rx_sig2,delay2,tx_fmcw_bb)

# rx_sig3 = np.array([])
# rx_sig3 = np.append(rx_sig3,hilbert(np.zeros(5000)))
# rx_sig3 = np.insert(rx_sig3,delay3,tx_fmcw_bb)

# rx_sig4 = np.array([])
# rx_sig4 = np.append(rx_sig4,hilbert(np.zeros(5000)))
# rx_sig4 = np.insert(rx_sig4,delay4,tx_fmcw_bb)



# rx_sig = np.array([])
# rx_sig = 10*rx_sig1 + 2*rx_sig2+0.5*rx_sig3+2*rx_sig4

# rx_sig = rx_sig[0:5000]
# # rx_sig = np.conj(rx_sig1[0:5000])


# t1 = np.arange(5000)*ts
# #plt.plot(t1,rx_sig)

# fft = np.fft.fftshift(np.fft.fft(rx_sig))
# fft_mag = np.abs(fft)
# plt.plot(f,fft_mag)


# down_con = (rx_sig)
# zero = np.zeros(len_zero, dtype=np.complex128)
# down_con = np.append(down_con, zero)



#t1 = np.arange(0,N,1)
#plt.plot(t1,np.abs(down_con))
# fft_mag = np.abs(np.fft.fftshift(np.fft.fft(down_con)))
# #index = fft_mag>200
# #index = np.invert(index)
# #fft_mag = fft_mag*index
# plt.plot(f,fft_mag)


###############################################################################
# N= 5000
# fsamp =500e3
# fc = 100e3
# T =10e-3
# tc = np.arange(0,T,1/fsamp)
# carrier = np.cos(2*np.pi*fc*tc)


# fs =1000
# ts = np.arange(0,T,1/fsamp)
# message1 = np.cos(2*np.pi*fs*ts)

# pass_band = carrier*message1 + carrier

# fft = np.fft.fftshift(np.fft.fft(pass_band))
# f = np.arange(-fsamp/2,fsamp/2,fsamp/N)

# plt.plot(f,np.abs(fft))


################## Amplitude Demodulation #####################################
# fs =5e6
# ts =1/fs
# fc = 10e3
# t = np.arange(1*ts,1e-3,ts)
# cos_sig = np.cos(2*np.pi*fc*t)
# tau =1e-4
# t_exp =np.arange(1e-3,2e-3,ts)
# sensor_sig = np.cos(2*np.pi*1*fc*t_exp) 
# sensor_a = np.exp(-t_exp/tau)
# sensor_sig=1e5*sensor_sig*sensor_a/4

# tsig = np.arange(10000)*ts
# sig = np.array([])
# sig = np.append(sig,cos_sig)
# sig = np.append(sig,sensor_sig)
# t = np.arange(10000)*ts
# cos_sig= np.cos(2*np.pi*fc*t)
# sig = sig*cos_sig
# f = np.arange(-fs/2,fs/2,fs/10000)
# fft = np.fft.fftshift(np.fft.fft(sig))
# plt.plot(f,np.abs(fft))
#plt.plot(t,sig)
###############################################################################










