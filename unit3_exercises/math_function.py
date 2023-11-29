import numpy as np
from utilities import plot_function

# define the x values
x = np.arange(0,6,1)

# function f(x)
f = 3*x

# plot the function
plot_function(x,f,'f = 3*x')