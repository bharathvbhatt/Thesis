#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:30:36 2021

@author: bharathvbhatt
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from scipy.signal import chirp,hilbert
import adi
from matplotlib import mlab as mlab
import time
from collections import deque 
from itertools import count
fs = 50e6
T = 1e-6
fc =300e3
ts = 1/fs
N=5000 #5000
len_zeropadd = int(N - (fs*T)-5000)
f = np.arange(-fs/2,fs/2,fs/N)
t = np.arange(0,2e-6,ts)
sig = np.array([])
sig = np.append(sig,np.cos(2*np.pi*fc*t))
 

array_samp = np.array([])
array_samp = np.append(array_samp,hilbert(sig))
array_samp =array_samp.astype(np.complex64)
array_samp = np.append(array_samp,np.zeros(4900))#4900




#**************Tx -SDR ********************************************************    
sample_rate = fs # sampling rate Hz
center_freq = 2.418e9 # Centre Frequency Hz
sdr = adi.Pluto("ip:192.168.3.1")
sdr.tx_destroy_buffer() #clean or empty the buffer
sdr.sample_rate = int(sample_rate) 
sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 00 # Increase to increase tx power, valid range is -90 to 0 dB
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
center_freq = 2.41e9 
sdr.rx_lo = int(center_freq)
sdr.rx_rf_bandwidth = int(sample_rate)
sdr.rx_buffer_size = N
sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 20.0 # dB, increase for a stronger signal, but be careful not to saturate


cnt =count()
cnt1 = count()
x =deque(np.zeros(100))
y =deque(np.zeros(100))
raw_data=np.array([])
all_raw = np.array([])
def animate(i):
    global raw_data
    global all_raw
    for i in range (0,10):
        raw = sdr.rx()
    raw_data = sdr.rx()
    raw_data =raw_data.astype(np.complex64)
    raw_data.tofile("raw_data"+str(next(cnt1))+".iq")
    all_raw=np.append(all_raw,raw_data)
    bin_fft=list()
    start_f =0
    end_f = 0
    for i in range(0,50000,5000): #5000000
        start_f = i
        end_f = i+5000
        samp = np.array([])
        samp = np.append(samp,raw_data[start_f:end_f])
        sig = samp
        # sig_index = np.abs(samp)>0.01
        # sig = sig*sig_index
        # index = np.where(sig_index==True)
        # index = index[0][0:115]
        # sig_index[index]=False
        # sig = sig*sig_index
        sig_index = np.abs(samp)>0.05#0.01
        index = np.where(sig_index==True)
        if((index[0][0]>10 and index[0][-1]<4990)):
            index = index[0][0:100]
            sig[index]=0
            start_index= index[99]
            stop_index=start_index+100
            sig[0:start_index]=0
            sig[stop_index:]=0
        fft_mag = np.abs((np.fft.fft(sig)))
        bin_fft.append(np.argmax(fft_mag))
    fft_value = np.array([])
    fft_value=np.append(fft_value,bin_fft)
    #fft_value.astype(np.int64)
    #fft_value.tofile("fft_val.txt")
    freq_avg = sum(bin_fft)/len(bin_fft)
    res_freq = (freq_avg)*fs/N+fc
    x.popleft()
    x.append(next(cnt))
    y.popleft()
    y.append(freq_avg)#res_freq
    plt.cla()
    plt.plot(x,y)
    #res_freq = (freq_avg)*fs/N+fc
    #print(res_freq/1.0e9)
    #plt.plot(f,fft_mag)


ani = FuncAnimation(plt.gcf(), animate, interval=1)
plt.show()
    

