#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:46:24 2021

@author: bharathvbhatt
"""
#***************Includes*******************************************************
""" Adding needed libraries """
import numpy as np
import adi
import matplotlib.pyplot as plt
from scipy.signal import chirp,hilbert
fs = 50e6
N=50000
t = np.arange(0,0.001,1/fs)
f = np.arange(0,fs,fs/N)
fmcw_array = chirp(t,0,0.001,20e6,method='linear')
array_samp = hilbert(fmcw_array)
#array_samp = array_samp.astype(np.complex64)

fmcw_waveform = np.array([])
fmcw_waveform=np.append(fmcw_waveform,array_samp)
fmcw_waveform *=2**14
fmcw_waveform=fmcw_waveform.astype(np.complex64)
fmcw_waveform=np.int_(fmcw_waveform.real) + (np.int_(fmcw_waveform.imag))*1J
fmcw_waveform.tofile("fmcwsamples.iq")

# fft = np.fft.fft(array_samp)
# plt.plot(f,np.abs(fft))

#fig, axs = plt.subplots(2)

#**************Tx -SDR ********************************************************    
sample_rate = fs # sampling rate Hz
center_freq = 2.42e9 # Centre Frequency Hz
sdr = adi.Pluto("ip:192.168.3.1")
sdr.tx_destroy_buffer() #clean or empty the buffer
sdr.sample_rate = int(sample_rate) 
sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 0 # Increase to increase tx power, valid range is -90 to 0 dB
N = 50000 # number of samples to transmit at once
#t = np.arange(N)/sample_rate
samples =  array_samp   #0.5*np.exp(2.0j*np.pi*100e3*t) # Simulate a sinusoid of 100 kHz, so it should show up at 915.1 MHz at the receiver
samples *= 2**14 # The PlutoSDR expects samples to be between -2^14 and +2^14, not -1 and +1 like some SDRs
# Transmit our batch of samples 100 times, so it should be 1 second worth of samples total, if USB can keep up
#for i in range(5):
#    sdr.tx(samples) # transmit the batch of samples once
sdr.tx_cyclic_buffer = True # Enable cyclic buffers
sdr.tx(samples) # transmit the batch of samples once
#**************Rx -SDR ********************************************************

sdr.rx_lo = int(center_freq)
sdr.rx_rf_bandwidth = int(sample_rate)
sdr.rx_buffer_size = N
sdr.gain_control_mode_chan0 = 'slow_attack'  #'manual'# 'slow_attack'##'slow_attack'
sdr.rx_hardwaregain_chan0 = 00.0 # dB, increase for a stronger signal, but be careful not to saturate

# sdr2 = adi.Pluto("ip:192.168.2.1")
# sdr2.rx_lo = int(center_freq)
# sdr2.rx_rf_bandwidth = int(sample_rate)
# sdr2.rx_buffer_size = 50000
# sdr2.gain_control_mode_chan0 ='slow_attack' #'slow_attack' #
# sdr2.rx_hardwaregain_chan0 = 25.0 # dB, increase for a stronger signal, but be careful not to saturate




raw_data = np.array([])
for i in range (0,10):
    raw = sdr.rx()
    #raw = sdr2.rx()


# sdr.tx_destroy_buffer()
# sdr.tx_cyclic_buffer = True # Enable cyclic buffers
# sdr.tx(zeros_samp) # transmit the batch of samples once

for i in range (0,100):   
    raw = sdr.rx()
    #raw = sdr2.rx()
    raw_data = np.append(raw_data,raw)
    
raw_data=raw_data.astype(np.complex64)
raw_data.tofile("raw_data.iq")

 
rx_samples = sdr.rx()
#print(rx_samples)
rx_samples = rx_samples/2**14
# Stop transmitting
sdr.tx_destroy_buffer()

#axs[0].plot(t,np.abs(rx_samples))
#plt.plot(t,rx_samples)
fft = np.fft.fft(rx_samples)
fft_mag = np.abs(fft)
fft_mag[0]=0
#axs[1].plot(f,fft_mag)
plt.plot(f,fft_mag)
#plt.title("Time response of SAW sensor")
#plt.xlabel("Frequency in Hz")
#plt.ylabel("Magnitude")
#plt.savefig("FMCW_response.svg")












