# HackRF RX and binary data signal processing of SDR IQ data

from libhackrf import *
from pylab import *
import os
import numpy as np

# Use hackrf_transfer to generate binary file
cmd = 'hackrf_transfer '
rx_filename = '-r rx_data.iq '
freq_cmd = '-f 1575420000 '
sample_rate = '-s 20000000 '
num_samples = '-n 1000 '
os.system(cmd + rx_filename + freq_cmd + sample_rate + num_samples)


# Open binary file and convert binary data to IQ 
samples = np.fromfile('rx_data.iq', np.int8).astype(np.float32).view(np.complex64) # cast int8 IQ data to float32,float32 (I,Q)
samples /= 128 # convert complex data to -1 to 1 to avoid Rx saturation
#print(samples)

    