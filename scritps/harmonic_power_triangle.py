"""
This script returns the power triangles per harmonic.

Last modification:
                Day: 22
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def triangle(p, q):
    """
    This function returns the power triangle.    
    :param p: Active power.
    :param q: Reactive power.
    :return: Graph.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, p],
                             y=[0, 0],
                             mode='lines+markers',
                             name='P'
                             ))
    
    fig.add_trace(go.Scatter(x=[p, p],
                             y=[0, q],
                             mode='lines+markers',
                             name='Q'
                             ))

    fig.add_trace(go.Scatter(x=[0, p],
                             y=[0, q],
                             mode='lines+markers',
                             name='S'
                             ))

    # Agregar etiquetas
    # fig.add_annotation(x=0.05,
    #                    y=0.95,
    #                    xref="paper", 
    #                    yref="paper",
    #                    text=f'P= {p} W',
    #                    showarrow=False,
    #                    font=dict(size=8,
    #                              color='black'
    #                              )
    #                     ) 

    return fig
   

def harmonic_power_triangle(data, phase):
    """
    This function returns the power triangles per harmonic.
    :param data: nformation for power triangle construction.
    :param phase: Phase.
    :return: Graphs.
    """
    titles = [f"Power triangle: Harmonic {data[i][0]}" for i in range(len(data))]
    fig = make_subplots(rows=len(data),
                        cols=1,
                        subplot_titles=titles)

    for i in range(len(data)):
        triangle_fig = triangle(data[i][3], data[i][4])
        for trace in triangle_fig['data']:
            fig.add_trace(trace, 
                          row=i + 1,
                          col=1)
        
        # Agregar texto adicional a cada gráfico        
        fig.add_annotation(
                   x=0,
                   y=data[i][4],
                   xanchor='left',
                   yanchor='top',
                   xref="paper",
                   yref="paper",
                   text=f'P= {data[i][3]} W',
                   showarrow=False,
                   font=dict(size=12, color='black'),
                   row=i+1,
                   col=1)

        fig.add_annotation(
                   x=0,
                   y=data[i][4] * 0.9,
                   xanchor='left',
                   yanchor='top',
                   xref="paper",
                   yref="paper",
                   text=f'Q= {data[i][4]} VAR',
                   showarrow=False,
                   font=dict(size=12, color='black'),
                   row=i+1,
                   col=1)

        fig.add_annotation(
                   x=0,
                   y=data[i][4] * 0.8,
                   xanchor='left',
                   yanchor='top',
                   xref="paper",
                   yref="paper",
                   text=f'S= {data[i][5]} VA',
                   showarrow=False,
                   font=dict(size=12, color='black'),
                   row=i+1,
                   col=1)

        fig.add_annotation(
                   x=0,
                   y=data[i][4] * 0.7,
                   xanchor='left',
                   yanchor='top',
                   xref="paper",
                   yref="paper",
                   text=f'fp= {data[i][6]}',
                   showarrow=False,
                   font=dict(size=12, color='black'),
                   row=i+1,
                   col=1)
    
    fig.update_xaxes(title_text="P")
    fig.update_yaxes(title_text="Q")

    fig.update_layout(height=300*len(data),
                      width=500, 
                      title_text=f"Harmonic Power Triangles: Phase {phase}",
                      showlegend=False)

    return fig
