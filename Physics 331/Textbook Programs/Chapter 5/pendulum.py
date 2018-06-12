def pendulum(y, t):
    """
    Returns the RHS of the equation for a damped pendulum.
    theta'' = -nu * theta' - (g/L) * sin(theta)
    
    Inputs
    ----------
    y:  Possition and velocity. y[0] should be the possition (theta in this case), and y[1] will be the 
        derivative of y[0] so theta' (dtheta / dt)
    t:  Time. Not used in the program but when I feed this into rk2
    
    Output:
    ----------
    Vector of the results of integrating the velocity and possition. f[0] should be y[1], integral of 
    the possitions is just the velocity. f[1] will be the acceleration.
    """
    import numpy as np
    
    g = 9.8  #Acceleration of gravity (m/s**2)
    L = 9.8  #Length of the pendulum (m)
    nu = 0.1 #Damping coefficient (s**-1)
    
    a = -nu * y[1] - (g/L)*np.sin(y[0])
    return np.array([y[1], a]) #Make the output a numpy array so that we can do math with it. If we don't turn
                                #this into an array then when we pass pendulum to rk2 we get an error in the line
                                #y_star = y[n][:] + 0.5 * dt * f because we can't multiply at list 'f' with
                                #a number 'dt'