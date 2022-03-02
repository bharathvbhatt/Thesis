#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:16:46 2021

@author: bharathvbhatt
"""
import numpy as np
import adi
import matplotlib.pyplot as plt
import scipy as sy
from scipy.signal import chirp,hilbert
import time

fc = np.arange(100)*10e3

fs = 50e6
T = 1e-6
#fc =300e3
ts = 1/fs
N=5000
len_zeropadd = int(N - (fs*T)-5000)
f = np.arange(-fs/2,fs/2,fs/N)
t = np.arange(0,2e-6,ts)


sample_rate = fs # sampling rate Hz
center_freq = 2.418e9 # Centre Frequency Hz
sdr = adi.Pluto("ip:192.168.3.1")
sdr.tx_destroy_buffer() #clean or empty the buffer
sdr.sample_rate = int(sample_rate) 
sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 00 # Increase to increase tx power, valid range is -90 to 0 dB

center_freq = 2.41e9 # Centre Frequency Hz
sdr.rx_lo = int(center_freq)
sdr.rx_rf_bandwidth = int(sample_rate)
sdr.rx_buffer_size = 5000
sdr.gain_control_mode_chan0 = 'manual'# #
sdr.rx_hardwaregain_chan0 =40.0 # dB, increase for a stronger signal, but be careful not to saturate
sdr.tx_cyclic_buffer = True # Enable cyclic buffers

raw_data = np.array([])
for f in fc:
    sig = np.array([])
    sig = np.append(sig,np.cos(2*np.pi*f*t))
    array_samp = np.array([])
    array_samp = np.append(array_samp,hilbert(sig))
    array_samp =array_samp.astype(np.complex64)
    array_samp = np.append(array_samp,np.zeros(4900))

    samples =  array_samp  #0.5*np.exp(2.0j*np.pi*100e3*t) # Simulate a sinusoid of 100 kHz, so it should show up at 915.1 MHz at the receiver
    samples *= 2**14 # The PlutoSDR expects samples to be between -2^14 and +2^14, not -1 and +1 like some SDRs
    sdr.tx(samples) # transmit the batch of samples once 

    for i in range (0,10):
        raw = sdr.rx()
    
    for i in range (0,10):   
        raw = sdr.rx()
        raw_data = np.append(raw_data,raw)
    
    rx_samples = sdr.rx()

    # Stop transmitting
    sdr.tx_destroy_buffer()
raw_data=raw_data.astype(np.complex64)
raw_data.tofile("raw_data.iq")

f_c = 2.41e9
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
res_freq = freq_avg*fs/N+f_c
print(res_freq/1.0e9)




























