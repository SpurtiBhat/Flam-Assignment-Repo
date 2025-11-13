import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Read data
data = np.loadtxt('points.csv', delimiter=',', skiprows=1)
x_data, y_data = data[:,0], data[:,1]
t = np.linspace(6, 60, len(x_data))

# Parametric functions
def x_func(t, theta, M, X):
    return t*np.cos(theta) - np.exp(M*np.abs(t))*np.sin(0.3*t)*np.sin(theta) + X

def y_func(t, theta, M, X):
    return 42 + t*np.sin(theta) + np.exp(M*np.abs(t))*np.sin(0.3*t)*np.cos(theta)

# Combined model for curve_fit
def model(t, theta, M, X):
    x_model = x_func(t, theta, M, X)
    y_model = y_func(t, theta, M, X)
    return np.concatenate((x_model, y_model))

combined_data = np.concatenate((x_data, y_data))
initial_guess = [0.5, -0.05, 55]
popt, _ = curve_fit(model, np.tile(t, 2), combined_data, p0=initial_guess)

theta_opt, M_opt, X_opt = popt
np.savetxt('fitted_params.txt', [popt], header='theta, M, X', fmt='%.8f', delimiter=',')

# Plot
plt.figure(figsize=(7,5))
plt.plot(x_data, y_data, 'o', label='Data points')
plt.plot(x_func(t, *popt), y_func(t, *popt), '-', label='Fitted curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Curve fitting result')
plt.grid(True)
plt.savefig('fitted_curve.png', dpi=300)
plt.show()
