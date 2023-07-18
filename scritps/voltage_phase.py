"""
This script returns the graphs of the voltage per phase.

Last modification:
                Day: 05
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""

# Bookstores
import plotly.graph_objects as go
import numpy as np
from scritps.time import time


def voltage_phase(voltage, N=200):
    """
    This function returns the graphs of the voltage per phase.
    :param voltage: Voltage matrix.
    :param N: Discrete period.
    :return: Graph.
    """
    names_signal = ['Phase A', 'Phase B', 'Phase C']

    size = np.shape(voltage)  # Voltage matrix dimension
    samples_time = time(size[1])

    fig = go.Figure()
    for i in range(size[0]):
        fig.add_trace(go.Scatter(x=samples_time[:N],
                                 y=voltage[i][:N],
                                 mode='lines',
                                 name=names_signal[i]))

    fig.update_layout(title_text='Phase voltage signal',
                      xaxis=dict(title='Time'),
                      yaxis=dict(title='Amplitude'),
                      )
    return fig
