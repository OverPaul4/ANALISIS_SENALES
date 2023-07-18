"""
this script returns the cost of energy taking into account both active and reactive power.

Last modification:
                Day: 13
                Month: May
                Year:2023

Author:
        Over Paul Perez
        Dilan Valencia

Technological University of Pereira
"""


def energy(p, q, cost_p, cost_q, time):
    """
    this function returns the cost of energy taking into account both active and reactive power.
    :param p: Total active power at node.
    :param q: Total reactive power at node.
    :param cost_p: Active energy cost.
    :param cost_q: Reactive energy cost.
    :param time: Time interval.
    :return: List.
    """
    energy_p = p * float(time) / 1000
    energy_q = q * float(time) / 1000

    pay_p = energy_p * float(cost_p)

    pay_q = 0
    if abs(energy_q) > energy_p / 2:

        pay_q = (abs(energy_q) - energy_p / 2) * float(cost_q)

    pay_total = pay_p + pay_q

    return [round(energy_p, 4), round(energy_q, 4), round(pay_p, 2), round(pay_q, 2), round(pay_total, 2)]
