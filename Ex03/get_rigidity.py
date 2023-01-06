"""
8- [1 point] Write a python function with the name of "get_rigidity"
to calculate the magnetic rigidity.
Test your code with the results of the previous exercise!

Beckmann, Thomas
January 2023
"""
import numpy as np
import scipy.constants as spc

class Particle:
	def __init__(self,charge,mass,e_kin): # instantiate class by giving the charge as multiples of e, the mass [kg] and the kinetic energy [J]
		self.q = abs(charge) * spc.e
		self.mass = mass	
		self.gamma = e_kin/(self.mass * spc.c**2) + 1
		self.beta = np.sqrt(1-1/self.gamma**2)

	def get_rigidity(self):
		return self.gamma * self.beta*spc.c * self.mass / self.q

def main():
# Task 1: 190 [AMeV] 238-U-28+
	u_238 = Particle(+28,238.05*1.66E-27,238*190E6*spc.e)
	print(f'The magnetic rigidity of 190 [AMeV] 238-U-28+ is {u_238.get_rigidity():.2f} [Tm]')
# Task 2: 410 [MeV/u] 197-Au-77+
	au_197 = Particle(+77,196.97*1.66E-27,196.97*410E6*spc.e)
	print(f'The magnetic rigidity of 410 [MeV/u] 197-Au-77+ is {au_197.get_rigidity():.2f} [Tm]')
# Task 3: 10 [GeV] electrons
	electron = Particle(-1,9.11E-31,10E9*spc.e)
	print(f'The magnetic rigidity of 10 [GeV] electrons is {electron.get_rigidity():.2f} [Tm]')

if __name__ == '__main__':
    main()