# Implements hackrf_transfer command in terminal with options that tunes to receive GPS L1 Frequency

import os

def hackrf_rx(): 
    # Use hackrf_transfer terminal command with options to generate binary file
    cmd = 'hackrf_transfer '
    rx_filename = '-r rx_data.iq '
    freq_cmd = '-f 1575420000 ' # f_lo - f_if, filter out high freq harmonics of LO
    local_osc_freq = '-o 3775420000 '
    if_freq = '-i 2200000000 '
    image_rej = '-m 1 '
    sample_rate = '-s 20000000 '
    num_samples = '-n 100000 ' 
    lna_gain = '-l 24 '
    #baseband_gain = '-g 10 ' # get dc offset at baseband, amplify and can saturate...
    baseband_bw = '-b 10000000 '
    crystal_err = '-C 1'

    os.system(cmd + rx_filename + freq_cmd + local_osc_freq + if_freq + image_rej + \
        sample_rate + num_samples + lna_gain + baseband_bw + crystal_err)

    #os.system('cp rx_data.iq rx_data_acquire_test')