import numpy as np
def euler_1d(y0, t0, tf, dt, deriv_func):
    """
    Numerically solve the first order ODE deriv_func using Eulers method

    Inputs
    ----------
    y0:         Starting 'y' value

    t0:         Starting time

    tf:         Final time

    dt:         Size of the step I want to take.

    deriv_func: Function that I am trying to numerically solve.

    Outputs
    ----------
    y:  Array of values evaluated at each point in time. Should look like
        y = [y(0), y(1), y(2), ... , y(n_steps)]

    t:  Array of times the function is evaluated at. You don't need this but it's
        nice to have to make plots
    """

    t = np.arange(t0, tf, dt)   #starts at t0 and makes steps of size dt. Does not
                                #get to tf. It gets as Close as it can to tf, but
                                #will always stop short of it.
    n_steps = len(t)
    y = np.zeros(n_steps)   #I want to make an array of zeros that I'll then put
                            #y-values into. This is a good practice because it
                            #forces the computer to allocate enough memory for the
                            #final answer and can prevent memory problems

    #Set the first element of the array to be our input starting value y0
    y[0] = y0
    for n in range(n_steps-1):
        f = deriv_func(y[n], t[n])  #Evaluate the function f(y,t)
        y[n+1] = (y[n] + dt * f)    #This is the Euler's method part.
    return t, y
