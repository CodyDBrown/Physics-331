def rk2(y0, t0, dt, tf, deriv_func):
    """
    General RK2 solver

    Inputs
    ----------
    y0: Starting 'y' values. y0 Can be an array/list of any number of dimentions

    t0: Initial time

    dt: Step size

    tf: Final time

    deriv_func: Derivative function that I want to solve for

    Output
    ----------
    y:Array of 'y' values.

    """
    t = np.arange(t0, tf, dt)

    y = np.zeros((len(t)+1, len(y0))) #Makes an array of zeros
    y[0,:] = y0 #Sets the first row in y to be the initial values.
    for n in range(len(t)):
        f = deriv_func(y[n,:],t[n])
        y_star = y[n,:] + 0.5 * dt * f

        #Now take the full step
        t_star = t[n] + 0.5 * dt
        f_star = deriv_func(y_star, t_star)
        y[n+1,:] = (y[n,:] + dt*f_star)
    return y
