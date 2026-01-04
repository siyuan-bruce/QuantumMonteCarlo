from qiskit import *
from typing import Tuple, Union, List, Optional, Any
from .variable import Variable
from .arithmetic import Arithmetic

class QuantumWalk:
    
    def __init__(
        self,
        num_steps: int,
        distribution: str,
        size: int,
        qc: QuantumCircuit = None,
    ) -> None:
        
        if qc == None:
            self.qc = QuantumCircuit()
        else:
            self.qc = qc
        self.num_steps = num_steps
        self.distribution = distribution
        self.size = size
        self.loc_start = self.qc.width()
        self.vars = []
        self.registers = []
    
    def generate_dist(
        self,
        distribution: str = None,
        size: int = None,
        mu: Optional[float] = None,
        sigma: Optional[float] = None,
        bounds: Union[Tuple[float, float], List[Tuple[float, float]]] = None,
        name: str = "Quantum Walk",
    ) -> QuantumCircuit:
        
        if size == None:
            size = self.size
        else:
            self.size = size

        if distribution == None:
            distribution = self.distribution
        else:
            self.distribution = distribution
        
        loc_start = self.qc.width()
        
        for i in range(self.num_steps):

            step = Variable(self.size + i, name = name + " step " + str(i) )
            
            step.load_distribution(distribution, size, mu, sigma, bounds)
            
            register = step.get_register()
            self.qc.add_register(register)
            
#             print("dis: ", range(loc_start, step.num_qubits))
            self.qc = self.qc.compose(step.get_qc(), qubits = range(loc_start, loc_start + step.num_qubits))
            
            self.vars.append(step)
            
            loc_start += step.num_qubits
        
    def walk(
        self,
    )-> QuantumCircuit:
        size = self.size
        loc_start = self.loc_start
        
        for i in range(self.num_steps - 1):
            arithmetic = Arithmetic()
            var1 = self.vars[i]
            var2 = self.vars[i+1]
#             print("var1_num_qubits:", var1.num_qubits)
#             print("var2_num_qubits:", var2.num_qubits)
            var1, var2 = arithmetic.add(var1, var2, False)
            self.vars[i] = var1
            self.vars[i+1] = var2
            
            loc_end = loc_start + self.size + i + self.size + i + 1
#             print(arithmetic.get_qc().width())
#             print(range(int(loc_start), int(loc_end)))
            self.qc = self.qc.compose(arithmetic.get_qc(), range(int(loc_start), int(loc_end)))
        
            loc_start += var1.num_qubits
            
    def get_qc(self):
        return self.qc
    
    def get_vars(self):
        return self.vars