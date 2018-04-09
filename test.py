import numpy as np

time_start = 0
time_end = 1
sampling = 0.001
freq = 1000

time = np.arange(time_start,time_end,sampling)
x = np.sin(np.pi * freq * time)
y = np.cos(np.pi * freq * time)
sig = x + y * 1j
sig_fft = np.fft.fft(sig)

