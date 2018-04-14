# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

time_start = 0
time_end = 1
sampling = 0.001
time = np.arange(time_start,time_end,sampling)

def make_signal(amp,freq):        
    x = amp * np.sin(np.pi * freq * time)
    y = amp * np.cos(np.pi * freq * time)
    sig = x + y * 1j
    return sig

def make_noise(mu,sigma):        
    x = np.random.normal(mu,sigma,size=len(time))
    y = np.random.normal(mu,sigma,size=len(time))
    sig = x + y * 1j
    return sig

if __name__ == '__main__':
    sig = make_signal(10,1000)
    noise = make_noise(0,10)
    sig = sig + noise
    sig = np.fft.fft(sig)
    plt.plot(time,abs(sig),'b-')
    plt.show()
