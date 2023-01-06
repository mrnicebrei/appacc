"""
9- [1 point] From the accelerator department, you received some data (see the attached data file: 2016-07-11_ipm_data.txt)
from an ionisation beam profile monitor (IPM). Read the file and plot it in blue color on a black grid background. 
The mark the maximum with a red dot!

Beckmann, Thomas
January 2023
"""

import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt('2016-07-11_ipm_data.txt') #import data from txt

def main():
	plt.plot(data)
	plt.grid(color='k')
	plt.plot(np.argmax(data), np.amax(data), marker='o', mfc='r')
	plt.xlabel('Signal Position')
	plt.ylabel('Signal Intensity')
	plt.title('Data from IPM')
	plt.savefig('Ex3_plot.png')

if __name__ == '__main__':
    main()