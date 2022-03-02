#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:35:15 2021

@author: bharathvbhatt
"""

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

fc = np.arange(201)*10e3

# fs = 50e6
# T = 1e-6
# #fc =300e3
# ts = 1/fs
# N=5000
# len_zeropadd = int(N - (fs*T)-5000)
# f = np.arange(-fs/2,fs/2,fs/N)
# t = np.arange(0,2e-6,ts)


# sample_rate = fs # sampling rate Hz
# center_freq = 2.418e9 # Centre Frequency Hz
# sdr = adi.Pluto("ip:192.168.3.1")
# sdr.tx_destroy_buffer() #clean or empty the buffer
# sdr.sample_rate = int(sample_rate) 
# sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
# sdr.tx_lo = int(center_freq)
# sdr.tx_hardwaregain_chan0 = 00 # Increase to increase tx power, valid range is -90 to 0 dB

# center_freq = 2.41e9 # Centre Frequency Hz
# sdr.rx_lo = int(center_freq)
# sdr.rx_rf_bandwidth = int(sample_rate)
# sdr.rx_buffer_size = 50000
# sdr.gain_control_mode_chan0 = 'manual'# #
# sdr.rx_hardwaregain_chan0 =40.0 # dB, increase for a stronger signal, but be careful not to saturate
# sdr.tx_cyclic_buffer = True # Enable cyclic buffers

# raw_data = np.array([])
# for f in fc:
#     sig = np.array([])
#     sig = np.append(sig,np.cos(2*np.pi*f*t))
#     array_samp = np.array([])
#     array_samp = np.append(array_samp,hilbert(sig))
#     array_samp =array_samp.astype(np.complex64)
#     array_samp = np.append(array_samp,np.zeros(4900))

#     samples =  array_samp  #0.5*np.exp(2.0j*np.pi*100e3*t) # Simulate a sinusoid of 100 kHz, so it should show up at 915.1 MHz at the receiver
#     samples *= 2**14 # The PlutoSDR expects samples to be between -2^14 and +2^14, not -1 and +1 like some SDRs
#     sdr.tx(samples) # transmit the batch of samples once 

#     for i in range (0,10):
#         raw = sdr.rx()
    
#     #for i in range (0,10):   
#     raw = sdr.rx()
#     raw_data = np.append(raw_data,raw)
    
#     rx_samples = sdr.rx()

#     # Stop transmitting
#     sdr.tx_destroy_buffer()
# raw_data=raw_data.astype(np.complex64)
# raw_data.tofile("raw_data.iq")

# f_c = 2.41e9
# fs = 50e6 #50e6
# ts=1/fs
# T = 1e-3
# N=5000 #5050
# len_zero = int(N-(fs*T))
# t = np.arange(0,1e-3,1/fs)
# f = np.arange(-fs/2,fs/2,fs/N)
# raw_data = np.fromfile("raw_data.iq",np.complex64)
# raw_data=raw_data/(2**14)

# # #############fft averaging#####################################################

# bin_fft=list()
# start_f =0
# end_f = 0
# last_value=0;

# for i in range(0,10000000,5000): #5000000
#     start_f = i
#     end_f = i+5000
#     samp = np.array([])
#     samp = np.append(samp,raw_data[start_f:end_f])
#     sig = samp
#     data = np.array([])
#     sig_index = np.abs(samp)>0.05
#     index = np.where(sig_index==True)
#     if((index[0][0]>10 and index[0][-1]<4990)):
#         index = index[0][0:100]
#         sig[index]=0
#         start_index= index[99]
#         stop_index=start_index+100
#         sig[0:start_index]=0
#         sig[stop_index:]=0
#         data = sig[start_index:stop_index] 
#         data_len=len(data)
#         data=np.append(data,np.zeros(N-data_len))
#         fft_mag = np.abs((np.fft.fft(data)))
#         last_value=np.argmax(fft_mag)
#         bin_fft.append(np.argmax(fft_mag))
#     else:
#         bin_fft.append(last_value)
        
# fft_value = np.array([])
# fft_value=np.append(fft_value,bin_fft)

#fft_value.tofile("fft_val2.txt")

#freq_avg = sum(bin_fft)/len(bin_fft)
#res_freq = (freq_avg)*fs/N+f_c
#print(res_freq/1.0e9)

fft_bin = np.fromfile('/home/bharathvbhatt/Documents/thesis/data/std_auto/fft_val2.txt')
array = np.array(fft_bin)
std_bin = np.array([])
for i in range(0,2000,10):
    new_array=array[i:i+10]
    freq=(new_array)*10e3 + 2.41e9
    freq_ppm = freq *1e6/2.45e9
    mean = sum(freq_ppm)/len(freq_ppm)
    freq_ppm = freq_ppm-mean
    std = np.std(freq_ppm)
    print("%2f" %(std))
    std_bin=np.append(std_bin,std)
    

plt.plot(fc[0:200],std_bin)
#plt.title("std vs. excitation frequency")
plt.xlabel("Excitation frequency in Hz")
plt.ylabel("standard deviation in ppm")














