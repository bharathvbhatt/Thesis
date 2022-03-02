#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:16:04 2021

@author: bharathvbhatt
"""
import numpy as np
import random
import socket,os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import mlab as mlab
from itertools import count
import threading
import numpy as np
import adi
import scipy as sy
from scipy.signal import chirp,hilbert
import time
from collections import deque 

# fs = 50e6
# T = 1e-6
# fc =800e3
# ts = 1/fs
# N=5000 #5000
# len_zeropadd = int(N - (fs*T)-5000)
# f = np.arange(-fs/2,fs/2,fs/N)
# t = np.arange(0,2e-6,ts)
# sig = np.array([])
# sig = np.append(sig,np.cos(2*np.pi*fc*t))
 

# array_samp = np.array([])
# array_samp = np.append(array_samp,hilbert(sig))
# array_samp =array_samp.astype(np.complex64)
# array_samp = np.append(array_samp,np.zeros(4900))#4900


# sample_rate = fs # sampling rate Hz
# center_freq = 2.418e9 # Centre Frequency Hz
# sdr = adi.Pluto(uri="ip:192.168.3.1")

# sdr.tx_destroy_buffer() #clean or empty the buffer
# sdr.sample_rate = int(sample_rate) 

# sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
# sdr.tx_lo = int(center_freq)
# sdr.tx_hardwaregain_chan0 = -00 # Increase to increase tx power, valid range is -90 to 0 dB
# samples =  array_samp  #0.5*np.exp(2.0j*np.pi*100e3*t) # Simulate a sinusoid of 100 kHz, so it should show up at 915.1 MHz at the receiver
# samples *= 2**14 # The PlutoSDR expects samples to be between -2^14 and +2^14, not -1 and +1 like some SDRs

# sdr.tx_cyclic_buffer = True # Enable cyclic buffers
# sdr.tx(samples) # transmit the batch of samples once 


buf =np.array([])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('0.0.0.0', 9999))  
sock.listen(1)
connection,address = sock.accept()  
cyc_buff =[] #np.array([])*100  
size=0
avg=0

index =count()
x =deque(np.zeros(100))
y =deque(np.zeros(100))
def animate(i):
    global buf
    global avg
    buf =connection.recv(4).decode('utf-8')
    print(int(buf[0:3]))
    #cyclic_buffer(int(buf[0:3]))
    x.popleft()
    x.append(next(index))
    y.popleft()
    y.append(int(buf))
    plt.cla()
    plt.plot(x,y)
    
    
ani = FuncAnimation(plt.gcf(),animate,interval=1)  

# def cyclic_buffer(val):
#     global cyc_buff
#     global size
#     global avg
#     if(size<100):
#         cyc_buff.insert(size, val)
#         size+=1
#     else:
#         avg = sum(cyc_buff)/len(cyc_buff)
#         print('Avg is :'+ str(avg))
#         size=0
#         cyc_buff.clear()

# i=0
# while i<10:  
#     buf =connection.recv(4).decode('utf-8')
#     print(int(buf))
#     #print(int(buf[0:3]))
#     #cyclic_buffer(int(buf[0:3]))
#     i+=1
#     # connection.send(buf)    		
#     #connection.close()
  
    
