#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:41:10 2021

@author: bharathvbhatt
"""

import numpy as np
from scipy.signal import hilbert,chirp,iirnotch,freqz,filtfilt,periodogram
import matplotlib.pyplot as plt
import math
###########  SIGNAL ##########################################################
fs = 5e6  # Sample frequency (Hz)
ts = 1/fs
t = np.arange(0,0.001,ts)
N=5000
f= np.arange(-fs/2,fs/2,fs/N)
chirp_sig = chirp(t,0,0.001,2e6,'linear')
sig = np.array([])
sig = hilbert(chirp_sig)
#plt.plot(t,sig,"r-",linewidth=6)
########## CHANNEL ############################################################
d = 10
fc = 2.4218e9
L_fs = 20*math.log10(d)+20*math.log10(fc)-147.55
pathloss=+16-L_fs
variance = 10**(-pathloss/10)
n = (math.sqrt(variance))*(np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2)
sig = sig+n
sig_multipath = np.roll(sig,2)
sig = sig+sig_multipath
#plt.plot(t,sig_multipath,"g-")
######### SAW SIMULATION ######################################################
f0 = 1.7e6  # Frequency to be removed from signal (Hz)
Q = 30.0  # Quality factor
# Design notch filter
b, a = iirnotch(f0, Q, fs)
freq, h = freqz(b, a, fs=fs)
response = filtfilt(b, a, sig)
response = response+n
ft,psd = periodogram(response,fs=fs)
psd[0]=0
plt.plot(ft, np.sqrt(psd))
plt.xlabel('frequency in Hz')
plt.ylabel('Power in V rms')
plt.title('PSD')
#response = response*np.conj(response)
#fft = np.fft.fftshift(np.fft.fft(response))
#plt.plot(f,np.abs(fft))
#plt.plot(t,response)

# Plot
# fig, ax = plt.subplots(2, 1, figsize=(8, 6))
# ax[0].plot(freq, 20*np.log10(abs(h)), color='blue')
# ax[0].set_title("Frequency Response")
# ax[0].set_ylabel("Amplitude (dB)", color='blue')
# ax[0].set_xlim([0, 100])
# ax[0].set_ylim([-25, 10])
# ax[0].grid()
# ax[1].plot(freq, np.unwrap(np.angle(h))*180/np.pi, color='green')
# ax[1].set_ylabel("Angle (degrees)", color='green')
# ax[1].set_xlabel("Frequency (Hz)")
# ax[1].set_xlim([0, 100])
# ax[1].set_yticks([-90, -60, -30, 0, 30, 60, 90])
# ax[1].set_ylim([-90, 90])
# ax[1].grid()
# plt.show()











































# import numpy as np
# import matplotlib.pyplot as plt
# import adi
# fs = 5e6
# ts = 1/fs
# fc = 800e3
# N =4096
# f = np.arange(-fs/2,fs/2,fs/N)
# t = np.arange(4096)*ts

# sig = np.array([])
# sig = np.append(sig,np.sin(2*np.pi*fc*t))




# sample_rate = fs # sampling rate Hz
# center_freq = 2.421e9 # Centre Frequency Hz
# sdr = adi.Pluto("ip:192.168.3.1")
# sdr.tx_destroy_buffer() #clean or empty the buffer
# sdr.sample_rate = int(sample_rate) 
# sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
# sdr.tx_lo = int(center_freq)
# sdr.tx_hardwaregain_chan0 = -10 # Increase to increase tx power, valid range is -90 to 0 dB
# samples =  sig  #0.5*np.exp(2.0j*np.pi*100e3*t) # Simulate a sinusoid of 100 kHz, so it should show up at 915.1 MHz at the receiver
# samples *= 2**14 # The PlutoSDR expects samples to be between -2^14 and +2^14, not -1 and +1 like some SDRs

# sdr.tx_cyclic_buffer = True # Enable cyclic buffers
# sdr.tx(samples) # transmit the batch of samples once 


# sdr2 = adi.Pluto("ip:192.168.2.1")
# center_freq = 2.421e9 # Centre Frequency Hz
# sdr2.rx_lo = int(center_freq)
# sdr2.rx_rf_bandwidth = int(sample_rate)
# sdr2.rx_buffer_size = N
# sdr2.gain_control_mode_chan0 = 'slow_attack'
# sdr2.rx_hardwaregain_chan0 = 0.0 # dB, increase for a stronger signal, but be careful not to saturate

# raw_data = np.array([])
# for i in range (0,10):
#     raw = sdr2.rx()
     


# for i in range (0,100):   
#     raw = sdr2.rx()
#     raw_data = np.append(raw_data,raw)

# rx_samples = sdr2.rx()    
# #sdr.tx_destroy_buffer()  
# fft = np.fft.fftshift(np.fft.fft(rx_samples))
# fft_mag = np.abs(fft)
# # fft_mag[0]=0
# plt.plot(f,fft_mag)