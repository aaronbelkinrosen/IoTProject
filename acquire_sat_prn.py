# Satellite Acquisition Algorithm to Find PRN Code
from GPS_PRN_Generator import *
import numpy as np

def acquire_sat_prn(): # arg is N, number of samples for siganl (set N = 32768 (greater than 20000 for 1 ms and power of 2 for FFT)

    samples = np.fromfile('rx_data.iq', np.int8).astype(np.float32).view(np.complex64)

    # Try each PRN code
    for sat in range(1,32,1):
        test_prn = PRN(sat, False) # False doesn't plot PRN for each satellite
        #print('testprn', len(test_prn))
        for i in range(len(samples[0:32768])):
            new_prn = [0]*i + test_prn + [0]*(32768-len(test_prn)-i) # pad front and back with zeros
            # print('newprn', len(new_prn))             newprn and samples[0:N] must always be same size since mult and fft
            # print('samples',len(samples[0:32768])) 
