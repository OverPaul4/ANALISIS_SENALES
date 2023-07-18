"""
This script returns the table with the primary information of the system.

Last modification:
                Day: 13
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""
import numpy as np
import plotly.graph_objects as go
from scritps.scritps_general.scripts_general import *


def information_general(voltage, current, cost_p, cost_q, time):
    """
    This function returns the table with the primary information of the system.
    :param voltage: Voltage matrix.
    :param current: Current matrix.
    :param cost_p: Active energy cost.
    :param cost_q: Reactive energy cost.
    :param time: Time interval.
    :return: Table.
    """
    vrms = v_rms(voltage)
    irms = i_rms(current)
    result = power(voltage, current)
    p = result[0]
    q = result[1]
    d = result[2]
    s = result[3]
    fp = result[4]
    harmonics = result[5]
    vrms_harmonic = result[9]
    irms_harmonic = result[10]
    result2 = energy(p[3], q[3], cost_p, cost_q, time)

    THD_V_A = (np.sqrt(np.sum(np.array(vrms_harmonic[0][1:]) ** 2)) / vrms_harmonic[0][0]) * 100
    THD_V_B = (np.sqrt(np.sum(np.array(vrms_harmonic[1][1:]) ** 2)) / vrms_harmonic[1][0]) * 100
    THD_V_C = (np.sqrt(np.sum(np.array(vrms_harmonic[2][1:]) ** 2)) / vrms_harmonic[2][0]) * 100

    THD_I_A = (np.sqrt(np.sum(np.array(irms_harmonic[0][1:]) ** 2)) / irms_harmonic[0][0]) * 100
    THD_I_B = (np.sqrt(np.sum(np.array(irms_harmonic[1][1:]) ** 2)) / irms_harmonic[1][0]) * 100
    THD_I_C = (np.sqrt(np.sum(np.array(irms_harmonic[2][1:]) ** 2)) / irms_harmonic[2][0]) * 100

    tab1 = go.Figure(
        data=[go.Table(
            header=dict(
                values=[' ', 'Phase A', 'Phase B', 'Phase C', 'Total/Equivalent/Cost']
                ),
            cells=dict(
                values=[['VRMS', 'IRMS', 'P', 'Q', 'D', 'S', 'harmonics','THD_V', 'THD_I', 'fp', 'Ep', 'Eq', '$Ep', '$Eq', '$E'],
                        ['{} V'.format(vrms[0]), '{} A'.format(irms[0]), '{} W'.format(p[0]), '{} VAR'.format(q[0]), '{} VAD'.format(d[0]), '{} VA'.format(s[0]), '{}'.format(harmonics[0]), '{} %'.format(round(THD_V_A, 3)), '{} %'.format(round(THD_I_A, 3)), '{}'.format(fp[0]), 'N.A', 'N.A', 'N.A', 'N.A', 'N.A'],
                        ['{} V'.format(vrms[1]), '{} A'.format(irms[1]), '{} W'.format(p[1]), '{} VAR'.format(q[1]), '{} VAD'.format(d[1]), '{} VA'.format(s[1]), '{}'.format(harmonics[1]), '{} %'.format(round(THD_V_B, 3)), '{} %'.format(round(THD_I_B, 3)), '{}'.format(fp[1]), 'N.A', 'N.A', 'N.A', 'N.A', 'N.A'],
                        ['{} V'.format(vrms[2]), '{} A'.format(irms[2]), '{} W'.format(p[2]), '{} VAR'.format(q[2]), '{} VAD'.format(d[2]), '{} VA'.format(s[2]), '{}'.format(harmonics[2]), '{} %'.format(round(THD_V_C, 3)), '{} %'.format(round(THD_I_C, 3)), '{}'.format(fp[2]), 'N.A', 'N.A', 'N.A', 'N.A', 'N.A'],

                        ['N.A', 'N.A', '{} W'.format(p[3]), '{} VAR'.format(q[3]), '{} VAD'.format(d[3]), '{} VA'.format(s[3]), 'N.A', 'N.A', 'N.A', '{}'.format(fp[3]), '{} kWh'.format(result2[0]), '{} kVARh'.format(result2[1]), '$ {}'.format(result2[2]), '$ {}'.format(result2[3]), '$ {}'.format(result2[4])],
                        ]))
        ])
    
    # ===============================================================
    # ===============================================================
    if THD_V_A < 5:
        text_THD_V_A = 'Low deformation: low risk of failure.'
    elif 5 <= THD_V_A < 8:
        text_THD_V_A = 'Significant deformation: risk of overheating and malfunction.'
    elif THD_V_A >= 8:
        text_THD_V_A = 'High risk of failure and malfunction.'
    
    if THD_V_B < 5:
        text_THD_V_B = 'Low deformation: low risk of failure.'
    elif 5 <= THD_V_B < 8:
        text_THD_V_B = 'Significant deformation: risk of overheating and malfunction.'
    elif THD_V_B >= 8:
        text_THD_V_B = 'High risk of failure and malfunction.'
    
    if THD_V_C < 5:
        text_THD_V_C = 'Low deformation: low risk of failure.'
    elif 5 <= THD_V_C < 8:
        text_THD_V_C = 'Significant deformation: risk of overheating and malfunction.'
    elif THD_V_C >= 8:
        text_THD_V_C = 'High risk of failure and malfunction.'


    # ===============================================================
    if THD_I_A < 10:
        text_THD_I_A = 'Low harmonic currents: Low risk of failure.'
    elif 10 <= THD_I_A < 50:
        text_THD_I_A = 'Significant harmonic currents: risk of heating in conductors and equipment.'
    elif THD_I_A >= 50:
        text_THD_I_A = 'High risk harmonic currents: high probability of breakdowns and dangerous overheating.'
    
    if THD_I_B < 10:
        text_THD_I_B = 'Low harmonic currents: Low risk of failure.'
    elif 10 <= THD_I_B < 50:
        text_THD_I_B = 'Significant harmonic currents: risk of heating in conductors and equipment.'
    elif THD_I_B >= 50:
        text_THD_I_B = 'High risk harmonic currents: high probability of breakdowns and dangerous overheating.'

    if THD_I_C < 10:
        text_THD_I_C = 'Low harmonic currents: Low risk of failure.'
    elif 10 <= THD_I_C < 50:
        text_THD_I_C = 'Significant harmonic currents: risk of heating in conductors and equipment.'
    elif THD_I_C >= 50:
        text_THD_I_C = 'High risk harmonic currents: high probability of breakdowns and dangerous overheating.'



    tab2 = go.Figure(
        data=[go.Table(
            header=dict(
                values=[' ', 'Phase A', 'Phase B', 'Phase C']
                ),
            cells=dict(
                values=[['THD_V', 'THD_I'],
                        [text_THD_V_A, text_THD_I_A],
                        [text_THD_V_B, text_THD_I_B],
                        [text_THD_V_C, text_THD_I_C],
                        ]))
        ])

    return tab1, tab2
