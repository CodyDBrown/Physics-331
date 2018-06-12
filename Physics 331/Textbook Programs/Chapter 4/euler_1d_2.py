def euler_1d_2(y0, t0, dt, tf, deriv_func):
    import numpy as np
    """
    Program is the same as 'euler-1d' but I wanted to make it a little easier to input time values. Rather than
    have t0, dt, and number of steps this has an initial and final time, with a set step size value. This is
    acctually a little faster than euler_1d. Using the %timeit command the run times were
    euler_1d:   8.81 µs ± 63 ns
    euler_1d_2: 6.04 µs ± 209 ns
    
    Input
    ----------
    y0: Starting 'y' value
    s a
    t0: Starting time
    
    tf: Final time
    
    dt: Size of the step I want to take.

    deriv_func: Function that I am trying to numerically solve. 
    
    Output
    ----------
    y:  Array of values evaluated at each point in time. Should looke like
        y = [y(0), y(1), y(2), ... , y(n_steps)]
    
    """
    
    t = np.arange(t0, tf, dt) #starts and t0 and makes steps of size dt. Does not get to tf. It gets as
                            #Close as it can to tf, but will always stop short of it.
    y = [y0] #Set y
    for n in range(len(t)):
        f = deriv_func(y[n], t[n])     #Evaluate the function f(y,t)
        y.append(y[n] + dt * f)    #This is the Euler's method part. 
    return y,t 