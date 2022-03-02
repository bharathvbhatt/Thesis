#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:24:51 2021

@author: bharathvbhatt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp,hilbert
import scipy as sy
fmcw_array=np.array([])
fc = 2.41e9
fs = 50e6 #50e6
ts=1/fs
T = 1e-3
N=5000 #5050
len_zero = int(N-(fs*T))
t = np.arange(0,1e-3,1/fs)
f = np.arange(-fs/2,fs/2,fs/N)
raw_data = np.fromfile("/home/bharathvbhatt/Documents/thesis/data/wireless/good_data.iq",np.complex64)
#raw_data = np.fromfile("plutorx.iq",np.complex64)
raw_data=raw_data/(2**14)

#############fft averaging#####################################################
# bin_fft=list()
# start_f =0
# end_f = 0

# for i in range(0,5000000,5000): #5000000
#     start_f = i
#     end_f = i+5000
#     samp = np.array([])
#     samp = np.append(samp,raw_data[start_f:end_f])
#     sig = samp
#     sig_index = np.abs(samp)>0.01
#     sig = sig*sig_index
#     index = np.where(sig_index==True)
#     index = index[0][0:115]
#     sig_index[index]=False
#     sig = sig*sig_index
#     fft_mag = np.abs((np.fft.fft(sig)))
#     bin_fft.append(np.argmax(fft_mag))
# fft_value = np.array([])
# fft_value=np.append(fft_value,bin_fft)
# #fft_value.astype(np.int64)
# fft_value.tofile("fft_val.txt")

# freq_avg = sum(bin_fft)/len(bin_fft)
# res_freq = (freq_avg)*fs/N+fc
# print(res_freq/1.0e9)

############samples averaging##################################################
# bin_fft=list()
# start_f =0
# end_f = 0
# k=0
# samp_val = np.array([0]*100)
# for i in range(0,50000,5000):
#     start_f = i
#     end_f = i+5000
#     samp = np.array([])
#     samp = np.append(samp,raw_data[start_f:end_f])
#     # sig = samp
#     # sig_index = np.abs(samp)>0.01
#     # sig = sig*sig_index
#     # index = np.where(sig_index==True)
#     # index = index[0][0:115]
#     # sig_index[index]=False
#     # sig = sig*sig_index
#     # x_index = np.where(sig_index==True)
#     # start = x_index[0][0]
#     # end = x_index[0][-1]
#     # x_sig = np.array([])
#     # x_sig = sig[start:end]
#     sig = samp
#     x_sig = np.array([])
#     sig_index = np.abs(samp)>0.05
#     index = np.where(sig_index==True)
#     if((index[0][0]>10 and index[0][-1]<4990)):
#         index = index[0][0:100]
#         sig[index]=0
#         start_index= index[99]
#         stop_index=start_index+100
#         sig[0:start_index]=0
#         sig[stop_index:]=0
#         x_sig = sig[start_index:stop_index] 
#         len_xsig = len(x_sig)
#     if (len_xsig<=100):
#        # x_sig = np.append(x_sig,np.zeros(100-len_xsig))
#         #samp_val = np.add(samp_val,x_sig)
#         if(np.all((samp_val==0))):
#             samp_val = np.add(samp_val,x_sig)
#         else:
#             corr = sy.signal.signaltools.correlate(samp_val,x_sig)
#             dt = np.arange(1-5000, 5000)
#             t_shift = dt[corr.argmax()]
#             x_sig =np.roll(x_sig,t_shift)
#             samp_val = np.add(samp_val,x_sig)
#     else :
#         k+=1
# samp_val = samp_val/(50000-k)

# t_sig = np.arange(100)*ts
# #plt.plot(t_sig,samp_val[0:100])
# # fft = (np.fft.fft(samp_val[0:100]))
# # fft = np.append(fft,np.zeros(100))
# # samp_val = np.fft.ifft(fft)
# #plt.plot(t_sig,samp_val)
# my_sig = np.array([])
# my_sig = np.append(my_sig,samp_val)
# my_sig = np.append(my_sig,np.zeros(4900))
# fft = (np.fft.fft(my_sig))
# #avg_power= np.mean(np.abs(samp_val)**2)

# #f_sig =np.arange(0,fs,fs/100)
# #plt.plot(f_sig,np.abs(fft))
# freq = np.argmax(np.abs(fft))
# res_freq = freq*fs/5000 +fc
# print(res_freq/1.0e9)
# print(k)
#print(avg_power)
###############################################################################
# bin_fft=list()
# start_f =0
# end_f = 0
# fft_val = list()
# for i in range(0,500000,5000):
#     start_f = i
#     end_f = i+5000
#     samp = np.array([])
#     samp = np.append(samp,raw_data[start_f:end_f])
#     sig = samp
#     sig_index = np.abs(samp)>0.4
#     sig = sig*sig_index
#     #index = np.where(sig_index==True)
#     #index = index[0][0:100]
#     #sig_index[index]=False
#     #sig = sig*sig_index
#     fft_mag = np.abs((np.fft.fft(sig)))
#     bin_fft.append(np.argmax(fft_mag))
# freq_avg = sum(bin_fft)/len(bin_fft)
# res_freq = freq_avg*fs/N+fc
# print(res_freq/1.0e9)
 
###############################################################################
bin_fft=list()
start_f =0
end_f = 0


for i in range(0,500000,5000): #5000000
    start_f = i
    end_f = i+5000
    samp = np.array([])
    samp = np.append(samp,raw_data[start_f:end_f])
    sig = samp
    data = np.array([])
    sig_index = np.abs(samp)>0.05
    index = np.where(sig_index==True)
    if((index[0][0]>10 and index[0][-1]<4990)):
        index = index[0][0:100]
        sig[index]=0
        start_index= index[99]
        stop_index=start_index+100
        sig[0:start_index]=0
        sig[stop_index:]=0
        data = sig[start_index:stop_index] 
        data_len=len(data)
        data=np.append(data,np.zeros(N-data_len))
        fft_mag = np.abs((np.fft.fft(data)))
        bin_fft.append(np.argmax(fft_mag))
fft_value = np.array([])
fft_value=np.append(fft_value,bin_fft)

fft_value.tofile("fft_val2.txt")

freq_avg = sum(bin_fft)/len(bin_fft)
res_freq = (freq_avg)*fs/N+fc
print(res_freq/1.0e9)










