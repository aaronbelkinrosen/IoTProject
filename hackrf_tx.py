# Implements hackrf_transfer command in terminal with options that tunes to receive GPS L1 Frequency

import os

def hackrf_tx(iq_filename): # takes string containing binary filename
    # Use hackrf_transfer terminal command with options to generate binary file
    cmd = 'hackrf_transfer '
    tx_filename = '-t ' + iq_filename + ' '
    freq_cmd = '-f 1575420000 ' # f_lo - f_if, filter out high freq harmonics of LO
    sample_rate = '-s 20000000'
    amp = '-a 1 '
    tx_gain = '-x 30'
    
    os.system(cmd + tx_filename + freq_cmd + sample_rate + amp + tx_gain) 