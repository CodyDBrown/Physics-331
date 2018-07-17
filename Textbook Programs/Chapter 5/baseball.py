import numpy as np
def baseball(w,t):
    """
    Finds the acceleration of a Baseball with forces from gravity and air resistance. 
    
    Inputs
    ----------
    w: array of with the possition and velocity of the ball
        w[0] = x, w[1] = y, w[2] = v_x, w[3] = v_y
    t: holder varriable. Again I should be able to get rid of this, but I don't know how to yet. 
    
    Output
    ----------
    foo: Array of velocities and accelerations
        foo[0] = v_x, foo[1] = v_y, foo[2] = a_x, foo[3] = a_y
    """
    g = 9.8    #gravity (m/s**2)
    rho = 1.2  #Mass density of air (kg/m**3)
    a = 4.16e-3 #crosssectional area of a baseball (m**2)
    C_d = 0.5  #Drag coefficient
    M = 0.142  #Mass of a baseball (kg)
    
    alpha = 0.5 * rho * a * C_d / M
    v_mag = np.linalg.norm(v) #Magnitude of the velocity
    
    foo = np.array([w[2], w[3], -alpha*v_mag*w[2], -g - alpha*v_mag * w[3]])
    return foo