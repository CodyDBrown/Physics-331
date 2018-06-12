def euler_1d_3(y0, t0, dt, tf, deriv_func):
    import numpy as np
    """
    Program will take n_steps of size dt in the differential equation dy/dt = f(y,t) = deriv_func(y,t)
    
    Input
    ----------
    y0: Starting 'y' value
    
    t0: Starting 't' value
    
    dt: Size of the step I want to take.
    
    n_steps: Number of steps I want to take
    
    deriv_func: Function that I am trying to numerically solve. 
    
    Output
    ----------
    y:  Array of values evaluated at each point in time. Should looke like
        y = [y(0), y(1), y(2), ... , y(n_steps)]
    
    """
    n_steps = int((tf - t0)/ dt)
    y = np.zeros(n_steps+1) # Make an array full of zeros with the length of n_setps.
    
    y[0] = y0 #Sets the first value of an array to be 
    for n in range(n_steps):
        t = t0 + dt*n               #Current time
        f = deriv_func(y[n], t)     #Evaluate the function f(y,t)
        y[n + 1] = y[n] + dt * f    #This is the Euler's method part. 
    return y