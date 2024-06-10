import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data for longitudinal field
I_long = np.array([4.25, 4.55, 4.85, 5.0, 5.25, 5.4, 4.75])
U_long = np.array([750, 850, 950, 1050, 1150, 1250, 900])
I2_long = I_long ** 2
U_long_err = np.sqrt(66.11163513)
I2_long_err = np.sqrt(1.45117131)

# Linear fit function
def linear_fit(x, m):
    return m * x

# Fit the line
params_long, covariance_long = curve_fit(linear_fit, I2_long, U_long)
slope_long = params_long[0]
fit_line_long = linear_fit(I2_long, slope_long)

# Constants
mu_0 = 4 * np.pi * 1e-7  # T·m/A
N = 130  # number of turns
l = 0.381  # m
z = 0.249 #m

# Specific charge e/me for longitudinal field
specific_charge_long = slope_long * 8 * ((np.pi * l )/ (mu_0 * N * z))**2
print(f'Specific charge (e/me) for longitudinal field: {specific_charge_long:.2e} C/kg')

# Plot U vs I^2 for longitudinal field
plt.figure(figsize=(10, 5))
plt.errorbar(I2_long, U_long, yerr=U_long_err, xerr=I2_long_err, fmt='o', label='Data with error bars', ecolor='r', capsize=5)
plt.plot(I2_long, fit_line_long, label=f'Fit line: $U = {slope_long:.2e} \cdot I^2$', color='g')
plt.xlabel('$I^2$ (A²)')
plt.ylabel('$U$ (V)')
plt.title('Longitudinal Field: $U$ vs $I^2$ with Fit Line and Error Bars')
plt.legend()
plt.grid(True)
plt.show()


