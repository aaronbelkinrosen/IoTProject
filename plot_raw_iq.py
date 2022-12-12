# Plot raw IQ data

from pylab import *
import numpy as np

def plot_raw_iq(samples, N):

    # Store real and complex components of raw data in I and Q respectively
    I = []
    Q = []

    samples = samples[0:N]
    for i in range(N):
        I.append(samples[i].real)
        Q.append(samples[i].imag)
    
    #Use matplotlib to generate subplot
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Raw IQ Samples')
    ax1.plot(range(N), I)
    ax1.set_ylabel('I')
    ax2.plot(range(N), Q)
    ax2.set_ylabel('Q')
    plt.xlabel('Sample #')
    plt.show()