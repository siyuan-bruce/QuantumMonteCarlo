from qiskit import *
import matplotlib.pyplot as plt
import numpy as np

from qiskit_finance.circuit.library import UniformDistribution, LogNormalDistribution, NormalDistribution
from typing import Tuple, Union, List, Optional, Any
from .distribution import Distribution
from .error import QMCError

class Variable:
    
    def __init__(
        self,
        num_qubits: int,
        name: str = None,
    ) -> None:
        
        if name == None:
            self.name = "var" + str(np.random.randint(1000000))
        else:
            self.name = name
        self.num_qubits = num_qubits

        self.register = QuantumRegister(self.num_qubits,  self.name)
        self.qc = QuantumCircuit(self.register)
        self.loaded = 0
        
    def load_distribution(
        self,
        distribution: str,
        size: int,
        mu: Optional[float] = None,
        sigma: Optional[float] = None,
        bounds: Union[Tuple[float, float], List[Tuple[float, float]]] = None,
    ) -> None:
        if self.loaded ==1:
            raise QMCError("The data is already loaded.")
        
        dist = Distribution(size)
        if distribution == "Normal":
            self.qc = self.qc.compose(dist.Normal(mu, sigma, bounds = bounds), range(size))
        elif distribution == "Uniform":
            self.qc = self.qc.compose(dist.Uniform(mu, sigma), range(size))
        elif distribution == "LogNormal":
            self.qc = self.qc.compose(dist.LogNormal(mu, sigma, bounds = bounds), range(size))
        else:
            raise QMCError("Not a provided distribution")
        
        self.loaded = 1
            
    def load_constant(
        self,
        constant: int,
    ) -> None:
        
        if self.loaded ==1:
            raise QMCError("The data is already loaded.")
        
        constant_b = str(bin(constant))[2:]
        
        length = len(constant_b)
        
        # print(constant_b)
        if length > self.num_qubits:
            raise QMCError("Cannot represent the number in a limited number of qubits.")
        
        for i in range(len(constant_b)):
            if constant_b[i] == "1":
                self.qc.x(length - (i+1)) #Flip the qubit from 0 to 1
        
        self.loaded = 1
        
    def get_qc(self):
        return self.qc
    
    def get_register(self):
        return self.register
    
    
    def set_register(
        self,
        register: QuantumRegister,
    ):
        self.num_qubits = register.size
        self.register = register
        