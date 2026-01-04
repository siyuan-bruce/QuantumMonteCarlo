#!/usr/bin/env python3
"""
Main script to run all QuantumMonteCarlo applications.
This script will:
1. Check and install required packages if missing
2. Set up the Python path to find QuantumMC module
3. Run all application examples
"""

import sys
import os
import subprocess
import importlib.util

# Get the project root directory (where this script is located)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Change to project root directory to ensure relative paths work
os.chdir(PROJECT_ROOT)

# Add src to path
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'applications'))

# Required packages from setup.py
REQUIRED_PACKAGES = [
    'numpy',
    'scipy',
    'matplotlib',
    'qiskit',
    'qiskit_finance',
    'qiskit_aer',
    'qiskit_optimization',
    'qiskit_algorithms'
]

# Applications to run
APPLICATIONS = [
    'quantum_walk',
    'option_pricing',
    'portfolio_selection',
    'distribution_addition'
]


def check_package(package_name):
    """Check if a package is installed."""
    try:
        # Handle package name variations
        import_name = package_name.replace('-', '_')
        if package_name == 'qiskit-algorithms':
            import_name = 'qiskit_algorithms'
        elif package_name == 'qiskit_finance':
            import_name = 'qiskit_finance'
        elif package_name == 'qiskit_aer':
            import_name = 'qiskit_aer'
        elif package_name == 'qiskit_optimization':
            import_name = 'qiskit_optimization'
        
        spec = importlib.util.find_spec(import_name)
        return spec is not None
    except (ImportError, ModuleNotFoundError):
        return False


def install_package(package_name):
    """Install a package using pip."""
    print(f"Installing {package_name}...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name, '--quiet'])
        return True
    except subprocess.CalledProcessError:
        print(f"Warning: Failed to install {package_name}")
        return False


def check_and_install_packages():
    """Check all required packages and install missing ones."""
    print("=" * 60)
    print("Checking required packages...")
    print("=" * 60)
    
    missing_packages = []
    for package in REQUIRED_PACKAGES:
        if check_package(package):
            print(f"✓ {package} is installed")
        else:
            print(f"✗ {package} is missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nInstalling {len(missing_packages)} missing package(s)...")
        for package in missing_packages:
            install_package(package)
        
        # Verify installation
        print("\nVerifying installations...")
        still_missing = []
        for package in missing_packages:
            if check_package(package):
                print(f"✓ {package} installed successfully")
            else:
                print(f"✗ {package} installation failed")
                still_missing.append(package)
        
        if still_missing:
            print(f"\nWarning: {len(still_missing)} package(s) could not be installed:")
            for pkg in still_missing:
                print(f"  - {pkg}")
            print("\nPlease install them manually:")
            print(f"  pip install {' '.join(still_missing)}")
            return False
    
    print("\nAll required packages are available!")
    return True


def run_application(app_name):
    """Run a single application as a subprocess."""
    app_path = os.path.join('applications', f'{app_name}.py')
    
    if not os.path.exists(app_path):
        print(f"Error: Application file not found: {app_path}")
        return False
    
    print("\n" + "=" * 60)
    print(f"Running {app_name}...")
    print("=" * 60)
    
    try:
        # Run the application as a subprocess
        # This ensures proper module imports and isolation
        result = subprocess.run(
            [sys.executable, app_path],
            cwd=PROJECT_ROOT,  # Run from project root
            capture_output=False,  # Show output in real-time
            text=True,
            timeout=300  # 5 minute timeout per application
        )
        
        if result.returncode == 0:
            print(f"✓ {app_name} completed successfully")
            return True
        else:
            print(f"✗ {app_name} failed with return code {result.returncode}")
            return False
        
    except subprocess.TimeoutExpired:
        print(f"✗ {app_name} timed out after 5 minutes")
        return False
    except Exception as e:
        print(f"✗ {app_name} failed with error:")
        print(f"  {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main function to run all applications."""
    print("=" * 60)
    print("QuantumMonteCarlo - Application Runner")
    print("=" * 60)
    
    # Check and install packages
    if not check_and_install_packages():
        print("\nSome packages are missing. Please install them and try again.")
        return 1
    
    # Run all applications
    print("\n" + "=" * 60)
    print("Running all applications...")
    print("=" * 60)
    
    results = {}
    for app in APPLICATIONS:
        results[app] = run_application(app)
    
    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    
    successful = sum(1 for v in results.values() if v)
    total = len(results)
    
    for app, success in results.items():
        status = "✓ PASSED" if success else "✗ FAILED"
        print(f"{status}: {app}")
    
    print(f"\nTotal: {successful}/{total} applications completed successfully")
    
    return 0 if successful == total else 1


if __name__ == '__main__':
    sys.exit(main())

