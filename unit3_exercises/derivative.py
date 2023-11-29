import numpy as np
from utilities import plot_tangent
    
# define the x values
x = np.arange(0.0,11.0,1)

# function f(x)
f = np.log(x+1)
t1 = x/3 + 0.43
t2 = x/10 + 1.42

# plot the function
plot_tangent(x,f,t1,t2,'f=ln(1+x)','tangent at x=2','tangent at x=9')