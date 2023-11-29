import numpy as np
import matplotlib.pyplot as plt
from utilities import plot_vectors

# Vector v
v = np.array(((1,0)))

# Rotation matrix R
R = np.array(((0,-1),
              (1,0)))

# Product of matrices with numpy
w = np.dot(R,v)
print('Product of matrices w = R * v =',w)

plot_vectors((v,w),'rotation')