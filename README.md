## FinQMC: A Quantum Monte Carlo Framework for Business Practitioners
FinQMC is a quantum Monte Carlo framework tailored for business practitioners who want to explore the potential of quantum computing for financial modeling. The primary contribution of this research is to establish a user-friendly software tool that enables financial analysts to experiment with quantum Monte Carlo methods without needing to be experts in quantum computing or computer programming.

### Features
- A simple and intuitive interface that allows users to specify financial models using familiar mathematical notation.
- Support for a wide range of probability distributions commonly used in financial modeling.
- The ability to simulate complex financial scenarios with high accuracy using quantum Monte Carlo methods.

### Requirements
- Python 3.7 or higher
- NumPy, SciPy, and Matplotlib libraries
- qiskit, a Python-based quantum computing library


#### Introduction to FinQMC Modules
The framework is composed of several modules that work together to provide a comprehensive suite of tools for quantum computing:

#### Quantum Variable
The Quantum Variable module allows users to define quantum variables and assign either constant or distribution-based values. This module provides a flexible and intuitive way to define the inputs for the QMC simulation.

#### Quantum Arithmetic
The Quantum Arithmetic module provides efficient operations between any two variables. This module enables business practitioners to perform complex calculations involving quantum variables, without needing a deep understanding of the underlying quantum mechanics.

#### Quantum Walk
The Quantum Walk module simplifies the sampling and accumulation process. This module enables users to efficiently simulate the QMC process, by handling the necessary steps involved in quantum walks.

#### Quantum Estimation
The Quantum Estimation module calculates expected values or the minimum values within a distribution. This module provides a reliable and accurate way to estimate the outcomes of QMC simulations, enabling users to make informed business decisions based on the results.

## Installation
You can install the Quantum Monte Carlo Library using pip:

## Usage
Here is an example of how to use the Quantum Monte Carlo Library to do addtion using a quantum circuit:
```python
from QuantumMC.quantummc import QuantumMC
from QuantumMC.variable import Variable
qmc = QuantumMC()

# Define two quantum variables with constant values
var1 = Variable(2, "var1")
var1.load_constant(2)
var2 = Variable(2, "var2")
var2.load_constant(1)
qmc.add_variable(var1)
qmc.add_variable(var2)

# Add the two variables using QuantumArithmetic module
a, b = qmc.arithmetic("add", [var1, var2])
```

### Variable Definition and Distribution Loading
The log-normal quantum distribution can be represented as:
$$
\ket{f(x)} = \sum_{i=0}^{2^{n}-1} \frac{1}{\sqrt{x_i \sigma \sqrt{2\pi}}} \exp\!\left(-\frac{(\log(x_i) - \mu)^2}{2\sigma^2}\right) \ket{x_i}
$$
where \(x_i\) is the \(i\)th value of the distribution and \(n\) is the number of qubits. The amplitude of the quantum state is the square root of its measurement probability.

```python
from QuantumMC.variable import Variable
final_price = Variable(num_qubits, name="variable")
final_price.load_distribution("LogNormal", num_uncertainty_qubits, mu=mu, sigma=sigma**2, bounds=(low, high))
```
The second line creates a distribution variable object called `final_price` with `num_uncertainty_qubits` qubits and a `variable` name. The third line loads a log-normal distribution onto the `final_price` variable with the specified parameters.

### Quantum Arithmetic
```python
from QuantumMC.quantummc import QuantumMC
from QuantumMC.variable import Variable
qmc = QuantumMC()
var1 = Variable(2, "var1")
var1.load_constant(2)
var2 = Variable(2, "var2")
var2.load_constant(1)
qmc.add_variable(var1)
qmc.add_variable(var2)
a, b = qmc.arithmetic("add", [var1, var2])
```
Lines 4–9 create two constant variables and add them to the `qmc` framework. Two qubits represent values up to 3, so the constant is set to 2. Line 10 performs the addition.

### Quantum Walk
```python
qmc = QuantumMC()
qw = qmc.walk(num_steps=1, distribution="Normal", size=1, name="r", mu=0.1, sigma=0.05)
```
The second line initializes the quantum walk object with the number of steps, distribution, and related parameters.

### Quantum Estimation
```python
qmc = QuantumMC()
result = qmc.estimate(0.05, 0.01, var)  # choose any variable to estimate
```
This starts the estimation technique on a chosen variable.

### Contribution Guidelines
We welcome contributions to FinQMC from the community. If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.

### License
This software is released under the MIT License. See LICENSE.txt for details.