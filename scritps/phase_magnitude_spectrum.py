"""
This script returns the graph of the magnitude and phase spectra of the signals.

Last modification:
                Day: 11
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
from scipy.fft import rfft, rfftfreq, fftshift


def phase_magnitude_spectrum(voltage, current, N=100, F=60, scale=100):
    """
    This function returns the graph of the magnitude and phase spectra of the signals.
    :param voltage: Voltage matrix.
    :param current: Current matrix.
    :param N: Discrete period.
    :param F: System frequency.
    :param scale: Scale for sample period.
    :return: Graph.
    """
    xf = rfftfreq(N, 1 / (F * scale))
    xf_shift = fftshift(xf) / F

    va_f = rfft(voltage[0][:N], norm="forward")  # Fast fourier transforms: Phase A voltage
    vb_f = rfft(voltage[1][:N], norm="forward")  # Fast fourier transforms: Phase B voltage
    vc_f = rfft(voltage[2][:N], norm="forward")  # Fast fourier transforms: Phase C voltage

    ia_f = rfft(current[0][:N], norm="forward")  # Fast fourier transforms: Phase A current
    ib_f = rfft(current[1][:N], norm="forward")  # Fast fourier transforms: Phase B current
    ic_f = rfft(current[2][:N], norm="forward")  # Fast fourier transforms: Phase C current
    
    va_f_shift = fftshift(va_f)
    vb_f_shift = fftshift(vb_f)
    vc_f_shift = fftshift(vc_f)

    ia_f_shift = fftshift(ia_f)
    ib_f_shift = fftshift(ib_f)
    ic_f_shift = fftshift(ic_f)
    
    fig_v_A_m = go.Figure()
    fig_v_B_m = go.Figure()
    fig_v_C_m = go.Figure()
    fig_i_A_m = go.Figure()
    fig_i_B_m = go.Figure()
    fig_i_C_m = go.Figure()

    fig_v_A_pha = go.Figure()
    fig_v_B_pha = go.Figure()
    fig_v_C_pha = go.Figure()
    fig_i_A_pha = go.Figure()
    fig_i_B_pha = go.Figure()
    fig_i_C_pha = go.Figure()
    
    posi_x = len(xf_shift) - 5
    # ==================================================
    for i, j in zip(xf_shift, va_f_shift):
        fig_v_A_m.add_trace(go.Scatter(
                                    x=[i, i],
                                    y=[0, 2 * np.abs(j)],
                                    mode='lines',
                                    line=dict(color='blue')
                                    ))
        
        fig_v_A_m.add_trace(go.Trace(x=[i],
                                 y=[2 * np.abs(j)],
                                 mode='markers',
                                 marker=dict(color='black', size=8)
                                 ))
    
    fig_v_A_m.update_layout(
                        showlegend=False,
                        xaxis=dict(
                            zeroline=False,
                            showgrid=False,
                            title='K'),
                        yaxis=dict(
                            zeroline=False,
                            showgrid=True,
                            showticklabels=False,
                            title='A_n'
                            ),
                        title='Magnitude spectrum: Phase A voltage',
                        annotations=[dict(x=posi_x,
                                          y=2 * np.max(np.abs(va_f_shift)),
                                          text=f"f_0 = {F} Hz",
                                          showarrow=False,
                                          font=dict(size=14,
                                                    color='black'
                                                    ))]
                        )
    # ==================================================

    for i, j in zip(xf_shift, vb_f_shift):
        fig_v_B_m.add_trace(go.Scatter(
                                    x=[i, i],
                                    y=[0, 2 * np.abs(j)],
                                    mode='lines',
                                    line=dict(color='blue')
                                    ))
        
        fig_v_B_m.add_trace(go.Trace(
                                x=[i],
                                y=[2 * np.abs(j)],
                                mode='markers',
                                marker=dict(color='black', size=8)
                                ))
        
    fig_v_B_m.update_layout(showlegend=False,
                        xaxis=dict(
                            zeroline=False,
                            showgrid=False,
                            title='K'),
                        yaxis=dict(
                            zeroline=False,
                            showgrid=True,
                            showticklabels=False,
                            title='A_n'
                            ),
                        title='Magnitude spectrum: Phase B voltage',
                        annotations=[dict(x=posi_x,
                                          y=2 * np.max(np.abs(vb_f_shift)),
                                          text=f"f_0 = {F} Hz",
                                          showarrow=False,
                                          font=dict(size=14,
                                                    color='black'
                                                    ))]
                        )
    # ==================================================

    for i, j in zip(xf_shift, vc_f_shift):
        fig_v_C_m.add_trace(go.Scatter(
                                    x=[i, i],
                                    y=[0, 2 * np.abs(j)],
                                    mode='lines',
                                    line=dict(color='blue')
                                    ))
        
        fig_v_C_m.add_trace(go.Trace(
                                x=[i],
                                y=[2 * np.abs(j)],
                                mode='markers',
                                marker=dict(color='black', size=8)
                                ))
        
    fig_v_C_m.update_layout(
                        showlegend=False,
                        xaxis=dict(
                            zeroline=False,
                            showgrid=False,
                            title='K'),
                        yaxis=dict(
                            zeroline=False,
                            showgrid=True,
                            showticklabels=False,
                            title='A_n'
                            ),
                        title='Magnitude spectrum: Phase C voltage',
                        annotations=[dict(x=posi_x,
                                          y=2 * np.max(np.abs(vc_f_shift)),
                                          text=f"f_0 = {F} Hz",
                                          showarrow=False,
                                          font=dict(size=14,
                                                    color='black'
                                                    ))]
                        )
    # ==================================================

    for i, j in zip(xf_shift, ia_f_shift):
        fig_i_A_m.add_trace(go.Scatter(
                                    x=[i, i],
                                    y=[0, 2 * np.abs(j)],
                                    mode='lines',
                                    line=dict(color='blue')
                                    ))
        
        fig_i_A_m.add_trace(go.Trace(
                                x=[i],
                                y=[2 * np.abs(j)],
                                mode='markers',
                                marker=dict(color='black', size=8)
                                ))
        
    fig_i_A_m.update_layout(
                        showlegend=False,
                        xaxis=dict(
                            zeroline=False,
                            showgrid=False,
                            title='K'),
                        yaxis=dict(
                            zeroline=False,
                            showgrid=True,
                            showticklabels=False,
                            title='A_n'
                            ),
                        title='Magnitude spectrum: Phase A current',
                        annotations=[dict(x=posi_x,
                                          y=2 * np.max(np.abs(ia_f_shift)),
                                          text=f"f_0 = {F} Hz",
                                          showarrow=False,
                                          font=dict(size=14,
                                                    color='black'
                                                    ))]
                        )
    # ==================================================

    for i, j in zip(xf_shift, ib_f_shift):
        fig_i_B_m.add_trace(go.Scatter(
                                    x=[i, i],
                                    y=[0, 2 * np.abs(j)],
                                    mode='lines',
                                    line=dict(color='blue')
                                    ))
        
        fig_i_B_m.add_trace(go.Trace(
                                x=[i],
                                y=[2 * np.abs(j)],
                                mode='markers',
                                marker=dict(color='black', size=8)
                                ))
        
    fig_i_B_m.update_layout(
                        showlegend=False,
                        xaxis=dict(
                            zeroline=False,
                            showgrid=False,
                            title='K'),
                        yaxis=dict(
                            zeroline=False,
                            showgrid=True,
                            showticklabels=False,
                            title='A_n'
                            ),
                        title='Magnitude spectrum: Phase B current',
                        annotations=[dict(x=posi_x,
                                          y=2 * np.max(np.abs(ib_f_shift)),
                                          text=f"f_0 = {F} Hz",
                                          showarrow=False,
                                          font=dict(size=14,
                                                    color='black'
                                                    ))]
                        )
    # ==================================================

    for i, j in zip(xf_shift, ic_f_shift):
        fig_i_C_m.add_trace(go.Scatter(
                                    x=[i, i],
                                    y=[0, 2 * np.abs(j)],
                                    mode='lines',
                                    line=dict(color='blue')
                                    ))
        
        fig_i_C_m.add_trace(go.Trace(
                                x=[i],
                                y=[2 * np.abs(j)],
                                mode='markers',
                                marker=dict(color='black', size=8)
                                ))
        
    fig_i_C_m.update_layout(
                        showlegend=False,
                        xaxis=dict(
                            zeroline=False,
                            showgrid=False,
                            title='K'),
                        yaxis=dict(
                            zeroline=False,
                            showgrid=True,
                            showticklabels=False,
                            title='A_n',
                            ),
                        title='Magnitude spectrum: Phase C current',
                        annotations=[dict(x=posi_x,
                                          y=2 * np.max(np.abs(ic_f_shift)),
                                          text=f"f_0 = {F} Hz",
                                          showarrow=False,
                                          font=dict(size=14,
                                                    color='black'
                                                    ))]
                        )
    # ==================================================

    for i, j in zip(xf_shift, va_f_shift):
        fig_v_A_pha.add_trace(go.Scatter(x=[i, i],
                                   y=[0, np.angle(j)],
                                   mode='lines',
                                   line=dict(color='black')
                                   ))
        
        fig_v_A_pha.add_trace(go.Trace(x=[i],
                                 y=[np.angle(j)],
                                 mode='markers',
                                 marker=dict(color='blue', size=8)
                                 ))

    fig_v_A_pha.update_layout(showlegend=False,
                        xaxis=dict(zeroline=False,
                                    showgrid=False,
                                    title='K'),
                        yaxis=dict(zeroline=False,
                                    showgrid=True,
                                    title='Φ_n',
                                    tickvals=[np.pi, 3*np.pi/4, np.pi/2, np.pi/4, 0, -np.pi/4, -np.pi/2, -3*np.pi/4, -np.pi],
                                    ticktext=["π", "3π/4", "π/2", "π/4", "0", "-π/4", "-π/2", "-3π/4", "-π"]
                                    ),
                        title='Phase spectrum: Phase A voltage'
                        )
    # ==================================================

    for i, j in zip(xf_shift, vb_f_shift):
        fig_v_B_pha.add_trace(go.Scatter(x=[i, i],
                                   y=[0, np.angle(j)],
                                   mode='lines',
                                   line=dict(color='black')
                                   ))
        
        fig_v_B_pha.add_trace(go.Trace(x=[i],
                                 y=[np.angle(j)],
                                 mode='markers',
                                 marker=dict(color='blue', size=8)
                                 ))

    fig_v_B_pha.update_layout(showlegend=False,
                        xaxis=dict(zeroline=False,
                                    showgrid=False,
                                    title='K'),
                        yaxis=dict(zeroline=False,
                                    showgrid=True,
                                    title='Φ_n',
                                    tickvals=[np.pi, 3*np.pi/4, np.pi/2, np.pi/4, 0, -np.pi/4, -np.pi/2, -3*np.pi/4, -np.pi],
                                    ticktext=["π", "3π/4", "π/2", "π/4", "0", "-π/4", "-π/2", "-3π/4", "-π"]
                                    ),
                        title='Phase spectrum: Phase B voltage'
                        )
    # ==================================================

    for i, j in zip(xf_shift, vc_f_shift):
        fig_v_C_pha.add_trace(go.Scatter(x=[i, i],
                                   y=[0, np.angle(j)],
                                   mode='lines',
                                   line=dict(color='black')
                                   ))
        
        fig_v_C_pha.add_trace(go.Trace(x=[i],
                                 y=[np.angle(j)],
                                 mode='markers',
                                 marker=dict(color='blue', size=8)
                                 ))

    fig_v_C_pha.update_layout(showlegend=False,
                        xaxis=dict(zeroline=False,
                                    showgrid=False,
                                    title='K'),
                        yaxis=dict(zeroline=False,
                                    showgrid=True,
                                    title='Φ_n',
                                    tickvals=[np.pi, 3*np.pi/4, np.pi/2, np.pi/4, 0, -np.pi/4, -np.pi/2, -3*np.pi/4, -np.pi],
                                    ticktext=["π", "3π/4", "π/2", "π/4", "0", "-π/4", "-π/2", "-3π/4", "-π"]
                                    ),
                        title='Phase spectrum: Phase C voltage'
                        )
        
    # ==================================================
    for i, j in zip(xf_shift, ia_f_shift):   
        fig_i_A_pha.add_trace(go.Scatter(x=[i, i],
                                         y=[0, np.angle(j)],
                                         mode='lines',
                                         line=dict(color='black')
                                         ))
            
        fig_i_A_pha.add_trace(go.Trace(x=[i],
                                       y=[np.angle(j)],
                                       mode='markers',
                                       marker=dict(color='blue', size=8)
                                       ))
            
    fig_i_A_pha.update_layout(showlegend=False,
                            xaxis=dict(
                                zeroline=False,
                                showgrid=False,
                                title='K'),
                            yaxis=dict(
                                zeroline=False,
                                showgrid=True,
                                title='Φ_n',
                                tickvals=[np.pi, 3*np.pi/4, np.pi/2, np.pi/4, 0, -np.pi/4, -np.pi/2, -3*np.pi/4, -np.pi],
                                ticktext=["π", "3π/4", "π/2", "π/4", "0", "-π/4", "-π/2", "-3π/4", "-π"]
                                ),
                            title='Phase spectrum: Phase A current'
                            )
        
    # ==================================================
    for i, j in zip(xf_shift, ib_f_shift):   
        fig_i_B_pha.add_trace(go.Scatter(x=[i, i],
                                         y=[0, np.angle(j)],
                                         mode='lines',
                                         line=dict(color='black')
                                         ))
            
        fig_i_B_pha.add_trace(go.Trace(x=[i],
                                       y=[np.angle(j)],
                                       mode='markers',
                                       marker=dict(color='blue', size=8)
                                       ))
            
    fig_i_B_pha.update_layout(showlegend=False,
                            xaxis=dict(
                                zeroline=False,
                                showgrid=False,
                                title='K'),
                            yaxis=dict(
                                zeroline=False,
                                showgrid=True,
                                title='Φ_n',
                                tickvals=[np.pi, 3*np.pi/4, np.pi/2, np.pi/4, 0, -np.pi/4, -np.pi/2, -3*np.pi/4, -np.pi],
                                ticktext=["π", "3π/4", "π/2", "π/4", "0", "-π/4", "-π/2", "-3π/4", "-π"]
                                ),
                            title='Phase spectrum: Phase B current'
                            )
        
    # ==================================================
    for i, j in zip(xf_shift, ic_f_shift):   
        fig_i_C_pha.add_trace(go.Scatter(x=[i, i],
                                         y=[0, np.angle(j)],
                                         mode='lines',
                                         line=dict(color='black')
                                         ))
            
        fig_i_C_pha.add_trace(go.Trace(x=[i],
                                       y=[np.angle(j)],
                                       mode='markers',
                                       marker=dict(color='blue', size=8)
                                       ))
            
    fig_i_C_pha.update_layout(showlegend=False,
                            xaxis=dict(
                                zeroline=False,
                                showgrid=False,
                                title='K'),
                            yaxis=dict(
                                zeroline=False,
                                showgrid=True,
                                title='Φ_n',
                                tickvals=[np.pi, 3*np.pi/4, np.pi/2, np.pi/4, 0, -np.pi/4, -np.pi/2, -3*np.pi/4, -np.pi],
                                ticktext=["π", "3π/4", "π/2", "π/4", "0", "-π/4", "-π/2", "-3π/4", "-π"]
                                ),
                            title='Phase spectrum: Phase C current'
                            )
        
    return fig_v_A_m, fig_v_B_m, fig_v_C_m, fig_i_A_m, fig_i_B_m, fig_i_C_m, fig_v_A_pha, fig_v_B_pha, fig_v_C_pha, fig_i_A_pha, fig_i_B_pha, fig_i_C_pha
