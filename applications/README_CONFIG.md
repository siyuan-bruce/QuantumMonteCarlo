# Application Configuration Files

This directory contains configuration files documenting all hyperparameters for each application to ensure reproducibility.

## Configuration Files

- **quantum_walk_config.json** - Hyperparameters for the quantum walk example
- **option_pricing_config.json** - Hyperparameters for European call option pricing
- **portfolio_selection_config.json** - Hyperparameters for portfolio optimization
- **distribution_addition_config.json** - Hyperparameters for distribution addition example

## Configuration File Format

Each configuration file is a JSON document containing:

1. **encoding_precision**: Number of uncertainty qubits, discretization bounds
2. **distribution_parameters**: Distribution type, μ, σ, and related parameters
3. **walk_configuration**: Number of steps, state space size, bounds (if applicable)
4. **amplitude_estimation**: Target accuracy (ε), confidence (α), iterations
5. **arithmetic_options**: Padding policies, operations performed
6. **objective_function**: Rescaling factors, breakpoints, domain/image (if applicable)
7. **execution_details**: Backend/simulator, shot count, measurement type

## Quick Reference

| Application | QAE Used | Uncertainty Qubits | Distribution | Key Operations |
|------------|----------|-------------------|--------------|----------------|
| quantum_walk | No | 1 per step (3 total) | Normal | Direct measurement |
| option_pricing | Yes (ε=0.05, α=0.01) | 3 | LogNormal | QAE estimation |
| portfolio_selection | Yes (ε=0.01, α=0.01) | 1 per walk | Normal | add, power2, sub, mult |
| distribution_addition | No | 1 per step (3 total) | Normal | Direct measurement |

## Usage

To reproduce results from any application:

1. Review the corresponding configuration file
2. Ensure your environment matches the execution details
3. Run the application script with the documented parameters

## Environment Requirements

- Python 3.7+
- qiskit (with AerSimulator)
- NumPy, SciPy
- See main README.md for full requirements

