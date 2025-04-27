### pad rules: we can make sure we only pad the second variable if neccessary. The second 
from qiskit import *
from .QArithmetic import add, sub, sub_swap, cadd
import numpy as np

from qiskit_aer import AerSimulator
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
        

        reg1 = var1.get_register()
        reg2 = var2.get_register()

        name1 = reg1.name
        name2 = reg2.name
        
        width1 = qc1.width()
        width2 = qc2.width()
        
        
        if width1 < width2:
            a = var1.get_register()
            if pad == True:
                b = QuantumRegister(width2 + 1, name = name2 + " padded")
                self.qc.add_register(b)
                for i in range(width2):
                    self.qc.cx(reg2[i], b[i])

            # add(self.qc, a, b, width1)
            else:
                b = var2.get_register()
            
            try:
                self.qc.add_register(a)
            except:
                pass

            try:
                self.qc.add_register(b)
            except:
                pass
            
            add(self.qc, a, b, width1)
            
        elif width1 == width2:
            a = var1.get_register()
            
            if pad == True:
                b = QuantumRegister(width2 + 1, name = name2 + " padded")
                self.qc.add_register(b)
                for i in range(width2):
                    self.qc.cx(reg2[i], b[i])
            else:
                b = var2.get_register()
                
            try:
                self.qc.add_register(a)
            except:
                pass

            try:
                self.qc.add_register(b)
            except:
                pass

            add(self.qc, a, b, width1)
            
        else:
            a = var1.get_register()
            if pad == True:
                b = QuantumRegister(width2 + 1, name = name2 + " padded")
                self.qc.add_register(b)
                for i in range(width2):
                    self.qc.cx(reg2[i], b[i])
                
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
        try:
            self.qc.add_register(a)
        except:
            pass

        try:
            self.qc.add_register(b)
        except:
            pass
        self.qc = self.qc.compose(qc1, qubits = range(width1))
        self.qc = self.qc.compose(qc2, qubits = range(width1, width1  + width2))

        square(self.qc, a, b)
        
        return a, b 


    def power2(
        self,
        var1: Variable,
        name: str = "power2",
              ) -> QuantumCircuit:
        a = var1.get_register()
        
        b_size = 2 ** a.size
        var2 = Variable(b_size, "power2_b")
        b = QuantumRegister(b_size, "b")
        var2.set_register(b)
        
        try:
            self.qc.add_register(a)
        except:
            pass

        try:
            self.qc.add_register(b)
        except:
            pass
        
        self.qc.x(a[0])
        self.qc.cx(a[0],b[0])
        self.qc.x(a[0])

        for i in range(a.size):
            self.qc.cx(a[i],b[2**(i)])
            for j in range(1,2**(i)):
                self.qc.ccx(b[j], b[2**(i)], b[j + 2**(i)])
                self.qc.cx(b[j + 2**(i)], b[j])
                self.qc.cx(b[j + 2**(i)], b[2**(i)])


        for i in range(1, b.size):
            if i % 2 ==0:
                self.qc.cx(b[i],b[0])

        return var1, var2

    def mult(
        self,
        var1: Variable,
        var2: Variable,
        name: str = "multiplier",
    ):
        qc1 = var1.get_qc()
        qc2 = var2.get_qc()
        
        reg1 = var1.get_register()
        reg2 = var2.get_register()
        
        width1 = qc1.width()
        width2 = qc2.width()

        result_var = Variable(width1 + width2 + 1, "result_mult")
        reg3 = result_var.get_register()
        self.qc.add_register(reg3)

        if width1 == 1:
            for i in range(width2):
                self.qc.ccx(reg1[0], reg2[i], reg3[i])
            return var1, var2, result_var

        elif width1 == 2:
            for i in range(width2):
                self.qc.ccx(reg1[1], reg2[i], reg3[i + 1])
            cadd(self.qc, reg1[0], reg2, reg3, width2) # control to add them, the case can be generliazed into a larger width
            return var1, var2, result_var


    def sub(
            self,
            var1: Variable,
            var2: Variable,
            name: str = "Subtractor",
        ) -> QuantumCircuit:
            
            qc1 = var1.get_qc()
            qc2 = var2.get_qc()

            reg1 = var1.get_register()
            reg2 = var2.get_register()

            name1 = reg1.name
            name2 = reg2.name
            
            width1 = qc1.width()
            width2 = qc2.width()

            if width1 < width2:
                raise QMCError("we now only support |a>|b> to |a-b>|b>")
                
                
            a = var1.get_register()
            a_padded = QuantumRegister(width1 + 1, name = name1 + " padded")
            
            try:
                self.qc.add_register(a_padded)
            except:
                pass

            for i in range(width1):
                self.qc.cx(reg1[i], a_padded[i])

            var1.set_register(a_padded)
            var2.set_register(reg2)

            try:
                self.qc.add_register(reg2)
            except:
                pass

            sub_swap(self.qc, a_padded, reg2, width1)
            
            return var1, var2


    def get_qc(self):
        return self.qc