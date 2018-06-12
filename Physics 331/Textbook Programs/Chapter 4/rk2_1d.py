def rk2_1d(y0, t0, dt, n_steps, deriv_func):
    import numpy as np
    """
    Inputs
    ----------
    y0: Starting y value
    
    t0: Starting time
    
    dt: Step size I want to take
    
    n_steps: Number of steps I want to take.
    
    deriv_func: Name of the function that I want to solve.
    
    Output
    ----------
    y:  Array of values evaluated at the different times should have the form of
        y = [y(0), y(1), y(2), ... , y(n_steps)]
    """
    #Make an empty array that will store the values
    y = np.zeros(n_steps+1)
    
    #Set the initial value
    y[0] = y0
    
    for n in range(n_steps):
        #First take a half step
        t = t0 + dt * n
        f = deriv_func(y[n],t)
        y_star = y[n] + 0.5 * dt * f
        
        #Now take the full step
        t_star = t + 0.5 * dt
        f_star = deriv_func(y_star, t_star)
        y[n+1] = y[n] + dt * f_star
    return y