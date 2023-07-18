"""
This script returns the table with the information associated with each harmonic.

Last modification:
                Day: 17
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""


import plotly.graph_objects as go


def create_columns(value):
    return [value[0], '{}'.format(value[1]), '{}'.format(value[2]), '{}'.format(value[3]), '{}'.format(value[4]), '{}'.format(value[5]), '{}'.format(value[6])]


def information_harmonics(info, phase):
    """
    This script returns the table with the information associated with each harmonic.
    :return: Table.
    """
    tab_data = [
        *zip(*[create_columns(item) for item in info])
        ]


    tab = go.Figure(
        data=[go.Table(
                header=dict(values=['Harmonic', 'VRMS [V]', 'IRMS [A]', 'P [W]', 'Q [VAR]', 'S [VA]', 'fp']),
                cells=dict(values=tab_data)
                )
            ]
        )
    
    tab.update_layout(title=f"Harmonic information: phase {phase}")

    return tab
