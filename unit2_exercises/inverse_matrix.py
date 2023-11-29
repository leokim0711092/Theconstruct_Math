import numpy as np
import matplotlib.pyplot as plt

# create a matrix with numpy
A = np.array(((1,2),
             (3,4)))
print('Matrix A: ')
print(A)

# invert matrix with numpy
A_inverted = np.linalg.inv(A)
print('Matrix A inverted: ')
print(A_inverted)