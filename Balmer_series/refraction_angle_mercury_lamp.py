import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Data: (colour_id, wavelength in nm, d1 in degrees, d2 in degrees, phi in degrees)
data = [
    ("green 546", 546, 69.37277778, 166.4561111, 48.54166667),
    ("oran577", 577, 69.695, 166.1494444, 48.22722222),
    ("oran579", 579, 69.71333333, 166.1294444, 48.20805556),
    ("cyan491", 491, 68.66055556, 167.1511111, 49.24527778),
    ("blu435", 435, 67.57555556, 168.2377778, 50.33111111),
    ("vio407", 407, 66.81388889, 169.0011111, 51.09361111),
    ("vio404", 404, 66.72666667, 169.0955556, 51.18444444),
    ("red690", 690, 70.43166667, 165.3694444, 47.46888889),
    ("red623", 623, 70.03111111, 165.7833333, 47.87611111),
    ("red607", 607, 69.94888889, 165.8672222, 47.95916667)
]

# Convert to numpy arrays for easier manipulation
wavelengths = np.array([item[1] for item in data]) #ITEM[1]=546....607
phi_values = np.array([item[4] for item in data])
errors = np.full(len(wavelengths), 0.43602214)  # CALCULATED STANDARD error value fROM EXCEL

# Define the dispersion relation
def dispersion_relation(lambda_, n_n, lambda_n, C):
    return n_n + C / (lambda_ - lambda_n)

# Perform the curve fit
popt, pcov = curve_fit(dispersion_relation, wavelengths, phi_values, sigma=errors, maxfev=10000)

# Extract fitted parameters
n_n, lambda_n, C = popt
print(f"Fitted parameters: n_n={n_n}, lambda_n={lambda_n}, C={C}")

# Generate data for the fit line
fit_wavelengths = np.linspace(min(wavelengths), max(wavelengths), 1000)
fit_refractive_indices = dispersion_relation(fit_wavelengths, *popt)

# Plot the data with error bars
plt.errorbar(wavelengths, phi_values, yerr=errors, fmt='o', label='Measured Data', ecolor='r', capsize=5)

# Plot the fit line
plt.plot(fit_wavelengths, fit_refractive_indices, label='Dispersion Relation Fit', color='blue')

# Adding labels and legend
plt.xlabel('Wavelength (nm)')
plt.ylabel('Refractive Index (phi)')
plt.title('Refractive Index vs. Wavelength with Dispersion Relation Fit')
plt.legend()

# Show the plot
plt.show()