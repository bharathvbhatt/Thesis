FSCW Reader
=============
 
Frequency step continuous waveform is the variation of the FMCW reader. Here again the procedure is same as FMCW. Instead of generating a linear ramp, steped ramp is 
considered. This waveform generation is similar to frequency shift keying (FSK). Source code is in *FSCW.py*

.. code-block:: python
 
 """ Import required library """
 import numpy as np
 import math
 import scipy
 import matplotlib.pyplot as plt
 from scipy.signal import chirp,hilbert 
 fs = 5e6
 fc=100
 N=5000
 t = np.arange(0,1,1/fs)
 data = np.arange(0,N,1) # generate the data
 symb = np.array(np.repeat(data,fs/N)) # repeate the data for the each frequency step time
 #symb.resize(int(fs))
 sig = np.cos(2*np.pi*t*(fc+symb*400)) # multiply the frequency by the symbol
 #f = np.fft.fftfreq(len(sig))
 f= np.arange(0,fs,1)
 fft_sig = np.fft.fft(sig)
 plt.plot(f,np.abs(fft_sig))
 plt.plot(t,sig)

The above method leads to serious discntinuity in the phase of the signal when frequency is stepped from *f1* to *f2*. To have continuous phase, continuous phase modulation
of digital communication can be used. This is implemented using equations from Digital Communication lecture by Prof. Bauch. The source code is inside *CPM.py*

.. code-block:: python

 """ Import necessary library"""
 import numpy as np
 import matplotlib.pyplot as plt
 from scipy.signal import lfilter

 fs = 100e3 # sampling frequency
 tb= 1e-3 # bit time
 t = np.arange(0,8*tb,1/fs)
 b = 2*np.random.randint(2,size=8)-1 # random bits
 fc=5e3 # carrier frequency
 h=1 # modulation index

 b = np.tile(b, (100,1)).flatten('F') 
 b_integrated = lfilter([1.0],[1.0,-1.0],b)/fs #Integrate b using filter. The integration of the frequency pulse
 theta= np.pi*h/tb*b_integrated #overall integrated pahse

 s = np.cos(2*np.pi*fc*t + theta) # CPFSK signal
 f = np.arange(-fs/2,fs/2,fs/800)
 plt.plot(f,b_integrated)


