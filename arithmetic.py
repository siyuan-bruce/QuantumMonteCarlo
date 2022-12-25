### pad rules: we can make sure we only pad the second variable if neccessary. The second 
from qiskit import *
from QArithmetic import add, sub, sub_swap
import numpy as np

from qiskit.utils import QuantumInstance
from typing import Tuple, Union, List, Optional, Any
from .distribution import Distribution
from .error import QMCError
from .variable import Variable
class Arithmetic:
    
    def __init__(
        self,
        qc: QuantumCircuit = None,
    ) -> None:
        
        if qc == None:
            self.qc = QuantumCircuit()
        else:
            self.qc = qc
    
    def add(
        self,
        var1: Variable,
        var2: Variable,
        pad: bool = True,
        name: str = "Adder",
    ) -> QuantumCircuit:
        
        qc1 = var1.get_qc()
        qc2 = var2.get_qc()
        
        name1 = var1.get_register().name
        name2 = var2.get_register().name
        
        width1 = qc1.width()
        width2 = qc2.width()
        
#         print("width1: ", width1)
#         print("width2: ", width2)
        
        if width1 < width2:
            a = var1.get_register()
            if pad == True:
                b = QuantumRegister(width1 + 1, name = name2 + "padded")
            else:
                b = var2.get_register()
            
            try:
                self.qc.add_register(a)
                self.qc.add_register(b)
            except:
                pass
#             self.qc = self.qc.compose(qc1, qubits = range(width1))
#             self.qc = self.qc.compose(qc2, qubits = range(width1, width1 + width2))
            add(self.qc, a, b, width1)
            
        elif width1 == width2:
            a = QuantumRegister(width1, name = name1)
            
            if pad == True:
                b = QuantumRegister(width2+1,  name = name2)
            else:
                b = QuantumRegister(width2, name = name2)
                
            self.qc.add_register(a)
            self.qc.add_register(b)

            
            add(self.qc, a, b, width1)
            
        else:
            a = var1.get_register()
            if pad == True:
                b = QuantumRegister(width1 + 1, name = name2 + "padded")
                self.qc.add_register(b)
                add(self.qc, a, b, width2)
                
            else:
                b = var2.get_register()
                add(self.qc, b, a, width2)
            
        var1.set_register(a)
        var2.set_register(b)
        
        return var1, var2
        
            
    def square(
        self,
        var1: Variable,
        name: str = "Square",
              ) -> QuantumCircuit:
        
        qc1 = var1.get_qc()
        
        width1 = qc1.width()
        width2 = 2 * width1
        
        a = QuantumRegister(width1, "var_a")
        b = QuantumRegister(width2, "square")
        self.qc.add_register(a)
        self.qc.add_register(b)
        self.qc = self.qc.compose(qc1, qubits = range(width1))
        self.qc = self.qc.compose(qc2, qubits = range(width1, width1  + width2))

        square(self.qc, a, b)
        
        return a, b 
            
#     def power(
#         self,
#         var1: Variable,
#         var2: Variable,
#         name: str = "Power",
#               ) -> QuantumCircuit:
        
#         dist = UniformDistribution(self.num_qubits, name = name)
        
#         return dist
    
    def get_qc(self):
        return self.qc