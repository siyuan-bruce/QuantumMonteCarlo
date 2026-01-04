# Hyperparameter Summary Table

This document provides a compact reference table of all hyperparameters for each application, suitable for inclusion in papers or documentation.

## Complete Hyperparameter Table

| Parameter | Quantum Walk | Option Pricing | Portfolio Selection | Distribution Addition |
|-----------|--------------|----------------|---------------------|----------------------|
| **Encoding/Precision** |
| Uncertainty qubits | 1 (per step) | 3 | 1 (per walk) | 1 (per step) |
| Total qubits (final) | 3 | 3 | Variable | 3 |
| Discretization bounds | (0, 1) | (1.2086, 2.8134) | (0, 1) | (0, 1) |
| **Distribution** |
| Type | Normal | LogNormal | Normal | Normal |
| μ | 0.5 | 0.6899 | 0.5 | 0.5 |
| σ | 1.0 | 0.1324 | 1.0 | 1.0 |
| **Path/Walk** |
| Num steps | 3 | N/A | 1 | 3 |
| State space size | 1 | N/A | 1 | 1 |
| **QAE Parameters** |
| Used | No | Yes | Yes | No |
| ε (accuracy) | N/A | 0.05 | 0.01 | N/A |
| α (confidence) | N/A | 0.01 | 0.01 | N/A |
| Iterations | N/A | Auto | Auto | N/A |
| **Arithmetic** |
| Padding | N/A | Default | Mixed | N/A |
| Operations | N/A | N/A | add, power2, sub, mult | N/A |
| **Objective Function** |
| c_approx | N/A | 0.25 | 0.1 (default) | N/A |
| **Execution** |
| Backend | qasm_simulator | AerSimulator | AerSimulator | qasm_simulator |
| Shots | 1000 | N/A (QAE) | N/A (QAE) | 1000 |
| Measurement | Direct | QAE | QAE | Direct |

## Additional Application-Specific Details

### Option Pricing
- **Financial parameters**: S=2.0, vol=0.4, r=0.05, T=40/365
- **Strike price**: 1.896
- **Bounds calculation**: mean=2.0110, stddev=0.2675
- **Note**: `load_distribution` uses σ²=0.0175 (variance) as parameter

### Portfolio Selection
- **Constant variable**: 1 qubit, value=1
- **Operation sequence**: add(pad=True) → add(pad=False) → power2 → sub → mult
- **Final estimation**: on multiplication result

### Quantum Walk & Distribution Addition
- Both use direct measurement (no QAE)
- Results via classical post-processing of measurement counts

## Version Information

- **Python**: 3.7+
- **qiskit**: See requirements.txt
- **Backend**: qiskit Aer (qasm_simulator or AerSimulator)

For detailed configuration files, see the corresponding `*_config.json` files in this directory.

