import numpy as np
def rk2_1d(y0, t0, tf, dt, deriv_func):
    """
    Numerically solves the first order ODE deriv_func using Runga-Kutta second order method

    Inputs
    ----------
    y0:         Starting 'y' value

    t0:         Starting time

    tf:         End time.

    dt:         Step size I want to take

    deriv_func: Name of the function that I want to solve.

    Outputs
    ----------
    y:  Array of values evaluated at the different times should have the form of
        y = [y(0), y(1), y(2), ... , y(n_steps)]

    t:  Array of time values that deriv_func was evaluated at. This is just to
        make plotting easier.
    """
    t = np.arange(t0, tf, dt)   #Array of all the times we want
    n_steps = len(t)

    y  = np.zeros(n_steps)
    y[0] = y0
    for n in range(n_steps-1):
        #Take a half step
        f = deriv_func(y[n],t[n])
        y_star = y[n] + 0.5 * dt * f

        #Now take the full step
        t_star = t[n] + 0.5 * dt
        f_star = deriv_func(y_star, t_star)
        y[n+1] = (y[n] + dt*f_star)

    return t, y
