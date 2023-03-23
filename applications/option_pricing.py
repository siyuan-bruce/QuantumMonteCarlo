'''
This module is following the work from Rebentrostet al. 2018, Stamatopoulos et al. 2020.
'''

from QuantumMC.quantummc import QuantumMC
from QuantumMC.variable import Variable
import numpy as np

from qiskit.circuit.library import LinearAmplitudeFunction
# number of qubits to represent the uncertainty
num_uncertainty_qubits = 3

# parameters for considered random distribution
S = 2.0  # initial spot price
vol = 0.4  # volatility of 40%
r = 0.05  # annual interest rate of 4%
T = 40 / 365  # 40 days to maturity

mu = (r - 0.5 * vol**2) * T + np.log(S)
sigma = vol * np.sqrt(T)
mean = np.exp(mu + sigma**2 / 2)
variance = (np.exp(sigma**2) - 1) * np.exp(2 * mu + sigma**2)
stddev = np.sqrt(variance)

# lowest and highest value considered for the spot price; in between, an equidistant discretization is considered.
low = np.maximum(0, mean - 3 * stddev)
high = mean + 3 * stddev

# set the strike price (should be within the low and the high value of the uncertainty)
strike_price = 1.896

# set the approximation scaling for the payoff function
c_approx = 0.25

# setup piecewise linear objective fcuntion
breakpoints = [low, strike_price]
slopes = [0, 1]
offsets = [0, 0]
f_min = 0
f_max = high - strike_price
european_call_objective = LinearAmplitudeFunction(
    num_uncertainty_qubits,
    slopes,
    offsets,
    domain=(low, high),
    image=(f_min, f_max),
    breakpoints=breakpoints,
    rescaling_factor=c_approx,
)

qmc = QuantumMC() #Initialization
final_price = Variable(num_uncertainty_qubits)
final_price.load_distribution("LogNormal", num_uncertainty_qubits, mu=mu, sigma=sigma**2, bounds = (low, high))
qmc.add_variable(final_price)
result = qmc.estimate(0.05, 0.01, final_price, objective = european_call_objective)
print(result)