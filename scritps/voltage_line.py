"""
This script returns line tension graphs.

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


def voltage_line(voltage, N=200):
    """
    This function returns line tension graphs.
    :param voltage: Voltage matrix.
    :param N: Discrete period.
    :return: Graph.
    """
    names_signal = ['Line AB', 'Line BC', 'Line CA']
    matrix_A = np.array([[1, -1, 0],
                         [0, 1, -1],
                         [-1, 0, 1]])

    voltage = np.dot(matrix_A, voltage)
    size = np.shape(voltage)  # Voltage matrix dimension
    samples_time = time(size[1])

    fig = go.Figure()
    for i in range(size[0]):
        fig.add_trace(go.Scatter(x=samples_time[:N],
                                 y=voltage[i][:N],
                                 mode='lines',
                                 name=names_signal[i]))

    fig.update_layout(title_text='Line voltage signal',
                      xaxis=dict(title='Time'),
                      yaxis=dict(title='Amplitude'),
                      )
    return fig
