"""
Written by: Thomas Beckmann
Purpose: Multiplies 2 randomly generated 3x3 matrices and prints the result.
"""
import numpy as np
def MultMatrix(inA,inB): # multiplication function
    out = inA@inB
    return out
print("This application multiplies two randomly generated three by three matrices and prints the result.")
print("These are your randomly generated matrices: ")
MatA = np.random.randint(0,10,(3,3))
MatB = np.random.randint(0,10,(3,3))
print("Matrix A:\n",MatA)
print("Matrix B:\n",MatB)
MatC = MultMatrix(MatA,MatB)
print("This is your result:\n",MatC)
