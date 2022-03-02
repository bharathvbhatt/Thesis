FMCW Reader
==============
Frequency modulated continuous waveform (FMCW) reader is the first and easiest reader to implement.
The working of the reader is detailed in the thesis. Here the emphasis is on programming the same on Pluto SDR.
Python programming is used for this purpose. Also, GNU radio and MATLAB can also be used.
Inital designs were created on GNU radio for easy analysis of the reader architecture.

The reader in terms of programming is divided into four major parts. The coding is made simple without any object oriented programming.
If there is a need in future the parts described below can as is it be used in the oops file structre.

The first part of the coding is on generation of the waveform.
FMCW is part of many python library, if desired it can also be obtained by the mathematical equation.

The file in src folder *FMCW.py* and *FMCW_analysis.py* will be discussed in this documentation.

.. code-block:: python
 
 import adi #pluto sdr library
 import numpy as np
 import matplotlib.pyplot as plt
 from scipy.signal import chirp,hilbert #chirp gives the FMCW waveform

In the above code section shows the inclusion of the libraries needed.
*adi* is the python library provided by *Aanlog Devices*. To generate FMCW waveform *scipy.signal* library is made use of.

.. code-block:: python

 fs = 50e6 # sampling rate
 N=50000   # Number of samples
 t = np.arange(0,0.001,1/fs) # time variable corresponds to the period i.e from 0-T
 f = np.arange(0,fs,fs/N)  # frequency variable, corresponds to the bandwidth
 fmcw_array = chirp(t,0,0.001,20e6,method='linear') # FMCW waveform
 array_samp = hilbert(fmcw_array)  # To make complex signal

 """ To save the generated waveform into a file used for C programming"""
 fmcw_waveform = np.array([])
 fmcw_waveform=np.append(fmcw_waveform,array_samp) # new variable to hold the complex FMCW waveform
 fmcw_waveform *=2**14 # Pluto SDR doesn't work from -1 to 1 instead from -2**14 to 2**14
 fmcw_waveform=fmcw_waveform.astype(np.complex64)
 fmcw_waveform=np.int_(fmcw_waveform.real) + (np.int_(fmcw_waveform.imag))*1J
 fmcw_waveform.tofile("fmcwsamples.iq")

The above program shows the generation of the FMCW waveform. Initially *fs* sampling frequency and number of samples used is set.
*t* the time range or independent variable is set from 0 - 1ms in steps of *fs*. The frequency variable is also set for plotting. This ranges from 0-20MHz.
Since pluto SDR uses Zero-IF, the waveform has to be converted to complex waveform, this is done using the hilbert transform.

.. code-block:: python

   sample_rate = fs # sampling rate Hz
   center_freq = 2.42e9 # Centre Frequency Hz
   sdr = adi.Pluto("ip:192.168.3.1") # connect to the pluto SDR, here the IP is changed. So is the frequency range.
   sdr.tx_destroy_buffer() #clean or empty the buffer
   sdr.sample_rate = int(sample_rate) 
   sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
   sdr.tx_lo = int(center_freq)
   sdr.tx_hardwaregain_chan0 = 0 # Increase to increase tx power, valid range is -90 to 0 dB
   N = 50000 # number of samples to transmit at once

   samples =  array_samp   #0.5*np.exp(2.0j*np.pi*100e3*t) # Simulate a sinusoid of 100 kHz, so it should show up at 915.1 MHz at the receiver
   samples *= 2**14 # The PlutoSDR expects samples to be between -2^14 and +2^14, not -1 and +1 like some SDRs

   """ To transmit waveform cyclically """
   sdr.tx_cyclic_buffer = True # Enable cyclic buffers
   sdr.tx(samples) # transmit the batch of samples once

Above coding section explains the Tx set up of the SDR. Using the *adi* library connection to pluto SDR is setup through its IP. The returned object *sdr* is used to setup the 
device parameters. The parameters such as sampling frequency (sampling rate), the center frequency i.e Tx_LO, Tx gain is set up. Instead of transmitting the same samples over and over again, Tx cyclic buffer is used.
The samples are loaded once and *tx_cyclic_buffer* is made *true*.

The next step is to capture the signals sent back by the senors. The following code block expalin the reception.

