#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 12:09:03 2021

@author: bharathvbhatt
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from scipy.signal import chirp,hilbert
import adi
from matplotlib import mlab as mlab
fs = 5e6
N=5000

t = np.arange(0,0.001,1/fs)
f = np.arange(-fs/2,fs/2,fs/N)
fmcw_array = chirp(t,0,0.001,2e6,method='linear')
array_samp = hilbert(fmcw_array)

fig = plt.figure()
graph_out = fig.add_subplot(1, 1, 1)


#**************Tx -SDR ********************************************************    
sample_rate = fs # sampling rate Hz
center_freq = 2.42e9 # Centre Frequency Hz
sdr = adi.Pluto("ip:192.168.3.1")
sdr.tx_destroy_buffer() #clean or empty the buffer
sdr.sample_rate = int(sample_rate) 
sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 00 # Increase to increase tx power, valid range is -90 to 0 dB
N = 5000 # number of samples to transmit at once
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
sdr.gain_control_mode_chan0 = 'slow_attack'
sdr.rx_hardwaregain_chan0 = 0.0 # dB, increase for a stronger signal, but be careful not to saturate







def animate(i):
    graph_out.clear()
    global samples 
    samples= np.array([])
    samples = sdr.rx()
    samples =samples.astype(np.complex64)/(2**14)
    samples.tofile("raw_data.iq")
    fft = np.fft.fftshift(np.fft.fft(samples))
    fft_mag = np.abs(fft)
    #fft_mag[0]=0
    plt.plot(f,fft_mag)
    # use matplotlib to estimate and plot the PSD
    #graph_out.psd(samples,window=np.hamming(5000), NFFT=5000, Fs=sample_rate , Fc=center_freq)
    #graph_out.xlabel('Frequency (MHz)')
    #graph_out.ylabel('Relative power (dB)')
    #graph_out.magnitude_spectrum(samples,Fs=fs,scale='dB',window=np.hamming(50000),Fc=center_freq)

try:
    for i in range (0,10):
        raw = sdr.rx()
    ani = FuncAnimation(fig, animate, interval=1)
    #animate()
    plt.show()
    
except KeyboardInterrupt:
    pass
finally:
    sdr.tx_destroy_buffer()
