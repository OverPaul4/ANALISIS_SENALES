"""
This script returns the table with the information of the consumed energy and its cost.

Last modification:
                Day: 25
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""

import plotly.graph_objects as go
from scritps.scritps_general.energy import energy


def information_energy(p, q, cost_p, cost_q, time):
    """
    This function returns the table with the information of the consumed energy and its cost.
    :param p: Total active power at node.
    :param q: Total reactive power at node.
    :param cost_p: Active energy cost.
    :param cost_q: Reactive energy cost.
    :param time: Time interval.
    :return: Table.
    """
    result = energy(p, q, cost_p, cost_q, time)

    fig = go.Figure(
        data=[go.Table(
            header=dict(
                values=['variable', 'Value']),
            cells=dict(
                values=[['Active energy', 'Reactive energy', 'Active energy cost', 'Reactive energy cost', 'Total energy cost'],
                        ['{} kWh'.format(round(result[0], 3)), '{} kVArh'.format(round(result[1], 3)), '$ {}'.format(round(result[2], 3)), '$ {}'.format(round(result[3], 3)), '$ {}'.format(round(result[4], 3))],
                        ]))
        ])
    return fig
