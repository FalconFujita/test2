import numpy as np

def sig(amp,freq):
    time_start = 0
    time_end = 1
    sampling = 0.001
    
    time = np.arange(time_start,time_end,sampling)
    x = amp * np.sin(np.pi * freq * time)
    y = amp * np.cos(np.pi * freq * time)
    sig = x + y * 1j
    sig_fft = np.fft.fft(sig)
    sig_fft_max = sig_fft.max()
    print(sig_fft_max)

if __name__ == '__main__':
    sig(10,1000)
