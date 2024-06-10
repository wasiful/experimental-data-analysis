import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data for transverse field
I_trans = np.array([1.4, 1.3, 1.2, 1.15, 1.05, 0.85, 0.95, 1.1])
U_trans = np.array([220, 200, 180, 160, 130, 100, 110, 146])
I2_trans = I_trans**2
U_trans_err = np.sqrt(15.0306235)
I2_trans_err = np.sqrt(0.143060458)


# Linear fit function
def linear_fit(x, m):
    return m * x


# Fit the line
params_trans, covariance_trans = curve_fit(linear_fit, I2_trans, U_trans)
slope_trans = params_trans[0]
fit_line_trans = linear_fit(I2_trans, slope_trans)

# Constants
mu_0 = 4 * np.pi * 1e-7  # T·m/A
d = 0.099  # m
R = 0.15  # m
N = 130  # number of turns

# Specific charge e/me for transverse field
specific_charge_trans = (
    slope_trans * 8 / (d**2 * (8 / (5 * np.sqrt(5)) * mu_0 * N / R) ** 2)
)
print(f"Specific charge (e/me) for transverse field: {specific_charge_trans:.2e} C/kg")

# Plot U vs I^2 for transverse field
plt.figure(figsize=(10, 5))
plt.errorbar(
    I2_trans,
    U_trans,
    yerr=U_trans_err,
    xerr=I2_trans_err,
    fmt="o",
    label="Data with error bars",
    ecolor="r",
    capsize=5,
)
plt.plot(
    I2_trans,
    fit_line_trans,
    label=f"Fit line: $U = {slope_trans:.2e} \cdot I^2$",
    color="g",
)
plt.xlabel("$I^2$ (A²)")
plt.ylabel("$U$ (V)")
plt.title("Transverse Field: $U$ vs $I^2$ with Fit Line and Error Bars")
plt.legend()
plt.grid(True)
plt.show()
