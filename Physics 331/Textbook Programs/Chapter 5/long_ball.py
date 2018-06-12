def long_ball(v0, theta0):
    """
    Finds the distance travelled by a baseball with the initial conditions v0, and angle theta0
    
    Inputs
    ----------
    v0: Initial velocity magnitude (m/s)
    that0: Initial launch angle (degrees)
    
    Output:
    ----------
    
    
    """
    import numpy as np
    import math as m
    from rk2 import rk2
    from baseball import baseball
    theta_r = m.radians(theta0) #Turn the input angle into a radian
    
    dt = 0.01 #time step size
    
    #Initial conditions
    w0 = [0, 0, v0*np.cos(theta_r), v0*np.sin(theta_r)]
    t = 0.0
    
    #This is my 'flag' condition. The program will keep checking what 'done' is. When it gets set to True then 
    #the program will end.
    done = False
    
    while not done:
        w = rk2(w0, t, dt, t+dt, baseball) #'tf' is set to t+dt becasue I want to take one step and then check
                                            #to see if we're done
        w0 = w[1,:]
        t = t + dt
        
        if w[1,1] < 0: #Checks if the y possition is in the ground or not
            done = True
        if t > 30:
            print('Something went wrong, baseball is in the air too long')
            break
    
    #Baseball has it the ground in the last step
    if done:
        x0 = w[0,0]
        y0 = w[0,1]
        
        x1 = w[1,0]
        y1 = w[1,1]
        
        frac = y0/(y0-y1)
        d = x0 * frac + x1*(1-frac)
    return d