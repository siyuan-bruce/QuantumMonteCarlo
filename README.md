## FinQMC: A Quantum Monte Carlo Framework for Business Practitioners
FinQMC is a quantum Monte Carlo framework tailored for business practitioners who want to explore the potential of quantum computing for financial modeling. The primary contribution of this research is to establish a user-friendly software tool that enables financial analysts to experiment with quantum Monte Carlo methods without needing to be experts in quantum computing or computer programming.

## Getting Started

**The easiest way to get started is to run the main script:**

```bash
python main.py
```

This will automatically:
- ✅ Check for required Python packages
- ✅ Install any missing dependencies
- ✅ Run all example applications
- ✅ Display results and a summary

The script will execute all four example applications:
1. **Quantum Walk** - Demonstrates quantum walk with direct measurement
2. **Option Pricing** - European call option pricing using quantum amplitude estimation
3. **Portfolio Selection** - Portfolio optimization with multiple quantum operations
4. **Distribution Addition** - Distribution addition example

For more details on installation and manual setup, see the [Installation](#installation) section below.

### Features
- A simple and intuitive interface that allows users to specify financial models using familiar mathematical notation.
- Support for a wide range of probability distributions commonly used in financial modeling.
- The ability to simulate complex financial scenarios with high accuracy using quantum Monte Carlo methods.

### Requirements
- Python 3.7 or higher
- NumPy, SciPy, and Matplotlib libraries
- qiskit, a Python-based quantum computing library

### Package Versions

The following package versions have been tested and are recommended for this project. Most packages use the latest stable versions:

| Package | Version | Status |
|--------|--------|--------|
| Python | 3.7+ (tested with 3.11) | Required |
| NumPy | 1.26.4 | Latest |
| SciPy | 1.16.2 | Latest |
| Matplotlib | 3.10.6 | Latest |
| qiskit | 1.4.2 | Latest |
| qiskit-finance | 0.4.1 | Latest |
| qiskit-aer | 0.17.0 | Latest |
| qiskit-optimization | 0.6.1 | Latest |
| qiskit-algorithms | 0.3.1 | Latest |

**Note:** These versions represent the latest stable releases at the time of documentation. The framework should work with newer versions, but compatibility is guaranteed for the versions listed above.

To install the exact versions:
```bash
pip install numpy==1.26.4 scipy==1.16.2 matplotlib==3.10.6
pip install qiskit==1.4.2 qiskit-finance==0.4.1 qiskit-aer==0.17.0
pip install qiskit-optimization==0.6.1 qiskit-algorithms==0.3.1
```

### Project Structure
```
QuantumMonteCarlo/
├── src/
│   └── QuantumMC/              # Main source code package
│       ├── __init__.py
│       ├── quantummc.py        # Main QuantumMC class
│       ├── variable.py         # Quantum Variable module
│       ├── QArithmetic.py      # Quantum Arithmetic operations
│       ├── arithmetic.py        # Arithmetic utilities
│       ├── distribution.py      # Probability distributions
│       ├── quantumwalk.py      # Quantum Walk module
│       ├── estimation.py        # Quantum Estimation module
│       ├── qft.py              # Quantum Fourier Transform
│       └── error.py            # Error handling
├── applications/               # Example applications
│   ├── quantum_walk.py         # Quantum walk example
│   ├── quantum_walk_config.json # Quantum walk hyperparameters
│   ├── option_pricing.py       # European call option pricing
│   ├── option_pricing_config.json # Option pricing hyperparameters
│   ├── portfolio_selection.py  # Portfolio optimization example
│   ├── portfolio_selection_config.json # Portfolio selection hyperparameters
│   ├── distribution_addition.py # Distribution addition example
│   └── distribution_addition_config.json # Distribution addition hyperparameters
├── main.py                     # Main runner script (runs all applications)
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup script
├── setup.cfg                   # Setup configuration
├── pyproject.toml              # Project metadata
├── LICENSE                     # License file
└── README.md                   # This file
```

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

### Quick Start (Recommended)

Simply run the main script from the project root:

```bash
python main.py
```

The script handles everything automatically - no manual installation needed!

### Manual Installation

If you prefer to install dependencies manually:

You can install the Quantum Monte Carlo Library using pip:

```bash
pip install -r requirements.txt
```

Or install the package directly:

```bash
pip install -e .
```

## Usage

### Running Applications

**Option 1: Run all applications at once (Recommended)**
```bash
python main.py
```

**Option 2: Run individual applications**
```bash
# From the project root directory
python applications/quantum_walk.py
python applications/option_pricing.py
python applications/portfolio_selection.py
python applications/distribution_addition.py
```

### Code Examples

Here is an example of how to use the Quantum Monte Carlo Library to do addition using a quantum circuit:
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

## Hyperparameter Reporting

This section provides detailed hyperparameter settings for each application/case study to ensure reproducibility. Configuration files for each application are available in the `applications/` directory.

### Table: Hyperparameter Settings by Application

| Parameter Category         | Distribution Addition | Quantum Walk | Portfolio Selection |
|---------------------------|----------------------|--------------|---------------------|
| **Encoding/Precision**    |                      |              |                     |
| Uncertainty qubits per variable | 1 (per step)         | 1 (per step)   | 1 (per walk step)    |
| Total qubits (final variable)   | 3                    | 3            | Variable (depends on operations) |
| Discretization bounds     | (0, 1)               | (0, 1)       | (0, 1)              |
| **Distribution Parameters**     |                      |              |                     |
| Distribution type         | Normal               | Normal       | Normal (2 walks)     |
| μ (mean)                  | 0.5                  | 0.5          | 0.5 (both)           |
| σ (std dev)               | 1.0                  | 1.0          | 1.0 (both)           |
| **Path/Walk Configuration**     |                  |              |                     |
| Number of steps           | 3                    | 3            | 1 (per walk)         |
| State space size          | 1                    | 1            | 1                    |
| Walk name                 | "r"                  | "r"          | "r", "xi"            |
| **Amplitude Estimation (QAE)**  |                  |              |                     |
| Target accuracy (ε)       | N/A                  | N/A          | 0.01                 |
| Confidence level (α)      | N/A                  | N/A          | 0.01                 |
| Iterations/repetitions    | N/A                  | N/A          | Auto-selected        |
| **Arithmetic/Register Options** |              |              |                     |
| Padding policy            | N/A                  | N/A          | Mixed<sup>3</sup>    |
| Operations performed      | N/A                  | N/A          | add, power2, sub, mult |
| **Objective Function (if applicable)** |       |              |                     |
| Rescaling factor (c_approx)    | N/A              | N/A          | N/A<sup>4</sup>      |
| Image                     | Yes                  | Yes          | Yes                  |
| **Execution Details**           |                  |              |                     |
| Backend/Simulator         | qasm_simulator       | qasm_simulator | AerSimulator         |
| Shot count                | 1000                 | 1000         | 1000                 |


### Additional Details

**Option Pricing Application (Following Rebentrost et al. 2024):**
- Initial spot price (S): 2.0
- Volatility (vol): 0.4 (40%)
- Annual interest rate (r): 0.05 (5%)
- Time to maturity (T): 40/365 days
- Strike price: 1.896
- Distribution parameters: μ = (r - 0.5*vol²)*T + ln(S), σ = vol*√T

**Portfolio Selection Application:**
- Constant variable: 1 qubit, value = 1
- Operations sequence: add (pad=True) → add (pad=False) → power2 → sub → mult
- Final estimation on result of multiplication

**Quantum Walk & Distribution Addition Applications:**
- Both use direct measurement (no QAE)
- Results obtained via classical post-processing of measurement counts

### Configuration Files

Each application has a corresponding configuration file in the `applications/` directory:
- `quantum_walk_config.json` - Quantum walk hyperparameters
- `option_pricing_config.json` - Option pricing hyperparameters  
- `portfolio_selection_config.json` - Portfolio selection hyperparameters
- `distribution_addition_config.json` - Distribution addition hyperparameters

### Version Information

The project has been tested with the following software versions:
- **Python**: 3.7+ (tested with 3.11)
- **Backend**: qiskit Aer (qasm_simulator or AerSimulator)
- **Operating System**: OS Independent (tested on macOS, Linux, Windows)

All package dependencies and their versions are listed in the [Package Versions](#package-versions) section above. The main runner script (`main.py`) will automatically check for and install the required packages if they are missing.

### Contribution Guidelines
We welcome contributions to FinQMC from the community. If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.

### License
This software is released under the MIT License. See LICENSE.txt for details.