"""
This script calculates the active power, reactive power, apparent power and power factor of a system with harmonics.
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
from scipy.fft import rfft


def power(voltage, current, N=100):
    """
    This function calculates active power, reactive power, apparent power and power factor of a system with harmonics.
    :param voltage: Voltage matrix.
    :param current: Current matrix.
    :param N: Discrete period.
    :return: P, Q, S, D, fp and harmonics.
    """
    
    list_p = list()
    list_q = list()
    list_s = list()
    list_d = list()
    list_fp = list()
    list_harmonic = [[], [], []]
    list_harmonic_info = [[], [], []]
    list_phase_diagram_v = [[], [], []]
    list_phase_diagram_i = [[], [], []]
    list_vrms = list()
    list_irms = list()
    list_vrms_info = list()
    list_irms_info = list()
    list_info = list()
    list_info2 = list()
    list_info3 = list()

    for i in range(3):
        v_f, i_f = rfft(voltage[i][:N], norm="forward"), rfft(current[i][:N], norm="forward") 

        p = 0
        q = 0
        vrms = 0
        irms = 0
        harmonic = 1

        list_vrms_info.clear()
        list_irms_info.clear()

        for j, k in zip(v_f[1:], i_f[1:]):
            An_v = 2 * np.abs(j)
            An_i = 2 * np.abs(k)

            if An_v > 0.01 or An_i > 0.01:
                list_info.clear()
                list_info2.clear()
                list_info3.clear()

                ter1 = (An_v / np.sqrt(2)) * (An_i / np.sqrt(2))
                p = + p + ter1 * np.cos(np.angle(j) - np.angle(k))
                q = + q + ter1 * np.sin(np.angle(j) - np.angle(k))
                vrms = vrms + np.power(An_v / np.sqrt(2), 2)  # Estan al cuadrado
                irms = irms + np.power(An_i / np.sqrt(2), 2)  # Estan al cuadrado

                list_harmonic[i].append(harmonic)

                # Add information for each harmonic
                vrms_harmonic = np.round(An_v / np.sqrt(2), 3)
                irms_harmonic = np.round(An_i / np.sqrt(2), 3)
                p_harmonic = np.round(ter1 * np.cos(np.angle(j) - np.angle(k)), 3)
                q_harmonic = np.round(ter1 * np.sin(np.angle(j) - np.angle(k)), 3)
                s_harmonic = np.round(vrms_harmonic * irms_harmonic, 3)
                # d_harmonic = np.round(np.sqrt(np.abs(np.square(s_harmonic) - np.square(p_harmonic) - np.square(q_harmonic))), 3)
                fp_harmonic = np.round(p_harmonic / s_harmonic, 3)
                list_info.extend([harmonic, vrms_harmonic, irms_harmonic, p_harmonic, q_harmonic, s_harmonic, fp_harmonic]) 
                list_harmonic_info[i].append(list_info.copy())

                # Add information for phasor diagrams
                list_info2.extend([harmonic, An_v / np.sqrt(2), np.degrees(np.angle(j))])
                list_phase_diagram_v[i].append(list_info2.copy())
                list_info3.extend([harmonic, An_i / np.sqrt(2), np.degrees(np.angle(k))])
                list_phase_diagram_i[i].append(list_info3.copy())

                # Valores RMS
                list_vrms_info.append(vrms_harmonic)
                list_irms_info.append(irms_harmonic)
  
            harmonic += 1

        # Adicionando valores RMS
        list_vrms.append(list_vrms_info.copy())
        list_irms.append(list_irms_info.copy())  
        
        s = np.sqrt(vrms) * np.sqrt(irms)
        d = np.sqrt(np.abs(np.square(s) - np.square(p) - np.square(q)))
        fp = p / s

        list_p.append(p)
        list_q.append(q)
        list_s.append(s)
        list_d.append(d)
        list_fp.append(fp)

    p_total = np.sum(list_p)
    q_total = np.sum(list_q)
    d_total = np.sum(list_d)

    s_total =np.sqrt(np.abs(np.square(p_total) + np.square(q_total) + np.square(d_total)))
    fp_equivalent = p_total / s_total

    list_p.append(p_total)
    list_q.append(q_total)
    list_s.append(s_total)
    list_d.append(d_total)
    list_fp.append(fp_equivalent)

    list_p = np.round(np.array(list_p), 3)
    list_q = np.round(np.array(list_q), 3)
    list_s = np.round(np.array(list_s), 3)
    list_d = np.round(np.array(list_d), 3)
    list_fp = np.round(np.array(list_fp), 3)
    # list_harmonic = np.round(np.array(list_harmonic), 2)

    return list_p, list_q, list_d, list_s, list_fp, list_harmonic, list_harmonic_info, list_phase_diagram_v, list_phase_diagram_i, list_vrms, list_irms
    
