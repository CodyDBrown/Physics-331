def euler_1d_3(y0, t0, tf, dt, deriv_func):
    from numpy import arange, zeros
    """
    This is a third attempt at making euler_1d a little easier to work with. Inputs are the same as euler_1d_2 
    but the 'problem' with euler_1d_2 is that it didn't use a numpy array for the 'y' values. This used a np.array
    This is acctually surprisingly slower than either of the other two euler_1d's. with a run time of
    %timeit euler_1d_3(0,0,10,1,sky_diver)
        10 µs ± 141 ns
    
    Input
    ----------
    y0: Starting 'y' value
    
    t0: Starting time
    
    tf: Final time
    
    dt: Size of the step I want to take.

    deriv_func: Function that I am trying to numerically solve. 
    
    Output
    ----------
    y:  Array of values evaluated at each point in time. Should looke like
        y = [y(0), y(1), y(2), ... , y(n_steps)]
    
    """
    
    t = arange(t0, tf, dt) #starts and t0 and makes steps of size dt. Does not get to tf. It gets as
                                #Close as it can to tf, but will always stop short of it.
    t_foo = len(t)
    y = zeros(t_foo)
    
    for n in range(t_foo-1):
        f = deriv_func(y[n], t[n])     #Evaluate the function f(y,t)
        y[n+1] =(y[n] + dt * f)    #This is the Euler's method part. 
    return y,t 