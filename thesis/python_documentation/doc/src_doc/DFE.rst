DFE Reader
=============

Digital frequency estimation is the popular read architecture. Here a single frequency sinusoidal signal is radiated towards the sensor. After transmission the receiver
looks for the response (exponentially decaying sinusoid). The frequency of this gives the resonant frequency. In this documentation both *DFE.py* and *DFE_analysis.py* is discussed.

The SDR configuration is similar to the FMCW reader. The only difference is the waveform generation. Also, in the receive section we use manual RX_gain instead of fast_attack or slow_attack.

.. code-block:: python

 """ Import necessary libraries """
 import numpy as np
 import adi
 import matplotlib.pyplot as plt
 import scipy as sy
 from scipy.signal import chirp,hilbert
 import time

 fs = 50e6 #40.96e6 #sampling frequency
 fc =930e3     # sinusoidal excitation frequency
 ts = 1/fs
 N= 5000#4096  # number of samples
 
 f = np.arange(-fs/2,fs/2,fs/N) # frequency variable for plotting
 t = np.arange(0,2e-6,ts) # time for the sinusoidal signal sampling
 sig = np.array([])
 sig = np.append(sig,np.cos(2*np.pi*fc*t)) # cosine signal of fc Hz
 

 array_samp = np.array([])
 array_samp = np.append(array_samp,hilbert(sig)) # convert to complex signal
 array_samp =array_samp.astype(np.complex64)
 array_samp = np.append(array_samp,np.zeros(4900))#4014 # Append zeros to get switching effect.

The code snippet above gives the code to generate a sinusoidal signal. This signal is of single frequency *fc* which is close to the resonant frequency of the 
sensor. The signal duration *t* is equal to the time constant needed to charge the sensor. Here it is taken to be 2 us. Later the samples are appended zeros. This creates
the switching effect. Also it is used to interpolate the frequency bins. Here the number of samples and zeros appended makes each transmission at 100 us.

Similar to the FMCW reader, the sdr is configured for Tx and Rx. The collected rx samples are stored in a file.

There are three methods used for analysis of DFE data.

* FFT averaging by setting threshold
* Time averaging and then computing FFT
* Take number of samples corresponding to the response


The analysis of the DFE is given in the code below.

.. code-block:: python

 bin_fft=list() # to store the fft bin of each measurement
 start_f =0
 end_f = 0
 """ Iterating over all received data in N steps"""
 for i in range(0,5000000,5000): #5000000
     start_f = i
     end_f = i+5000
     samp = np.array([])
     samp = np.append(samp,raw_data[start_f:end_f])
     sig = samp

     sig_index = np.abs(samp)>0.01 # check for the noise floor and set the threshold, removes the noise floor
     sig = sig*sig_index
     index = np.where(sig_index==True)
     index = index[0][0:115] # index of the transmitted signal that has to be removed + some ringing
     sig_index[index]=False # remove it by making it false
     sig = sig*sig_index
     fft_mag = np.abs((np.fft.fft(sig))) # compute the fft of the remaining signal which is just the response
     bin_fft.append(np.argmax(fft_mag)) # compute the max fft and store the corresponding bin 
 fft_value = np.array([])
 fft_value=np.append(fft_value,bin_fft)
 #fft_value.astype(np.int64)
 fft_value.tofile("fft_val.txt") # store raw fft values in a file to calulate things further
 freq_avg = sum(bin_fft)/len(bin_fft) # compute the average
 res_freq = (freq_avg)*fs/N+fc  # compute the frequeny using fft bin
 print(res_freq/1.0e9) # print the value normailzed to GHz.

The above code is based on threshold. Initially noise floor is made 0 by setting up a threshold. Anything above the threshold is Tx signal+Response signal.
Then the first 115 non zero samples is made zero i.e to remove the Tx signal. Now the response signal is left. The fft of the signal is taken. The bin corresponding to the
max magnitude is saved to a list. This then put in a file. The fft bin values are averaged and converted to GHz. While priting normailzed value is given.

The second method uses the time averaging. The response signal is added in time domain by remoing the Tx signal once all measurements are averaged the signal fft is computed.
Since there will be time lag and phase lag of the response signal between each measurement, correlation funtion is used to lead or lag the signal so that they constructively
interfere. The code is given below.

.. code-block:: python

 bin_fft=list()
 start_f =0
 end_f = 0
 k=0
 samp_val = np.array([0]*100)
 for i in range(0,50000,5000):
     start_f = i
     end_f = i+5000
     samp = np.array([])
     samp = np.append(samp,raw_data[start_f:end_f])
     sig = samp
     x_sig = np.array([])
     sig_index = np.abs(samp)>0.05   # threshold just to avoid noise floor
     index = np.where(sig_index==True)
     if((index[0][0]>10 and index[0][-1]<4990)): # if signal captured are close to start or end dont consider it
         index = index[0][0:100] 
         sig[index]=0           # removing the Tx signal
         start_index= index[99]
         stop_index=start_index+100
         sig[0:start_index]=0
         sig[stop_index:]=0
         x_sig = sig[start_index:stop_index]  # only the response signal
         len_xsig = len(x_sig)
     if (len_xsig<=100):        # greater than 100 samples means some interference is also considered as a signal
         if(np.all((samp_val==0))):
             samp_val = np.add(samp_val,x_sig) # adding the first measurement to the null buffer
         else:
             corr = sy.signal.signaltools.correlate(samp_val,x_sig) # find correlation of the current measurement with previous exiting signal
             dt = np.arange(1-5000, 5000)
             t_shift = dt[corr.argmax()]
             x_sig =np.roll(x_sig,t_shift) # shift the signal by correlation amount
             samp_val = np.add(samp_val,x_sig) # add correlated signals
     else :
         k+=1
 samp_val = samp_val/(50000-k)
 t_sig = np.arange(100)*ts
 my_sig = np.array([])
 my_sig = np.append(my_sig,samp_val)
 my_sig = np.append(my_sig,np.zeros(4900))
 fft = (np.fft.fft(my_sig))
 freq = np.argmax(np.abs(fft))
 res_freq = freq*fs/5000 +fc
 print(res_freq/1.0e9)

In the last method first few samples that corresponds to the Tx signal is made zero and the next 100 samples are considered as the response and fft is calculated for
each measurement and frequency is calculated by averaging the fft bins.

.. code-block:: python

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
