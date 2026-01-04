import sys
import os

sys.path.append('src/')
sys.path.append('../src/')

from QuantumMC.quantummc import QuantumMC
from qiskit import ClassicalRegister, transpile
from qiskit_aer import AerSimulator

# Initialize QuantumMC object
qmc = QuantumMC()

# Perform quantum walk with 1 and 2 steps, respectively
qw1 = qmc.walk(num_steps = 3, distribution = "Normal", size = 1, name = "r", mu = 0.5, sigma = 1, bounds=(0, 1))


# qmc = QuantumMC()
b = qw1.vars[-1]
# # Perform quantum walk with 1 and 2 steps, respectively
# qw1 = qmc.walk(num_steps = 1, distribution = "Normal", size = 1, name = "r", mu = 0.5, sigma = 0.1, bounds=(0, 1))

cr = ClassicalRegister(b.get_register().size)
qmc.get_qc().add_register(cr)
for i in range(cr.size):
    qmc.get_qc().measure(b.get_register()[i], cr[i])
    
num_shots = 1000 #Setting the number of times to repeat measurement
backend = AerSimulator()
transpiled_circuit = transpile(qmc.get_qc(), backend)
job = backend.run(transpiled_circuit, shots=num_shots)
#Get results of program
job_stats = job.result().get_counts()
print(job_stats)

a = 0
for i in job_stats:
    a +=(int(i,2) * job_stats[i])   
    print(int(i,2))
    
print(a/num_shots)