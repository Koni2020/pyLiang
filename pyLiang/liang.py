"""
Created on 08 Jun 2023
Update on 08 Jun 2023
@author: Hanyu Jin
version: 1.0.0
Citation: X. San Liang, 2015: Normalizing the causality between time series. Phys. Rev. E 92, 022126.
"""

import numpy as np
from scipy.stats import norm
from collections import namedtuple

def causality_est(xx1: np.ndarray, xx2: np.ndarray, n=2, alpha=0.95) -> tuple[float, float, float, float]:
    '''
    Estimate T21, the information transfer from series X2 to series X1
    dt is taken to be 1.
    :param xx1: the series1
    :param xx2: the series2
    :param n: integer >=1, time advance in performing Euler forward
    :return: T21:  info flow from X2 to X1	(Note: Not X1 -> X2!)
             err90: standard error at 90% significance level
             err95: standard error at 95% significance level
             err99: standard error at 99% significance level
    '''

    res = namedtuple('Liang_Causality_Test', ['info', 'h', 'err', 'alpha'])

    dt = 1

    nm = xx1.size

    dx1 = (xx1[n:nm] - xx1[:(nm - n)]) / (n * dt)
    x1 = xx1[:(nm - n)]

    dx2 = (xx2[n:nm] - xx2[:(nm - n)]) / (n * dt)
    x2 = xx2[:(nm - n)]

    N = nm - n

    C = np.cov(x1, x2)

    dC = np.zeros((2, 2))
    dC[0, 0] = np.sum((x1 - np.mean(x1)) * (dx1 - np.mean(dx1)))
    dC[0, 1] = np.sum((x1 - np.mean(x1)) * (dx2 - np.mean(dx2)))
    dC[1, 0] = np.sum((x2 - np.mean(x2)) * (dx1 - np.mean(dx1)))
    dC[1, 1] = np.sum((x2 - np.mean(x2)) * (dx2 - np.mean(dx2)))
    dC = dC / (N - 1)

    C_infty = C

    detc = np.linalg.det(C)

    a11 = C[1, 1] * dC[0, 0] - C[0, 1] * dC[1, 0]
    a12 = -C[0, 1] * dC[0, 0] + C[0, 0] * dC[1, 0]

    a11 = a11 / detc
    a12 = a12 / detc

    f1 = np.mean(dx1) - a11 * np.mean(x1) - a12 * np.mean(x2)

    R1 = dx1 - (f1 + a11 * x1 + a12 * x2)

    Q1 = np.sum(R1 * R1)

    b1 = np.sqrt(Q1 * dt / N)

    NI = np.zeros((4, 4))
    NI[0, 0] = N * dt / (b1 * b1)
    NI[1, 1] = dt / (b1 * b1) * np.sum(x1 * x1)
    NI[2, 2] = dt / (b1 * b1) * np.sum(x2 * x2)
    NI[3, 3] = 3 * dt / (b1 * b1 * b1 * b1) * np.sum(R1 * R1) - N / (b1 * b1)
    NI[0, 1] = dt / (b1 * b1) * np.sum(x1)
    NI[0, 2] = dt / (b1 * b1) * np.sum(x2)
    NI[0, 3] = 2 * dt / (b1 * b1 * b1) * np.sum(R1)
    NI[1, 2] = dt / (b1 * b1) * np.sum(x1 * x2)
    NI[1, 3] = 2 * dt / (b1 * b1 * b1) * np.sum(R1 * x1)
    NI[2, 3] = 2 * dt / (b1 * b1 * b1) * np.sum(R1 * x2)

    NI[1, 0] = NI[0, 1]
    NI[2, 0] = NI[0, 2]
    NI[2, 1] = NI[1, 2]
    NI[3, 0] = NI[0, 3]
    NI[3, 1] = NI[1, 3]
    NI[3, 2] = NI[2, 3]

    invNI = np.linalg.inv(NI)
    var_a12 = invNI[2, 2]

    T21 = C_infty[0, 1] / C_infty[0, 0] * (-C[1, 0] * dC[0, 0] + C[0, 0] * dC[1, 0]) / detc

    var_T21 = (C_infty[0, 1] / C_infty[0, 0]) ** 2 * var_a12

    z_alpha = norm.ppf((1 + alpha) / 2)
    err = np.sqrt(var_T21) * z_alpha
    err1 = T21 - err
    err2 = T21 + err
    if err2 < 0 or err1 > 0:
        h = True
    else:
        h = False

    return res(T21, h, err, alpha)
