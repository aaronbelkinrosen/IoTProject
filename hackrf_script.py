# HackRF RX and binary data signal processing of SDR IQ data
import time
from pylab import *
import os
import numpy as np

# Import user defined functions
from plot_psd import *
from plot_raw_iq import *
from GPS_PRN_Generator import *
from acquire_sat_prn import *
from hackrf_rx import *
from hackrf_tx import *

# Use hackrf_transfer terminal command with options to generate rx binary file
#hackrf_rx()

# Use hackrf_transfer terminal command to tx waveform from binary file
# binary_file = 'gpssim2.bin'
# i = 0
# while i < 5:
#     hackrf_tx(binary_file)
#     i += 1

# time.sleep(1)
# Open binary file and convert binary data to IQ 
#samples = np.fromfile('rx_data.iq', np.int8).astype(np.float32).view(np.complex64) # cast int8 IQ data to float32,float32 (I,Q)
#print(samples)

# Calculate avg power
# mean = np.mean(np.abs(samples)**2) # If roughly zero mean (can use var to calculate avg power since same eqn as var!)
# avg_pwr = np.var(samples)
#print(avg_pwr)

# Plot PSD, Raw IQ Data, and PRN Code Generator Outputs
center_freq = 1575420000 # SDR tuned for L1 GPS freq
F_sampling = 20000000 # 20 MHz sampling rate
N =  8192 # size of commplex array to perform fft on
num_plot_samples = 5000

#plot_psd(samples, center_freq, F_sampling, N)
#samples /= 128 # normalize since int8 from -128 to 127 so divide by 128
#plot_raw_iq(samples, num_plot_samples) # plot normalized raw IQ values

#prn_code = PRN(28,False) # Arg1: Satellite to Generate PRN For
                         # Arg2: True plot, false don't

# Satellite Acquisition Algorithm (try to correlate each satellite's PRN code to Rx signal iteratively)

acquire_sat_prn()

