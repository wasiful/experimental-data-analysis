import statistics

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Given constants
eta = 1.8e-5  # Pa·s
rho_oil = 874  # kg/m³
rho_air = 1.225  # kg/m³
g = 9.81  # m/s²
d = 0.006  # m
A = (6.18e-5) / 0.765  # m

# Data from the table
U = np.array(
    [
        495,
        500,
        496,
        495,
        495,
        495,
        495,
        492,
        488,
        488,
        480,
        482,
        480,
        482,
        476,
        478,
        478,
    ]
)
t_rise = np.array(
    [
        6.32,
        7.96,
        12.07,
        9.01,
        13.2,
        13.81,
        5.3,
        8.45,
        8.32,
        9.58,
        24.14,
        6.63,
        9.36,
        7.42,
        12.11,
        5.56,
        8.87,
    ]
)
t_fall = np.array(
    [
        18.87,
        16.14,
        20.05,
        15.12,
        8.27,
        18,
        11.35,
        24.5,
        14.97,
        24,
        3.75,
        11.38,
        9.57,
        11.83,
        19.61,
        16.96,
        6.3,
    ]
)
distance = np.array(
    [20, 20, 20, 20, 20, 20, 20, 30, 20, 20, 20, 20, 20, 20, 20, 20, 20]
) * (6 / 120)  # Convert divisions to mm

# Calculate velocities
v_k = distance / t_fall
v_s = distance / t_rise

# Calculate radius r
r = np.sqrt((9 * eta * v_k/100) / (2 * g * (rho_oil - rho_air)))

# Calculate f_c
f_c = 1 + (A / r)

# Calculate charge Q
Q = (d / U) * ((6 * np.pi * eta * (v_k/100 + v_s/100) * r)/ (f_c ** (3 / 2)))
print(f"Q={Q}")
print(f"Average Charge of the electron ={np.mean(Q)}" )

# Calculate standard error for Q
Q_err = Q * np.sqrt(
    (0.002 / d) ** 2 + (0.01 / U) ** 2 + (0.01 / v_k) ** 2 + (0.01 /v_s) ** 2
)
print(f"the average error is = {np.mean(Q_err)} ")

# average_q_err = statistics.mean(
#     [
#         6.35732935e-13,
#         4.99513741e-13,
#         4.70736851e-13,
#         4.63792630e-13,
#         4.42424600e-13,
#         4.36789368e-13,
#         5.09658196e-13,
#         6.21172130e-13,
#         4.83092764e-13,
#         5.91234097e-13,
#         1.11768263e-12,
#         4.74089988e-13,
#         4.24727271e-13,
#         4.62213908e-13,
#         4.85227643e-13,
#         6.62411620e-13,
#         4.43226030e-13,
#     ]
# )
# print(f"average error is ={average_q_err}")

average_specific_charge = np.mean([2.88 * 10**11, 1.60* 10**11])
print (f"average specific charge is = {average_specific_charge}")
#2.24*10**11
print (f"average mass of the electron = {np.mean(Q) / average_specific_charge}")


# Linear fit function
def linear_fit(x, m, b):
    return m * x + b


# Fit the line
params, covariance = curve_fit(linear_fit, r, Q)
slope, intercept = params
fit_line = linear_fit(r, slope, intercept)

# Plot Q vs r with error bars and fit line
plt.figure(figsize=(10, 5))
plt.errorbar(
    r, Q, yerr=Q_err, fmt="o", label="Data with error bars", ecolor="r", capsize=5
)
plt.plot(
    r, fit_line, label=f"Fit line: $Q = {slope:.2e}r + {intercept:.2e}$", color="g"
)
plt.xlabel("Radius $r$ (m)")
plt.ylabel("Charge $Q$ (C)")
plt.title("Charge $Q$ vs Radius $r$")
plt.legend()
plt.grid(True)
plt.show()
