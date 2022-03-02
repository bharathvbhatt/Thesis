#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:39:56 2021

@author: bharathvbhatt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp,hilbert
import tikzplotlib

fs = 50e6 #50e6
ts=1/fs
T = 1e-3
N=50000 #5050
fc = 2.41e9
t = np.arange(50000)*ts

raw_data = np.fromfile("/home/bharathvbhatt/Documents/thesis/data/wired/raw_data.iq",np.complex64)
raw_data = raw_data/(2**14)


val = list()


for i in range(0,5000000,50000):
    start_f = i
    end_f = i+50000
    samp = np.array([])
    samp = np.append(samp,raw_data[start_f:end_f])

    sig = np.array([])
    fft_mag  = np.abs((np.fft.fft(samp)))
    sig_index = fft_mag >0.54
    fft_sig =fft_mag*sig_index
    sig_index = fft_sig>0
    for i in range(0,20000):
          if(sig_index[i] == True):
              sig = np.append(sig,fft_mag[i])      
    fft_value = min(sig)
    fft_bin = np.where(fft_sig==fft_value)
    val.append(fft_bin[0])
         #plt.plot(f_win,fft_sig)
fmcw_bin = np.array([])
fmcw_bin= np.append(fmcw_bin,val)
fmcw_bin.tofile("fmcw_bin.txt")
avg = sum(val)/len(val)
freq = (avg*fs/N)+fc
print(freq/1.0e9)


# start_f = 0
# end_f = 0


# raw_data_8dbi = np.fromfile("/home/bharathvbhatt/Documents/thesis/data/wireless/antenna/raw_data_8dBi.iq",np.complex64)
# raw_data_2dbi = np.fromfile("/home/bharathvbhatt/Documents/thesis/data/wireless/antenna/raw_data_2dBi.iq",np.complex64)
# raw_data_2dbi=raw_data_2dbi/(2**14)
# raw_data_8dbi=raw_data_8dbi/(2**14)
# raw_data_0cm = np.fromfile("/home/bharathvbhatt/Documents/thesis/data/wireless/FMCW/raw_data_0cm.iq",np.complex64)
# raw_data_0cm=raw_data_0cm/(2**14)
# raw_data_5cm = np.fromfile("/home/bharathvbhatt/Documents/thesis/data/wireless/FMCW/raw_data_5cm.iq",np.complex64)
# raw_data_5cm=raw_data_5cm/(2**14)
# raw_data_12cm = np.fromfile("/home/bharathvbhatt/Documents/thesis/data/wireless/FMCW/raw_data_12cm.iq",np.complex64)
# raw_data_12cm=raw_data_12cm/(2**14)
# raw_data_20cm = np.fromfile("/home/bharathvbhatt/Documents/thesis/data/wireless/FMCW/raw_data_20cm.iq",np.complex64)
# raw_data_20cm=raw_data_20cm/(2**14)


# f = np.arange(0,fs,fs/N)
# rx_samples = raw_data[0:50000]
# rx_samples1 = raw_data_0cm[0:50000]
# rx_samples2 = raw_data_5cm[0:50000]
# rx_samples3 = raw_data_12cm[0:50000]
# rx_samples4 = raw_data_20cm[0:50000]

# rx_samples_2dbi = raw_data_2dbi[1000000:1050000]
# rx_samples_8dbi = raw_data_8dbi[1000000:1050000]


# fft1 = np.fft.fft(rx_samples1)
# fft_mag1 = np.abs(fft1)
# fft_db1 = 10.0*np.log10(fft_mag1)
# fft_mag1[0]=0

# fft2 = np.fft.fft(rx_samples2)
# fft_mag2 = np.abs(fft2)
# fft_db2 = 10.0*np.log10(fft_mag2)
# fft_mag2[0]=0

# fft3 = np.fft.fft(rx_samples3)
# fft_mag3 = np.abs(fft3)
# fft_db3 = 10.0*np.log10(fft_mag3)
# fft_mag3[0]=0

# fft4 = np.fft.fft(rx_samples4)
# fft_mag4 = np.abs(fft4)
# fft_db4 = 10.0*np.log10(fft_mag4)
# fft_mag4[0]=0


# fft_2dbi = np.fft.fft(rx_samples_2dbi)
# fft_mag_2dbi = np.abs(fft_2dbi)
# fft_db_2dbi = 10.0*np.log10(fft_mag_2dbi)
# fft_mag_2dbi[0]=0

# fft_8dbi = np.fft.fft(rx_samples_8dbi)
# fft_mag_8dbi = np.abs(fft_8dbi)
# fft_db_8dbi = 10.0*np.log10(fft_mag_8dbi)
# fft_mag_8dbi[0]=0


# plt.plot(f,fft_mag1,'r',label="5cm")
# plt.plot(f,fft_mag2,'b',label="12cm")
# plt.plot(f,fft_mag3,'g',label="20cm")
# plt.plot(f[0:20000],fft_db1[0:20000],label="0cm")
# plt.legend()
# plt.show()

#plt.plot(t,rx_samples1)

#axs[1].plot(f,fft_mag)
# plt.rcParams["figure.figsize"] = (6,6)
# plt.subplot(2,2,1)
# plt.plot(f[0:20000],fft_db1[0:20000])
# plt.xlabel("Frequency in Hz")
# plt.ylabel("Magnitude in dB")
# #plt.title("FMCW Frequency resopnse wired")
# plt.text(1e6,5,"0cm")

# plt.subplot(2,2,2)
# plt.plot(f[0:20000],fft_db2[0:20000])
# plt.xlabel("Frequency in Hz")
# plt.ylabel("Magnitude in dB")
# plt.text(1e6,5,"5cm")

# plt.subplot(2,2,3)
# plt.plot(f[0:20000],fft_db3[0:20000])
# plt.xlabel("Frequency in Hz")
# plt.ylabel("Magnitude in dB")
# plt.text(1e6,5,"12cm")

# plt.subplot(2,2,4)
# plt.plot(f[0:20000],fft_db4[0:20000])
# plt.text(1e6,5,"20cm")
# plt.xlabel("Frequency in Hz")
# plt.ylabel("Magnitude in dB")


# plt.subplot(2,1,1)
# plt.plot(f[0:20000],fft_db_2dbi[0:20000])
# plt.xlabel("Frequency in Hz")
# plt.ylabel("Magnitude in dB")
# #plt.title("2dBi antenna response")

# plt.subplot(2,1,2)
# plt.plot(f[0:20000],fft_db_8dbi[0:20000])
# plt.xlabel("Frequency in Hz")
# plt.ylabel("Magnitude in dB")
# #plt.title("8dBi antenna response")



# # #plt.title("FMCW Reader Response")


# fft = np.fft.fft(rx_samples)
# fft_mag = np.abs(fft)
# fft_db = 10.0*np.log10(fft_mag)
# fft_db[0]=0
# plt.plot(f[0:20000],fft_mag[0:20000])
# plt.xlabel("Frequency in Hz")
# plt.ylabel("Magnitude in dB")
# plt.text(10000000,7, "Secondary resonance")
# plt.text(8000000,5, "Primary resonance")
#tikzplotlib.save("FMCW_freqresp.tex")
#plt.savefig("freq_FMCW.pgf")