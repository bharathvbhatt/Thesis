#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:59:38 2021

@author: bharathvbhatt
"""

import numpy as np
import adi
import matplotlib.pyplot as plt
import scipy as sy
from scipy.signal import chirp,hilbert
import time
################# Cosine waveform #############################################

fs = 50e6 #40.96e6
T = 1e-6
fc =930e3
ts = 1/fs
N= 5000#4096
len_zeropadd = int(N - (fs*T)-5000)
f = np.arange(-fs/2,fs/2,fs/N)
t = np.arange(0,2e-6,ts)
sig = np.array([])
sig = np.append(sig,np.cos(2*np.pi*fc*t))
 

array_samp = np.array([])
array_samp = np.append(array_samp,hilbert(sig))
array_samp =array_samp.astype(np.complex64)
array_samp = np.append(array_samp,np.zeros(4900))#4014


####################10 frequencies ################################
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
# array_samp =signal
##############################################################

#t1 = np.arange(50)*ts
#plt.plot(t1,sig)
sample_rate = fs # sampling rate Hz
center_freq = 2.416e9 # Centre Frequency Hz
sdr = adi.Pluto(uri="ip:192.168.3.1")

sdr.tx_destroy_buffer() #clean or empty the buffer
sdr.sample_rate = int(sample_rate) 

sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = -10 # Increase to increase tx power, valid range is -90 to 0 dB
samples =  array_samp  #0.5*np.exp(2.0j*np.pi*100e3*t) # Simulate a sinusoid of 100 kHz, so it should show up at 915.1 MHz at the receiver
samples *= 2**14 # The PlutoSDR expects samples to be between -2^14 and +2^14, not -1 and +1 like some SDRs

sdr.tx_cyclic_buffer = True # Enable cyclic buffers
sdr.tx(samples) # transmit the batch of samples once 
center_freq = 2.41e9 # Centre Frequency Hz
#sdr.rx_enabled_channels = [0, 1]
sdr.rx_lo = int(center_freq)
sdr.rx_rf_bandwidth = int(sample_rate)
sdr.rx_buffer_size = 5000
sdr.gain_control_mode_chan0 ='manual'#
sdr.rx_hardwaregain_chan0 =40.0 # dB, increase for a stronger signal, but be careful not to saturate
#sdr.gain_control_mode_chan1 = 'manual'# #
#sdr.rx_hardwaregain_chan1 =10
# sdr2 = adi.Pluto("ip:192.168.2.1")
# sdr2.rx_lo = int(center_freq)
# sdr2.rx_rf_bandwidth = int(sample_rate)
# sdr2.rx_buffer_size = 5000
# sdr2.gain_control_mode_chan0 ='manual' #'slow_attack' #
# sdr2.rx_hardwaregain_chan0 = 0.0 # dB, increase for a stronger signal, but be careful not to saturate


raw_data = np.array([])
for i in range (0,10):
    raw = sdr.rx()
    #raw = sdr2.rx() 

#with open("raw_data.iq",'w+') as file:
for i in range (0,100):   
    raw = sdr.rx()
    #raw = sdr2.rx()
    raw_data = np.append(raw_data,raw)
raw_data=raw_data.astype(np.complex64)
raw_data.tofile("raw_data.iq")


rx_samples = sdr.rx()
#print(rx_samples)

# Stop transmitting
sdr.tx_destroy_buffer()
#rx_samples = np.append(rx_samples,np.zeros(len_zeropadd))

rx_samples = rx_samples[0:5000]
t_res = np.arange(5000)*ts
#plt.plot(t_res,rx_samples)

# fig,axs = plt.subplots(2)
# t1 = np.arange(N)/fs
# axs[0].plot(t1,(rx_samples))
#fft = np.fft.fftshift(np.fft.fft(rx_samples))
##fft_mag = np.abs(fft)
#fft_mag[0]=0
#plt.plot(f,fft_mag)