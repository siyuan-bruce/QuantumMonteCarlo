from .distribution import Distribution
from .variable import Variable
from .estimation import QuantumEstimation
from .arithmetic import Arithmetic
from .quantumwalk import QuantumWalk
from qiskit import QuantumCircuit
import numpy as np
from typing import Tuple, Union, List, Optional, Any
from qiskit.circuit.library import LinearAmplitudeFunction

class QuantumMC:

    def __init__(
        self,
        qc: QuantumCircuit = None,
    ) -> None:
        
        if qc == None:
            qc = QuantumCircuit()

        self.qc = qc
        self.vars = []

        
    def add_variable(
        self,
        var: Variable,
    ):
        self.qc.add_register(var.get_register())
        self.vars.append(var)
        self.qc = self.qc.compose(var.get_qc(), range(self.qc.width() - var.num_qubits, self.qc.width()))
        
        return var

    def walk(
        self,
        num_steps: int,
        distribution: str,
        size: int,
        name: str = "walk",
        mu: Optional[float] = None,
        sigma: Optional[float] = None,
        bounds: Union[Tuple[float, float], List[Tuple[float, float]]] = None,
    ):

        qw = QuantumWalk(num_steps = num_steps, distribution = distribution, size = size, qc = self.qc)
        
        qw.generate_dist(name = name, mu = mu, sigma = sigma, bounds=bounds)
        qw.walk()
        for i in qw.vars:
            self.vars.append(i)
            
        self.qc = qw.get_qc()

        return qw
        
    
    def estimate(
        self,
        epsilon: float,
        alpha: float,
        var: Variable = None,
        objective: LinearAmplitudeFunction = None,
        plain: bool = None,
    ):
        qe = QuantumEstimation(self.qc)
        qe.estimate(var, objective = objective)
        if (objective == None) & (plain == None):
            plain = True
        result = qe.calculate(epsilon,alpha, plain = plain)
        self.qc = qe.qc
        return result
    
    
    def arithmetic(
        self,
        operation: str,
        variables: List[Variable] = [],
        pad: bool = True,
    ):
        arithmetic = Arithmetic(self.qc, self.qc.qregs)
#        print(len(variables))

        if operation == "add":
            a, b = arithmetic.add(variables[0], variables[1], pad)
            
        if operation == "square":
            a, b = arithmetic.add(variables[0])
            
        if operation == "power2":
            a,b = arithmetic.power2(variables[0])
            
        if operation == "mult":
            a, b, c = arithmetic.mult(variables[0], variables[1])
            self.qc = arithmetic.qc
            return a, b, c
            
        
        self.qc = arithmetic.qc
        return a,b
        
    def get_qc(self):
        return self.qc
        
    