.. code-block:: python
 
 sdr.rx_lo = int(center_freq)
 sdr.rx_rf_bandwidth = int(sample_rate)
 sdr.rx_buffer_size = N
 sdr.gain_control_mode_chan0 = 'slow_attack'  #'manual','fast_attack','slow_attack'
 sdr.rx_hardwaregain_chan0 = 00.0 # dB, increase for a stronger signal, but be careful not to saturate

Like Tx, Rx also initialized using *sdr* object. Parameters such as rx_lo , rx_rf_bandwidth, number of samples to receive, gain_control_mode_chan0 and manual gain value can be set.
The FMCW reader uses either fast_attack or slow_attack AGC control mode so manual gain is set to 0 dB.

.. code-block:: python 

 raw_data = np.array([])
 """ Clear the Rx Buffer """ 
 for i in range (0,10):
    raw = sdr.rx()
 """ Receive the number of samples N times in a loop"""
 for i in range (0,100):   
    raw = sdr.rx()
    #raw = sdr2.rx()
    raw_data = np.append(raw_data,raw)
  """ Store the received sample in a file """   
 raw_data=raw_data.astype(np.complex64)
 raw_data.tofile("raw_data.iq")
 sdr.tx_destroy_buffer() #sto transmitting

The above code snippet gives the Rx block. Initially Rx buffer is cleared in the first loop. Depending on number of samples needed the looping construct can be used to receive
samples corresponding to any number of seconds. These collected samples are appended, later pushed to a file.

This file is processed in *FMCW_analysis.py* to obtain the frequency. The below code snippet shows the python program to calculate the resonant frequency.
In FMCW the frequency corresponding to the minimum magnitude is taken to be the resonant frequency.

.. code-block:: python 
 
 import numpy as np
 import matplotlib.pyplot as plt
   
 fs = 50e6 #50e6
 ts=1/fs
 T = 1e-3
 N=50000 #5050
 fc = 2.41e9

 t = np.arange(50000)*ts

 raw_data = np.fromfile("/home/bharathvbhatt/Documents/thesis/data/wired/raw_data.iq",np.complex64)
 raw_data = raw_data/(2**14)

The above code snippet includes the necessary libraries for the calculations and if necessary plotting (commented code mostly used to make plots for the thesis).
The sampling frequency and time period is taken same as the one used in the tx-rx file.
The received samples stored in a read is stored in raw_data array.

.. code-block:: python

 """ Iterate over the entire received data in steps of N"""
 for i in range(0,5000000,50000):
    start_f = i
    end_f = i+50000
    samp = np.array([])
    """ Each measurement is 50000 samples corrresponding to 1 ramp of the FMCW i.e 1ms"""
    samp = np.append(samp,raw_data[start_f:end_f])

    sig = np.array([])
    fft_mag  = np.abs((np.fft.fft(samp))) #compute the magnitude response of the fft
    sig_index = fft_mag >0.54  # used as threshold to remove the noise floor
    fft_sig =fft_mag*sig_index 
    sig_index = fft_sig>0
    for i in range(0,20000):  # look inside the bandwidth of 20 MHz
          if(sig_index[i] == True):
              sig = np.append(sig,fft_mag[i])      
    fft_value = min(sig)
    fft_bin = np.where(fft_sig==fft_value)
    val.append(fft_bin[0])   # append min value into a list
         #plt.plot(f_win,fft_sig)
 fmcw_bin = np.array([])
 fmcw_bin= np.append(fmcw_bin,val)
 fmcw_bin.tofile("fmcw_bin.txt") # store the raw value of the resonant frequency in a file, which can be used to compute STD.
 avg = sum(val)/len(val) # Average value of the frequency
 freq = (avg*fs/N)+fc    # Frequency in GHz
 print(freq/1.0e9) # print resonant frequency only the float point without GHz (which is assumed i,e normalized to GHz)

The data is analysed by iterating over received data in setps of the number of samples collected (N). The fft of the N samples is performed. Then the required bandwidth
need for analysis is taken by setting threshold. Then the frequency corresponding to the minimum is computed and appended to the list. Once all samples are analysed, the
average of the frequency bin is calculated. This is stored in a file for other analysis such as to compute the Standard deviation. The average fft bin value is converted
to the frequency in GHz and then printed by normalising to GHz.

File based programming is used so that data can be analysed on its own at a later stage using automatic script. Also, these files can be labelled and stored to compare measurements.
