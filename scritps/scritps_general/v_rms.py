"""
This script calculates the RMS values of the voltages.
Last modification:
                Day: 12
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""
import numpy as np
from scipy.fft import rfft


def v_rms(voltage, N=100):
    """
    This function calculates the RMS values of the voltages.
    :param voltage: Voltage matrix.
    :param N: Discrete period.
    :param F: System frequency.
    :param scale: Scale for sample period.
    :return: List with RMS values.
    """
    list_vrms = list()

    for i in range(3):
        v_f = voltage[i][:N]
        v_f = rfft(v_f, norm="forward")    
        An = 2 * np.abs(v_f[1:])
        An_filtered = An[An > 0.01]
        vrms = np.sqrt(np.sum((An_filtered / np.sqrt(2)) ** 2))
        list_vrms.append(vrms)
    
    list_vrms = np.round(np.array(list_vrms), 3)
    return list_vrms
