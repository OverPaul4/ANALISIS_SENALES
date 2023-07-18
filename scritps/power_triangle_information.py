"""
This script returns the table with the power triangle information.

Last modification:
                Day: 16
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""


import plotly.graph_objects as go


def power_triangle_information(p, q, d, s, fp):
    """
    This function returns the table with the power triangle information.
    :param p: Active power.
    :param q: Reactive power.
    :param d: Distortion power.
    :param s: Apparent power.
    :param fp: Power factor.
    :return: Table.
    """

    fig = go.Figure(
        data=[go.Table(
            header=dict(
                values=['variable', 'Value']),
            cells=dict(
                values=[['P', 'Q', 'D', 'S', 'fp'],
                        ['{} W'.format(p), '{} VAR'.format(q), '{} VAD'.format(d), '{} VA'.format(s), '{}'.format(fp)],
                        ]))
        ])
    return fig
