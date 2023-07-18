"""
This script returns the power triangle graphs. 

Last modification:
                Day: 16
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""
# Bookstores
import numpy as np
import plotly.graph_objects as go
from scritps.scritps_general.power import power


def power_triangle(voltage, current):
    """
    This function returns the power triangle graphs. 
    :param voltage: Voltage matrix.
    :param current: Current matrix.
    :return: List with power triangles.
    """
    result = power(voltage, current)
    p = result[0]
    q = result[1]
    d = result[2]
    s = result[3]

    # =====================================================
    # PHASE A POWER TRIANGLE
    fig_A = go.Figure()
    fig_A.add_trace(go.Scatter3d(x=[0, p[0]],
                                 y=[0, 0],
                                 z=[0, 0],
                                 mode='lines+markers',
                                hovertemplate=f'P<br>magnitude: {p[0]}<extra></extra>',
                                name='P'
                                 ))
    
    fig_A.add_trace(go.Scatter3d(x=[p[0], p[0]],
                                 y=[0, q[0]],
                                 z=[0, 0],
                                 mode='lines+markers',
                                hovertemplate=f'Q<br>magnitude: {q[0]}<extra></extra>',
                                name='Q'
                                 ))
    
    fig_A.add_trace(go.Scatter3d(x=[p[0], p[0]],
                                 y=[q[0], q[0]],
                                 z=[0, d[0]],
                                 mode='lines+markers',
                                 hovertemplate=f'D<br>magnitude: {d[0]}<extra></extra>',
                                 name='D'
                                 ))
    
    fig_A.add_trace(go.Scatter3d(x=[0, p[0]],
                                 y=[0, q[0]],
                                 z=[0, d[0]],
                                 mode='lines+markers',
                                 hovertemplate=f'S<br>magnitude: {s[0]}<extra></extra>',
                                 name='S'
                                 ))
    
    fig_A.update_layout(title='Phase A Power Triangle',
                        scene=dict(xaxis_title='P',
                                   yaxis_title='Q',
                                   zaxis_title='D'
                                   ),
                                   margin=dict(l=0, r=0, b=0, t=30)
                                   )
    
    # =====================================================
    # PHASE B POWER TRIANGLE
    fig_B = go.Figure()
    fig_B.add_trace(go.Scatter3d(x=[0, p[1]],
                                 y=[0, 0],
                                 z=[0, 0],
                                 mode='lines+markers',
                                hovertemplate=f'P<br>magnitude: {p[1]}<extra></extra>',
                                name='P'
                                 ))
    
    fig_B.add_trace(go.Scatter3d(x=[p[1], p[1]],
                                 y=[0, q[1]],
                                 z=[0, 0],
                                 mode='lines+markers',
                                hovertemplate=f'Q<br>magnitude: {q[1]}<extra></extra>',
                                name='Q'
                                 ))
    
    fig_B.add_trace(go.Scatter3d(x=[p[1], p[1]],
                                 y=[q[1], q[1]],
                                 z=[0, d[1]],
                                 mode='lines+markers',
                                 hovertemplate=f'D<br>magnitude: {d[1]}<extra></extra>',
                                 name='D'
                                 ))
    
    fig_B.add_trace(go.Scatter3d(x=[0, p[1]],
                                 y=[0, q[1]],
                                 z=[0, d[1]],
                                 mode='lines+markers',
                                 hovertemplate=f'S<br>magnitude: {s[1]}<extra></extra>',
                                 name='S'
                                 ))
    
    fig_B.update_layout(title='Phase B Power Triangle',
                        scene=dict(xaxis_title='P',
                                   yaxis_title='Q',
                                   zaxis_title='D'
                                   ),
                                   margin=dict(l=0, r=0, b=0, t=30)
                                   )
    
    # =====================================================
    # PHASE C POWER TRIANGLE
    fig_C = go.Figure()
    fig_C.add_trace(go.Scatter3d(x=[0, p[2]],
                                 y=[0, 0],
                                 z=[0, 0],
                                 mode='lines+markers',
                                hovertemplate=f'P<br>magnitude: {p[2]}<extra></extra>',
                                name='P'
                                 ))
    
    fig_C.add_trace(go.Scatter3d(x=[p[2], p[2]],
                                 y=[0, q[2]],
                                 z=[0, 0],
                                 mode='lines+markers',
                                hovertemplate=f'Q<br>magnitude: {q[2]}<extra></extra>',
                                name='Q'
                                 ))
    
    fig_C.add_trace(go.Scatter3d(x=[p[2], p[2]],
                                 y=[q[2], q[2]],
                                 z=[0, d[2]],
                                 mode='lines+markers',
                                 hovertemplate=f'D<br>magnitude: {d[2]}<extra></extra>',
                                 name='D'
                                 ))
    
    fig_C.add_trace(go.Scatter3d(x=[0, p[2]],
                                 y=[0, q[2]],
                                 z=[0, d[2]],
                                 mode='lines+markers',
                                 hovertemplate=f'S<br>magnitude: {s[2]}<extra></extra>',
                                 name='S'
                                 ))
    
    fig_C.update_layout(title='Phase C Power Triangle',
                        scene=dict(xaxis_title='P',
                                   yaxis_title='Q',
                                   zaxis_title='D'
                                   ),
                                   margin=dict(l=0, r=0, b=0, t=30)
                                   )
    
    # =====================================================
    # PHASE GENERAL POWER TRIANGLE
    fig_G = go.Figure()
    fig_G.add_trace(go.Scatter3d(x=[0, p[3]],
                                 y=[0, 0],
                                 z=[0, 0],
                                 mode='lines+markers',
                                hovertemplate=f'P<br>magnitude: {p[3]}<extra></extra>',
                                name='P'
                                 ))
    
    fig_G.add_trace(go.Scatter3d(x=[p[3], p[3]],
                                 y=[0, q[3]],
                                 z=[0, 0],
                                 mode='lines+markers',
                                hovertemplate=f'Q<br>magnitude: {q[3]}<extra></extra>',
                                name='Q'
                                 ))
    
    fig_G.add_trace(go.Scatter3d(x=[p[3], p[3]],
                                 y=[q[3], q[3]],
                                 z=[0, d[3]],
                                 mode='lines+markers',
                                 hovertemplate=f'D<br>magnitude: {d[3]}<extra></extra>',
                                 name='D'
                                 ))
    
    fig_G.add_trace(go.Scatter3d(x=[0, p[3]],
                                 y=[0, q[3]],
                                 z=[0, d[3]],
                                 mode='lines+markers',
                                 hovertemplate=f'S<br>magnitude: {s[3]}<extra></extra>',
                                 name='S'
                                 ))
    
    fig_G.update_layout(title='Equivalent Power Triangle',
                        scene=dict(xaxis_title='P',
                                   yaxis_title='Q',
                                   zaxis_title='D'
                                   ),
                                   margin=dict(l=0, r=0, b=0, t=30)
                                   )

    return fig_A, fig_B, fig_C, fig_G
    