# Plot PSD Function
from pylab import *
import numpy as np

def plot_psd(samples, freq_center, Fs, N):

    # Compute components of PSD graph
    x = samples[0:N]
    x = x * np.hamming(len(x)) # apply hamming window for FFT since last and first elements of array ~ equal since fft assumes periodicity
    psd = (np.abs(np.fft.fft(x))**2) / (N*Fs) # take fft, magnitude of fft and square to get power, divide by Fs * N to normalize
    psd_log = 10 * np.log10(psd) # convert to log scale
    psd_shifted = np.fft.fftshift(psd_log) # shift so 0 Hz is center freq 
    freq = np.arange(Fs/-2.0, Fs/2.0, Fs/N) # start, stop, step centered around 0 Hz
    freq += freq_center
    freq /= 1000000 # plot in MHz

    # Use matplotlib to generate plot
    plt.plot(freq, psd_shifted)
    plt.title('Power Spectral Density')
    plt.xlabel('f (MHz)')
    plt.ylabel('Power (dB)')
    plt.show()