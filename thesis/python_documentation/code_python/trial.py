#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:13:21 2021

@author: bharathvbhatt
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp,hilbert
from scipy.signal.windows import hann,hamming,bartlett,blackman,blackmanharris

import matplotlib
# matplotlib.use("pgf")
# matplotlib.rcParams.update({
#     "pgf.texsystem": "pdflatex",
#     'font.family': 'serif',
#     'text.usetex': True,
#     'pgf.rcfonts': False,
# })
# fs =5e6
# N=5000
# fsig=1.5e6
# t = np.arange(0,0.001,1/fs)
# f = np.arange(0,fs,fs/N)
# fmcw_array = chirp(t,0,0.001,2e6,method='linear')
# # array_samp = hilbert(fmcw_array)
# sig = np.cos(2*np.pi*fsig*t)
# y = fmcw_array+sig
# down = y-fmcw_array
# fft = np.fft.fft(down)
# fft[0]=0
# plt.plot(f,np.absolute(fft))

#fmcw_array=np.array([])
fs = 50e6 #50e6
fc=2.41e9
ts=1/fs
T = 1e-3
N=5000 #5050
len_zero = int(N-(fs*T))
t = np.arange(0,1e-3,1/fs)
f = np.arange(0,fs,fs/N)
raw_data = np.fromfile("/home/bharathvbhatt/Documents/thesis/data/wired/DFE/raw_data0.iq",np.complex64)
#raw_data = np.fromfile("/home/bharathvbhatt/Documents/thesis/data/std_auto/raw_data.iq",np.complex64)
#raw_data = np.fromfile("plutorx.iq",np.complex64)
raw_data=raw_data/(2**14)

#raw_data_conj = np.conj(raw_data)
#fmcw_array = np.fromfile("fmcwsamples.iq",np.complex64)
#fmcw_array= np.tile(fmcw_array,10)
# down = raw_data_conj*raw_data

start_f =10*5000
end_f = start_f+5000

# fft = np.fft.fftshift(np.fft.fft(down[start_f:end_f]))
# bin_fft = (np.max(fft))
# plt.plot(f,np.abs(fft))


# powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(raw_data, Fs=fs)
# plt.xlabel('Time')
# plt.ylabel('Frequency')
# plt.show()   

samp = np.array([])
samp = np.append(samp,raw_data[start_f:end_f])
# fft = np.fft.fftshift(np.fft.fft(samp))
# plt.plot(f,np.abs(fft))
#samp = np.append(samp,np.zeros(len_zero))
#ifft = np.fft.ifft(samp)
#t_sig = np.arange(N)*1/fs
#plt.plot(t_sig,np.abs(ifft))
# N_win =5000
# window = np.hamming(N_win)
# window.resize(N)
#window = np.roll(window,5000)
# win_ifft = samp*window
f_win = np.arange(0,fs,fs/N)
plt.style.use('seaborn')
# fft_mag = (np.fft.fft(samp))
# plt.plot(f_win,np.abs(fft_mag))

 ###########################Switched###########################################
# t_res = np.arange(5000)*ts
# sig = samp
# sig_index = np.abs(samp)>0.0048#0.01
# sig = sig*sig_index
# ## sig_index =np.abs(sig)>0.0310
# ## sig_index = np.invert(sig_index)
# ## sig=sig*sig_index
# index = np.where(sig_index==True)
# index = index[0][0:120]
# sig_index[index]=False
# sig = sig*sig_index
# index=np.abs(sig)>0
# index=np.where(index==True)
# x_sig = np.array([])
# start = index[0][0]
# end = index[0][-1]
# x_sig = np.append(x_sig,sig[start:end])
# N=4096

# len_zeros = N-len(x_sig)
# x_sig = np.append(x_sig,np.zeros(len_zeros))


# plt.style.use('seaborn')
# fft_mag = np.abs((np.fft.fft(sig)))
# bin_fft = (np.argmax(fft_mag))
# plt.rc('pgf', texsystem='pdflatex')
# plt.plot(t_res,samp,color='Blue',label='Excitation Signal')
# plt.plot(t_res,(sig),color='Orange',label='SAW Response Signal')
# #plt.title('Time domain signal')
# plt.xlabel("Time in s")
# plt.ylabel("Amplitude in V")
# plt.legend()
# plt.show()
# #plt.savefig("img.svg")
# #plt.plot(f_win,fft_mag)
# # plt.set_size_inches(w=4.7747, h=3.5)
# plt.savefig('DFE_response.pgf')

#############################FMCW##############################################
sig = np.array([])
fft_mag  = np.abs((np.fft.fft(samp)))
sig_index = fft_mag >0.54
fft_sig =fft_mag*sig_index
sig_index = fft_sig>0
for i in range(0,10000):
    if(sig_index[i] == True):
      sig = np.append(sig,fft_mag[i])      
fft_value = min(sig)
fft_bin = np.where(fft_sig==fft_value)
plt.plot(f_win,fft_sig)

##########################Plot samples########################################
# fig, axs = plt.subplots(2)

# N=5000
# t_res = np.arange(N)*ts
# sig = samp
# sig_index = np.abs(samp)>0.05#0.01
# data = np.array([])
# index = np.where(sig_index==True)
# if((index[0][0]>10 and index[0][-1]<4990)):
#     index = index[0][0:100]
#     sig[index]=0
#     start_index= index[99]
#     stop_index=start_index+100
#     sig[0:start_index]=0
#     sig[stop_index:]=0
#     data = sig[start_index:stop_index] 
#     data_len=len(data)
#     data = data*bartlett(data_len)
#     data=np.append(data,np.zeros(N-data_len))
# # index=np.abs(sig)>0
# # index=np.where(index==True)
# # x_sig = np.array([])
# # start = index[0][0]
# # end = index[0][-1]
# # x_sig = np.append(x_sig,sig[start:end])
# # N=4096
# # 
# # len_zeros = N-len(x_sig)
# # x_sig = np.append(x_sig,np.zeros(len_zeros))

#     fft_mag = np.abs(((np.fft.fft(data))))
#     fft_dB = 10.0*np.log10(fft_mag)
#     bin_fft = (np.argmax(fft_mag))
#     freq = bin_fft*fs/N+fc
#     print(freq)
#     plt.rc('pgf', texsystem='pdflatex')
#     #plt.plot(t_res,samp,color='Blue',label='Excitation Signal')
#     plt.subplot(1,2,1)
#     plt.plot(t_res,(data),color='Orange',label='SAW Response Signal')
#     plt.title('Time domain signal representation')
#     plt.xlabel("Time in s")
#     plt.ylabel("Amplitude in V")
#     plt.subplot(1,2,2)
#     plt.plot(f,fft_dB)
#     plt.title('Frequency representation')
#     plt.xlabel("Frequency in Hz")
#     plt.ylabel("Magnitude in dB")
#     #plt.text(11e6,4,"Primary resonance")
#     #plt.text(12e6,-2,"Secondary resonance")
#     #plt.text(33e6,-5,"Noise")
#     plt.legend()
#     plt.show()
# else:
#     print("failed")


