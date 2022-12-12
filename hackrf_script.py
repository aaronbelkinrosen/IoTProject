# HackRF RX and binary data signal processing of SDR IQ data

from libhackrf import * # import libhackrf python wrapper
from pylab import *
import os
import numpy as np

# Import user defined functions
from plot_psd import *
from plot_raw_iq import *


# Use hackrf_transfer terminal command with options to generate binary file
cmd = 'hackrf_transfer '
rx_filename = '-r rx_data.iq '
freq_cmd = '-f 1575420000 '
sample_rate = '-s 20000000 '
num_samples = '-n 100000 ' 
crystal_err = '-C 1'
#os.system(cmd + rx_filename + freq_cmd + sample_rate + num_samples + crystal_err)


# Open binary file and convert binary data to IQ 
samples = np.fromfile('rx_data_copy.iq', np.int8).astype(np.float32).view(np.complex64) # cast int8 IQ data to float32,float32 (I,Q)
samples /= 128 # convert complex data to -1 to 1 to avoid Rx saturation (int8 from -128 to 127 so divide by 128)
print(samples)

# Calculate avg power
mean = np.mean(np.abs(samples)**2) # If roughly zero mean (can use var to calculate avg power since same eqn as var!)
avg_pwr = np.var(samples)
#print(avg_pwr)

# Calculate PSD of Rx Signal 

center_freq = 1575420000 # SDR tuned for L1 GPS freq
F_sampling = 20000000 # 20 MHz sampling rate
N =  8192 # size of commplex array to perform fft on
num_plot_samples = 5000

#plot_psd(samples, center_freq, F_sampling, N)
plot_raw_iq(samples, num_plot_samples)