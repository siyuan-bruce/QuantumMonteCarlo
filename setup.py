import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="finqmc",
    version="0.2",
    author="Bruce",
    author_email="siyuan.jin@connect.ust.hk",
    description="Quantum Monte Carlo framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/siyuan-bruce/QuantumMonteCarlo",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'qiskit',
        'qiskit_finance',
        'qiskit_aer',
        'qiskit_optimization',
        'qiskit-algorithms'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)