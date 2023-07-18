"""
This script returns the graph of the instantaneous power per phase.

Last modification:
                Day: --
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""

import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html
from scritps.scritps import *
from scritps.scritps_general.power import power
from data.seniales_sep import PowerSystem


def selection_node(node):
    system = PowerSystem()
    Data = system.get_data()
    voltage, current = Data

    if node == 'Node 1':
        return [voltage[0], current[0]]
    elif node == 'Node 2':
        return [voltage[1], current[1]]
    elif node == 'Node 3':
        return [voltage[2], current[2]]


# ==========================================================
rawScenarios = ['Phase voltage', 'Line voltage', 'Line-Phase-Neutral current', 'Instant power', 'Magnitude-Phase spectrum',
                'Phase diagram harmonic: Voltage', 'Phase diagram harmonic: Current', 'Harmonic power triangle', 'Power triangle',
                'Energy results', 'Harmonic info', 'Report']


def createTab(scenario):
    return dbc.Tab(label=scenario, tab_id=scenario)


# ==========================================================
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [html.Img(src='assets/Logo_U.T.P.png', width='200px'),
     html.Hr(),
     dcc.Store(id="store"),
     html.H1("LINE ANALYZER"),
     html.Hr(),

     # ==============================================

     dbc.Row([
         dbc.Col([
             html.Div([
                 html.Div([

                     dbc.Button("Regenerate graphs",
                                color="primary",
                                id="button",
                                className="mb-3"),

                     html.Div([
                         dcc.Dropdown(['Node 1', 'Node 2', 'Node 3'],
                                      'Node 1',
                                      id='nodes',
                                      style={'width': '90%'}),
                         html.Div(id='salida_nodos'),
                     ]),
                     html.Br(),

                     html.H5('Hours Range'),
                     dcc.Input(id='input1',
                               type='number',
                               placeholder='Input Range...',
                               style={'marginRight': '10px'},
                               value='24')
                 ]),
                 html.Br(),
                 html.Div([
                     html.H5('Active energy cost [$/kWh]'),
                     dcc.Input(id='input2',
                               type='number',
                               placeholder='Input Cost...',
                               style={'marginRight': '10px'},
                               value='285.44')
                 ]),
                 html.Br(),
                 html.Div([
                     html.H5('Reactive energy cost [$/kVArh]'),
                     dcc.Input(id='input3',
                               type='number',
                               placeholder='Input Cost...',
                               style={'marginRight': '10px'},
                               value='189.78')
                 ]),
             ])
         ], md=3),
         dbc.Col([
             html.Div([
                 html.Img(src='assets/Media_tension.jpeg', style={'width': '700px'})
             ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'})
         ], md=9)
     ]),
     html.Br(),
     # ==============================================
     dbc.Tabs(
         list(map(createTab, rawScenarios)),
         id="tabs",
         active_tab="Phase voltage",
     ),
     html.Div(id="tab-content", className="p-4"),
     ])


# =============================================
# This section creates the sections where the graphics will go.
@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"),
     Input("store", "data"),
     ],
)
def render_tab_content(active_tab, data):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    # selection = selection_node(node)
    # result = power(selection[0], selection[1])
    # result2 = phase_diagram_harmonic(result[7])


    if active_tab and data is not None:
        if active_tab == "Phase voltage":
            return dcc.Graph(figure=data["Phase voltage"])

        elif active_tab == "Line voltage":
            return dcc.Graph(figure=data["voltage_line"])

        elif active_tab == "Line-Phase-Neutral current":
            return dcc.Graph(figure=data["current_line_phase_neutral"])

        elif active_tab == "Instant power":
            return dcc.Graph(figure=data["instant_power"])
       
        elif active_tab == "Magnitude-Phase spectrum":
            return dbc.Row([
                dbc.Col(dcc.Graph(figure=data["fig_v_A_m"]), width=6),
                dbc.Col(dcc.Graph(figure=data["fig_i_A_m"]), width=6),
            ]), dbc.Row([
                dbc.Col(dcc.Graph(figure=data["fig_v_A_pha"]), width=6),
                dbc.Col(dcc.Graph(figure=data["fig_i_A_pha"]), width=6),
            ]), dbc.Row([
                dbc.Col(dcc.Graph(figure=data["fig_v_B_m"]), width=6),
                dbc.Col(dcc.Graph(figure=data["fig_i_B_m"]), width=6),
            ]), dbc.Row([
                dbc.Col(dcc.Graph(figure=data["fig_v_B_pha"]), width=6),
                dbc.Col(dcc.Graph(figure=data["fig_i_B_pha"]), width=6),
            ]), dbc.Row([
                dbc.Col(dcc.Graph(figure=data["fig_v_C_m"]), width=6),
                dbc.Col(dcc.Graph(figure=data["fig_i_C_m"]), width=6),
            ]),  dbc.Row([
                dbc.Col(dcc.Graph(figure=data["fig_v_C_pha"]), width=6),
                dbc.Col(dcc.Graph(figure=data["fig_i_C_pha"]), width=6),
            ])

        elif active_tab == "Phase diagram harmonic: Voltage":
            return dcc.Graph(figure=data["phase_diagram_harmonic_voltage"])

        elif active_tab == "Phase diagram harmonic: Current":
            return dcc.Graph(figure=data["phase_diagram_harmonic_current"])

        elif active_tab == "Harmonic power triangle":
            return dbc.Row([
                dbc.Col(dcc.Graph(figure=data["harmonic_power_triangle_A"]), width=4),
                dbc.Col(dcc.Graph(figure=data["harmonic_power_triangle_B"]), width=4),
                dbc.Col(dcc.Graph(figure=data["harmonic_power_triangle_C"]), width=4),
            ])

        elif active_tab == "Power triangle":
            return dbc.Row([
                dbc.Col(dcc.Graph(figure=data["power_triangle_A"]), width=6),
                dbc.Col(dcc.Graph(figure=data["power_triangle_B"]), width=6),
            ]), dbc.Row([
                dbc.Col(dcc.Graph(figure=data["information_A"]), width=6),
                dbc.Col(dcc.Graph(figure=data["information_B"]), width=6),
            ]), dbc.Row([
                dbc.Col(dcc.Graph(figure=data["power_triangle_C"]), width=6),
                dbc.Col(dcc.Graph(figure=data["power_triangle_general"]), width=6),
            ]), dbc.Row([
                dbc.Col(dcc.Graph(figure=data["information_C"]), width=6),
                dbc.Col(dcc.Graph(figure=data["information_G"]), width=6),
            ]),

        elif active_tab == "Energy results":
            return dcc.Graph(figure=data["energy_results"])

        elif active_tab == "Harmonic info":
            return dbc.Row([
                dbc.Col(dcc.Graph(figure=data["harmonic_info_A"])),
            ]), dbc.Row([
                dbc.Col(dcc.Graph(figure=data["harmonic_info_B"])),
            ]),dbc.Row([
                dbc.Col(dcc.Graph(figure=data["harmonic_info_C"])),
            ]),
    
        elif active_tab == "Report":
            return dbc.Row([
                    dbc.Col(dcc.Graph(figure=data["report"])),
                ]), dbc.Row([
                    dbc.Col(dcc.Graph(figure=data["text_report"])),
                ])

        # elif active_tab == "Download pdf":
        #     return True
        
    return "No tab selected"


# =============================================
# This section adds the graphs to the dashboard
@app.callback(Output("store", "data"),
              [Input("button", "n_clicks"),
               Input("nodes", "value"),
               Input("input1", "value"),
               Input("input2", "value"),
               Input("input3", "value")]
              )
def generate_graphs(n, node, input1, input2, input3):
    """
    This callback generates three simple graphs from random data.
    """
    selection = selection_node(node)
    result = power(selection[0], selection[1])

    if not n:
        # generate empty graphs when app loads
        return {k: go.Figure(data=[]) for k in rawScenarios}

    fig_1 = voltage_phase(selection[0])
    fig_2 = voltage_line(selection[0])
    fig_3 = current_line_phase_neutral(selection[1])
    fig_4 = instant_power(selection[0], selection[1])

    fig_5 = phase_magnitude_spectrum(selection[0], selection[1])

    fig_6 = phase_diagram_harmonic(result[7])
    fig_7 = phase_diagram_harmonic(result[8])

    fig_8_A = harmonic_power_triangle(result[6][0], 'A')
    fig_8_B = harmonic_power_triangle(result[6][1], 'B')
    fig_8_C = harmonic_power_triangle(result[6][2], 'C')

    fig_9 = power_triangle(selection[0], selection[1])

    fig_9_A = power_triangle_information(result[0][0], result[1][0], result[2][0], result[3][0], result[4][0])
    fig_9_B = power_triangle_information(result[0][1], result[1][1], result[2][1], result[3][1], result[4][1])
    fig_9_C = power_triangle_information(result[0][2], result[1][2], result[2][2], result[3][2], result[4][2])
    fig_9_G = power_triangle_information(result[0][3], result[1][3], result[2][3], result[3][3], result[4][3])

    fig_10 = information_energy(result[0][3], result[1][3], input2, input3, input1)

    fig_11_A = information_harmonics(result[6][0], 'A')
    fig_11_B = information_harmonics(result[6][1], 'B')
    fig_11_C = information_harmonics(result[6][2], 'C')

    fig_12 = information_general(selection[0], selection[1], input2, input3, input1)

    # pdf = reporte(node, result[6], selection[0], selection[1], input2, input3, input1)

    return {"Phase voltage": fig_1, "voltage_line": fig_2, "current_line_phase_neutral": fig_3, "instant_power": fig_4,
            "fig_v_A_m": fig_5[0], "fig_v_B_m": fig_5[1], "fig_v_C_m": fig_5[2],
            "fig_i_A_m": fig_5[3], "fig_i_B_m": fig_5[4], "fig_i_C_m": fig_5[5],
            "fig_v_A_pha": fig_5[6], "fig_v_B_pha": fig_5[7], "fig_v_C_pha": fig_5[8],
            "fig_i_A_pha": fig_5[9], "fig_i_B_pha": fig_5[10], "fig_i_C_pha": fig_5[11],

            "phase_diagram_harmonic_voltage": fig_6,
            "phase_diagram_harmonic_current": fig_7,
            "harmonic_power_triangle_A": fig_8_A, "harmonic_power_triangle_B": fig_8_B, "harmonic_power_triangle_C": fig_8_C,
            "power_triangle_A": fig_9[0], "power_triangle_B": fig_9[1], "power_triangle_C": fig_9[2], "power_triangle_general": fig_9[3],
            "information_A": fig_9_A, "information_B": fig_9_B, "information_C": fig_9_C, "information_G": fig_9_G,
            "energy_results": fig_10,
            "harmonic_info_A": fig_11_A, "harmonic_info_B": fig_11_B, "harmonic_info_C": fig_11_C,
            "report": fig_12[0], "text_report": fig_12[1]
            }

# ==========================================================
if __name__ == '__main__':
    app.run_server(debug=True)
