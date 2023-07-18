"""
This script returns the phasor diagrams per harmonic.

Last modification:
                Day: 22
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""

import plotly.subplots as sp
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def diagram(voltages, angles, phases):
    """
    This function returns the phasor diagrams per harmonic.
    :param voltages: List of maximum voltages.
    :param angles: List of maximum voltage angles.
    :param phases: List phase associated to each harmonic.
    :return: Graphs.
    """

    fig = go.Figure()
    for i in range(len(voltages)):
        fig.add_trace(go.Scatterpolar(r=[0, voltages[i]],
                                        theta=[0, angles[i]],
                                        name=f"Phase {phases[i]}",
                                        ))

    return fig


def sort_data(data):
    dict_voltages = dict()
    dict_angles = dict()
    dict_phases = dict()

    counter = 1
    for i in data:
        for j in i:
            llave = j[0]
            if llave not in dict_voltages:
                dict_voltages[llave] = []
            
            if llave not in dict_angles:
                dict_angles[llave] = []
            
            if llave not in dict_phases:
                dict_phases[llave] = []

            dict_voltages[llave].append(j[1])
            dict_angles[llave].append(j[2])

            if counter == 1:
                fase = 'A'
            elif counter == 2:
                fase = 'B'
            elif counter == 3:
                fase = 'C'

            dict_phases[llave].append(fase)
        counter +=1

    return dict_voltages, dict_angles, dict_phases


def order(dict_voltages):
    order_list = list(dict_voltages)
    order_list.sort()

    return order_list


def phase_diagram_harmonic(data):
    new_data = sort_data(data)
    harmonic_order = order(new_data[0])  # Total de armonicos y ordenados de menor a mayor

    num_plots = len(harmonic_order)
    rows = int(num_plots / 3) + (num_plots % 3 > 0)  # Calcular el número de filas necesarias

    fig = sp.make_subplots(
                        rows=rows,
                        cols=3,
                        subplot_titles=[f"Harmonic {h}" for h in harmonic_order], 
                        horizontal_spacing=0.2,
                        vertical_spacing=0.1,
                        specs=[[{'type': 'polar'}]*3]*rows)

    fig.update_layout(height=1300, width=1300)  # Ajustar el tamaño de la figura

    row, col = 1, 1
    for harmonic in harmonic_order:
        voltages = new_data[0][harmonic]
        angles = new_data[1][harmonic]
        phases = new_data[2][harmonic]

        diagram_fig = diagram(voltages, angles, phases)
        for trace in diagram_fig['data']:
            fig.add_trace(trace, row=row, col=col)

        col += 1
        if col > 3:
            col = 1
            row += 1

    fig.update_layout(showlegend=True)

    return fig
