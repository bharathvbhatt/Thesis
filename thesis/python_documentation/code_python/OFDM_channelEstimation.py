#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:54:10 2021

@author: bharathvbhatt
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert,chirp,iirnotch,freqz,filtfilt,periodogram
import scipy
K = 64 # number of OFDM subcarriers
CP = K//4  # length of the cyclic prefix: 25% of the block

P = 8 # number of pilot carriers per OFDM block
pilotValue = 3+3j # The known value each pilot transmits

allCarriers = np.arange(K)  # indices of all subcarriers ([0, 1, ... K-1])

pilotCarriers = allCarriers[::K//P] # Pilots is every (K/P)th carrier.

# For convenience of channel estimation, let's make the last carriers also be a pilot
pilotCarriers = np.hstack([pilotCarriers, np.array([allCarriers[-1]])])
P = P+1

# data carriers are all remaining carriers
dataCarriers = np.delete(allCarriers, pilotCarriers)

#print ("allCarriers:   %s" % allCarriers)
#print ("pilotCarriers: %s" % pilotCarriers)
#print ("dataCarriers:  %s" % dataCarriers)
#plt.plot(pilotCarriers, np.zeros_like(pilotCarriers), 'bo', label='pilot')
#plt.plot(dataCarriers, np.zeros_like(dataCarriers), 'ro', label='data')


mu = 4 # bits per symbol (i.e. 16QAM)
payloadBits_per_OFDM = len(dataCarriers)*mu  # number of payload bits per OFDM symbol

mapping_table = {
    (0,0,0,0) : -3-3j,
    (0,0,0,1) : -3-1j,
    (0,0,1,0) : -3+3j,
    (0,0,1,1) : -3+1j,
    (0,1,0,0) : -1-3j,
    (0,1,0,1) : -1-1j,
    (0,1,1,0) : -1+3j,
    (0,1,1,1) : -1+1j,
    (1,0,0,0) :  3-3j,
    (1,0,0,1) :  3-1j,
    (1,0,1,0) :  3+3j,
    (1,0,1,1) :  3+1j,
    (1,1,0,0) :  1-3j,
    (1,1,0,1) :  1-1j,
    (1,1,1,0) :  1+3j,
    (1,1,1,1) :  1+1j
}
# for b3 in [0, 1]:
#     for b2 in [0, 1]:
#         for b1 in [0, 1]:
#             for b0 in [0, 1]:
#                 B = (b3, b2, b1, b0)
#                 Q = mapping_table[B]
#                 #plt.plot(Q.real, Q.imag, 'bo')
#                 #plt.text(Q.real, Q.imag+0.2, "".join(str(x) for x in B), ha='center')
                
                
demapping_table = {v : k for k, v in mapping_table.items()}                
#########################  channel Response-- SAW simulation #######################################                
# fs = 500                
# f0 = 60  # Frequency to be removed from signal (Hz)
# Q = 30.0  # Quality factor
# # Design notch filter
# b, a = iirnotch(f0, Q, fs)
# freq, channelResponse = freqz(b, a,fs=fs,worN=64)
#plt.plot(freq,np.abs(h))      
          
channelResponse = np.array([1, 1, 0 ])  # the impulse response of the wireless channel
H_exact = np.fft.fft(channelResponse, K)
# H_exact = channelResponse
####################################################################################################

SNRdb = 25  # signal to noise-ratio in dB at the receiver 
#plt.plot(allCarriers, abs(H_exact))  
bits = np.random.binomial(n=1, p=0.5, size=(payloadBits_per_OFDM, ))
              
def SP(bits):
    return bits.reshape((len(dataCarriers), mu))
bits_SP = SP(bits)


def Mapping(bits):
    return np.array([mapping_table[tuple(b)] for b in bits])
QAM = Mapping(bits_SP)


def OFDM_symbol(QAM_payload):
    symbol = np.zeros(K, dtype=complex) # the overall K subcarriers
    symbol[pilotCarriers] = pilotValue  # allocate the pilot subcarriers 
    symbol[dataCarriers] = QAM_payload  # allocate the pilot subcarriers
    return symbol
OFDM_data = OFDM_symbol(QAM)     


def IDFT(OFDM_data):
    return np.fft.ifft(OFDM_data)
OFDM_time = IDFT(OFDM_data)

def addCP(OFDM_time):
    cp = OFDM_time[-CP:]               # take the last CP samples ...
    return np.hstack([cp, OFDM_time])  # ... and add them to the beginning
OFDM_withCP = addCP(OFDM_time)


def channel(signal):
    convolved = np.convolve(signal, channelResponse)
    signal_power = np.mean(abs(convolved**2))
    sigma2 = signal_power * 10**(-SNRdb/10)  # calculate noise power based on signal power and SNR
    
    print ("RX Signal power: %.4f. Noise power: %.4f" % (signal_power, sigma2))
    
    # Generate complex noise with given variance
    noise = np.sqrt(sigma2/2) * (np.random.randn(*convolved.shape)+1j*np.random.randn(*convolved.shape))
    return convolved + noise
OFDM_TX = OFDM_withCP
OFDM_RX = channel(OFDM_TX)
# plt.figure(figsize=(8,2))
# plt.plot(abs(OFDM_TX), label='TX signal')
# plt.plot(abs(OFDM_RX), label='RX signal')
# plt.legend(fontsize=10)
# plt.xlabel('Time'); plt.ylabel('$|x(t)|$');
# plt.grid(True);


def removeCP(signal):
    return signal[CP:(CP+K)]
OFDM_RX_noCP = removeCP(OFDM_RX)
         
def DFT(OFDM_RX):
    return np.fft.fft(OFDM_RX)
OFDM_demod = DFT(OFDM_RX_noCP)


def channelEstimate(OFDM_demod):
    pilots = OFDM_demod[pilotCarriers]  # extract the pilot values from the RX signal
    Hest_at_pilots = pilots / pilotValue # divide by the transmitted pilot values
    
    # Perform interpolation between the pilot carriers to get an estimate
    # of the channel in the data carriers. Here, we interpolate absolute value and phase 
    # separately
    Hest_abs = scipy.interpolate.interp1d(pilotCarriers, abs(Hest_at_pilots), kind='linear')(allCarriers)
    Hest_phase = scipy.interpolate.interp1d(pilotCarriers, np.angle(Hest_at_pilots), kind='linear')(allCarriers)
    Hest = Hest_abs * np.exp(1j*Hest_phase)
    
    plt.plot(allCarriers, abs(H_exact), label='Correct Channel')
    plt.stem(pilotCarriers, abs(Hest_at_pilots), label='Pilot estimates')
    plt.plot(allCarriers, abs(Hest), label='Estimated channel via interpolation')
    plt.grid(True); plt.xlabel('Carrier index'); plt.ylabel('$|H(f)|$'); plt.legend(fontsize=10)
    # plt.ylim(0,2)
    
    return Hest
Hest = channelEstimate(OFDM_demod)