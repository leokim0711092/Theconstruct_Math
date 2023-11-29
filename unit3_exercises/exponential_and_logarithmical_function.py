import numpy as np
from utilities import plot_equation

# define the x values
t = np.arange(0,6,1)

# function population N(t)
N_0 = 1000
r = 0.75
N_t = N_0 * np.exp(r*t)

# plot the equation
plot_equation(t,N_t,'N_t = N_0*e^rt','Time t','Population infected N(t)')

plot_equation(N_t,t,'t = (1/r)*ln(N(t)/N_0)','Population infected N(t)','Time t')