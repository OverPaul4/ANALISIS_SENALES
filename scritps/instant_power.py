"""
This script returns the graph of the instantaneous power per phase.

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


def instant_power(voltage, current, N=200):
    """
    This function returns the graph of the instantaneous power per phase.
    :param voltage: Voltage matrix.
    :param current: Current matrix.
    :param N: Discrete period.
    :return: Graph
    """
    names_signal = ['P_A', 'P_B', 'P_C']
    size = np.shape(voltage)
    samples_time = time(size[1])

    fig = go.Figure()
    for i in range(size[0]):
        fig.add_trace(go.Scatter(x=samples_time[:N],
                                 y=voltage[i][:N] * current[i][:N],
                                 mode='lines',
                                 name=names_signal[i]))

    fig.update_layout(title_text='Instantaneous power per phase',
                      xaxis=dict(title='Time'),
                      yaxis=dict(title='Power'),
                      )
    return fig
