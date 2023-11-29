import numpy as np
import matplotlib.pyplot as plt
from utilities import plot_vectors

# vector
vector = np.array((1,2))

# calculate multiplication
alpha = 2
multiplication_ = alpha*vector

plot_vectors([vector,multiplication_],'sum')