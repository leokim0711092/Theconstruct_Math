import numpy as np
from utilities import plot_equation

# define the x values
radius = np.arange(0,6,1)

# function Volume
Volume = (4/3)*np.pi*radius**3

# plot the equation
plot_equation(radius,Volume,'V = (4/3)*pi*r^3','Radius of the sphere','Volume of the sphere')