"""
This script returns the graph of the line currents that are equal to the phase currents, as well as the graph of the
neutral currents.
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


def current_line_phase_neutral(current, N=200):
    """
    This function returns the graph of the line currents that are equal to the phase currents, as well as the graph of
    the neutral currents.
    :param current: Current matrix.
    :param N: Discrete period.
    :return: Graph.
    """
    names_signal = ['Phase A', 'Phase B', 'Phase C']
    size = np.shape(current)
    samples_time = time(size[1])

    fig = go.Figure()
    for i in range(size[0]):
        fig.add_trace(go.Scatter(x=samples_time[:N],
                                 y=current[i][:N],
                                 mode='lines',
                                 name=names_signal[i]))

    fig.add_trace(go.Scatter(x=samples_time[:N],
                             y=current[0][:N] + current[1][:N] + current[2][:N],
                             mode='lines',
                             name='Neutral Current'))

    fig.update_layout(title_text='Line/phase and neutral current signal',
                      xaxis=dict(title='Time'),
                      yaxis=dict(title='Amplitude'),
                      )

    return fig
