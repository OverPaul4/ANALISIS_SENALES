"""
This script returns a list of times given an amount n of samples at a sampling frequency.

Last modification:
                Day: 05
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""
import numpy as np


def time(long, F=60, scale=100):
    """
    This function returns a list of times given an amount n of samples at a sampling frequency.
    :param long: Number of samples.
    :param F: frequency [Hz].
    :param scale: Scale factor for the sample rate.
    :return: Time list
    """
    Ts = 1 / (F * scale)              # Sampling period
    list_time = np.arange(long) * Ts  # Time list
    return list_time                  # Returns the list vector
