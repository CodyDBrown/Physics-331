import numpy as np
def baseball(w,t):
    """
    Finds the acceleration of a Baseball with forces from gravity and air resistance.

    Inputs
    ----------
    w:  Array of with the position and velocity of the ball
        w[0] = x (m)
        w[1] = y (m)
        w[2] = v_x (m/s)
        w[3] = v_y (m/s)

    t:  Dumby variable

    Output
    ----------
    foo: Array of velocities and accelerations
         foo[0] = v_x (m/s)
         foo[1] = v_y (m/s)
         foo[2] = a_x (m/s**2)
         foo[3] = a_y (m/s**2)
    """
    g = 9.8     #gravity (m/s**2)
    rho = 1.2   #Mass density of air (kg/m**3)
    a = 4.16e-3 #cross sectional area of a baseball (m**2)
    C_d = 0.5   #Drag coefficient
    M = 0.142   #Mass of a baseball (kg)

    alpha = 0.5 * rho * a * C_d / M

    v_mag = np.sqrt(w[2]**2 + w[3]**2) #Magnitude of the velocity

    foo = np.array([w[2], w[3], -alpha*v_mag*w[2], -g - alpha*v_mag * w[3]])
    return foo
