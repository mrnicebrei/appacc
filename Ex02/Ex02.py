"""
12- [2 point]:
Write a python class for a particle, don't forget the init, by giving Z and A.
This class should have a method which gives the number of neutron back.
Instantiate this class with an example

Beckmann, Thomas

November 2022
"""

class particle:
	def __init__(self,massnumber,chargenumber): # instantiate class by giving Z and A
		self.massnumber = massnumber
		self.chargenumber = chargenumber

	def calc_neutrons (self): # method to calculate N
		self.neutronnumber = self.massnumber - self.chargenumber

	def identify(self):	#particle identifies itself, only prints N if calculated
		print(f"My Massnumber is {self.massnumber} and my Chargenumber is {self.chargenumber}.")
		if hasattr(self,"neutronnumber"):
			print (f"My Number of Neutrons is: {self.neutronnumber}")

def main():
	Carbon = particle(12,6)
	Carbon.calc_neutrons()
	Carbon.identify()

if __name__ == '__main__':
    main()