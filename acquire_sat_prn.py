# Satellite Acquisition Algorithm to Find PRN Code
from GPS_PRN_Generator import *
import numpy as np
from pylab import *

def acquire_sat_prn(): # arg is N, number of samples for siganl (set N = 2048 (greater than 20000 for 1 ms and power of 2 for FFT)

    samples = np.fromfile('rx_data_copy.iq', np.int8).astype(np.float32).view(np.complex64) # dream would be 3D plot with prn on x, freq index y, mag z
    
    num_samples = 2048
    prn_list = range(1,32,1)
    freq_index = range(0,2048,1) 

    # Try each PRN code
    for sat in prn_list:

        #x_axis_prndata = [sat]*2048
        test_prn = PRN(sat, False) # False doesn't plot PRN for each satellite
        magnitude_list = []

        for i in range(len(samples[0:2048])): # shift through iq data and append average magnitude for each fft

            # Dynamically pad front and back with zeros, element-wise multiply vectors, fft, and magnitude squared result
            new_prn = [0]*i + test_prn + [0]*(2048-len(test_prn)-i) # (newprn and samples[0:N] must always be same size since mult and fft)
            try:
                prod = np.multiply(samples[0:2048], new_prn)
                mag_result = np.abs(np.fft.fft(prod))**2
                magnitude_list.append(np.average(mag_result))

                # Prints for visual feedback on how outlier search is going :)
                # if np.average(mag_result) > 20000: # catch outliers in magnitude size!
                #     print('OUTLIER FOUND! sat: %d ' %sat )
                # else:
                #     print('No Outlier: %d  ' %sat, np.average(mag_result))
            except:
                pass
        
        hist, bins = np.histogram(magnitude_list, bins=10)
        center = (bins[:-1] + bins[1:])/2
        width = 0.7 * (bins[1] - bins[0])
        plt.bar(center, hist, align='center', width=width)
        plt.title('Average FFT Magnitude of Satellite %d PRN Code x IQ Data' %sat)
        plt.ylabel('Frequency of Magnitude Data')
        plt.xlabel('Sample Value')
        plt.show()
            
          


