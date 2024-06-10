import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data for longitudinal field
I_longitudinal = np.array([4.25, 4.55, 4.85, 5.00, 5.25, 5.40, 4.75])
U_longitudinal = np.array([750, 850, 950, 1050, 1150, 1250, 900])
I2_longitudinal = I_longitudinal**2

# Data for transverse field
I_transverse = np.array([1.4, 1.3, 1.2, 1.15, 1.05, 0.85, 0.95, 1.1])
U_transverse = np.array([220, 200, 180, 160, 130, 100, 110, 146])
I2_transverse = I_transverse**2


# Define linear function for fitting
def linear_fit(I2, a):
    return a * I2


# Fit the longitudinal data
popt_long, pcov_long = curve_fit(linear_fit, I2_longitudinal, U_longitudinal)
a_long = popt_long[0]
error_long = np.sqrt(np.diag(pcov_long))[0]

# Fit the transverse data
popt_trans, pcov_trans = curve_fit(linear_fit, I2_transverse, U_transverse)
a_trans = popt_trans[0]
error_trans = np.sqrt(np.diag(pcov_trans))[0]

# Calculate specific charge e/me
e_me_long = a_long * 8
e_me_trans = a_trans * 8

# Print results
print(f"Longitudinal field: e/me = {e_me_long:.2f} C/kg, error = {error_long:.2f}")
print(f"Transverse field: e/me = {e_me_trans:.2f} C/kg, error = {error_trans:.2f}")

# Plot the results
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(I2_longitudinal, U_longitudinal, label="Data")
plt.plot(
    I2_longitudinal, linear_fit(I2_longitudinal, *popt_long), color="red", label="Fit"
)
plt.xlabel("$I^2$ (A$^2$)")
plt.ylabel("U (V)")
plt.title("Longitudinal Magnetic Field")
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(I2_transverse, U_transverse, label="Data")
plt.plot(
    I2_transverse, linear_fit(I2_transverse, *popt_trans), color="red", label="Fit"
)
plt.xlabel("$I^2$ (A$^2$)")
plt.ylabel("U (V)")
plt.title("Transverse Magnetic Field")
plt.legend()

plt.tight_layout()
plt.show()
