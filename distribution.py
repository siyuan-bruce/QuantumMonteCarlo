from qiskit import *
import numpy as np

from qiskit_finance.circuit.library import UniformDistribution, LogNormalDistribution, NormalDistribution
from typing import Tuple, Union, List, Optional, Any
from .error import QMCError

class Distribution:
    
    def __init__(
        self,
        num_qubits: int,
    ) -> None:
        
        self.num_qubits = num_qubits
        
    
    def Uniform(
        self,
        mu: Optional[float] = None,
        sigma: Optional[float] = None,
        name: str = "Uniform(X)",
              ) -> QuantumCircuit:
        
        dist = UniformDistribution(self.num_qubits, name = name)
        
        return dist
    
            
    def Normal(
        self,
        mu: Optional[float] = None,
        sigma: Optional[float] = None,
        bounds: Union[Tuple[float, float], List[Tuple[float, float]]] = None,
        name: str = "Normal(X)",
              ) -> QuantumCircuit:
        
        if mu is None:
            mu = 0

        if sigma is None:
            sigma = 1
        
        dist = NormalDistribution(self.num_qubits, mu, sigma, name = name, bounds =  bounds)
        
        return dist
    
    def LogNormal(
        self,
        mu: Optional[float] = None,
        sigma: Optional[float] = None,
        bounds: Union[Tuple[float, float], List[Tuple[float, float]]] = None,
        name: str = "LogNormal(X)",
              ) -> QuantumCircuit:
        
        if mu is None:
            mu = 0

        if sigma is None:
            sigma = 1
        
        dist = LogNormalDistribution(self.num_qubits, mu, sigma, name = name, bounds =  bounds)
        
        return dist