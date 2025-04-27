# some_file.py
import sys
import os

sys.path.append('src/')
sys.path.append('../src/')

from QuantumMC.quantummc import QuantumMC
from QuantumMC.variable import Variable

import numpy as np
import qiskit

# Create an instance of the QuantumMC class and assign it to the variable qmc
qmc = QuantumMC()

# Generate a random walk with the specified parameters and assign it to the variable qw1
qw1 = qmc.walk(num_steps = 1, distribution = "Normal", size = 1, name = "r", mu = 0.5, sigma = 1, bounds = (0, 1))

# Generate a second random walk with different parameters and assign it to the variable qw2
qw2 = qmc.walk(num_steps = 1, distribution = "Normal", size = 1, name = "xi", mu = 0.5, sigma = 1, bounds = (0, 1))

# Perform an addition operation on the last element of the vars attribute of qw1 and qw2, and assign the result to the variables a and b
a, b = qmc.arithmetic("add", [qw1.vars[-1], qw2.vars[-1]])

# Create a variable with a size of 1 and a type of "constant", and assign it to the variable var
var = Variable(1, "constant")

# Load a constant value of 1 into the var variable
var.load_constant(1)

# Add the var variable to the list of variables in the qmc object
qmc.add_variable(var)

# Perform an addition operation on the var variable and the b variable, and assign the result to the variables a and b
a, b = qmc.arithmetic("add", [var, b], pad = False)

# Perform a power-of-2 operation on the b variable and assign the result to the variables a and b
a, b = qmc.arithmetic("power2", [b])

a, b = qmc.arithmetic("sub", [b, var])
# Perform a multiplication operation on the first element of the vars attribute of qw1 and the b variable, and assign the result to the variables a, b, and c
a, b, c = qmc.arithmetic("mult", [qw1.vars[0], b])

# Estimate the value of the c variable using Monte Carlo sampling, with the specified error tolerances, and assign the result to the variable result
result = qmc.estimate(0.01, 0.01, c)

print(result)