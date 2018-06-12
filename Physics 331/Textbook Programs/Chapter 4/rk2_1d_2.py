def rk2_1d_2(y0, t0, dt, tf, deriv_func):
    import numpy as np
    """
    Inputs
    ----------
    y0: Starting y value
    
    t0: Starting time
    
    dt: Step size I want to take
    
    tf: End time.
    
    deriv_func: Name of the function that I want to solve.
    
    Output
    ----------
    y:  Array of values evaluated at the different times should have the form of
        y = [y(0), y(1), y(2), ... , y(n_steps)]
    """
    t = np.arange(t0, tf, dt) #starts and t0 and makes steps of size dt. Does not get to tf. It gets as
                            #Close as it can to tf, but will always stop short of it.
    y = [y0] #Set y
    
    for n in range(len(t)):
        f = deriv_func(y[n],t[n])
        y_star = y[n] + 0.5 * dt * f
        
        #Now take the full step
        t_star = t[n] + 0.5 * dt
        f_star = deriv_func(y_star, t_star)
        y.append(y[n] + dt*f_star)
    return y