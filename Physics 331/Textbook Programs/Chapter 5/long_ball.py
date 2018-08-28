from baseball import baseball
from rk2 import rk2
import numpy as np

def long_ball(v0, theta0):
    """
    Finds the distance traveled by a baseball with the initial velocity
    magnitude v0 and launched at angle theta0

    Inputs
    ----------
    v0:     Initial velocity magnitude (m/s)

    that0:  Initial launch angle (degrees)

    Output:
    ----------
    d:  Distance the ball traveled (m)

    """
    theta_r = np.radians(theta0) #Convert the input angle into radians

    dt = 0.01 #time step size (s)

    #Initial conditions w0 = [x0, y0, vx0, vy0]
    w0 = [0, 0, v0*np.cos(theta_r), v0*np.sin(theta_r)]
    t0 = 0.0

    #This is my 'flag' condition. The program will keep checking what 'done' is.
    #When it gets set to True then the program will end.
    done = False

    while not done:
        w, t = rk2(w0, t0, t0+2*dt, dt, baseball) #'tf' is set to t0+2*dt becasue I want
                                        #to take one step and then check to see
                                        #if we're done. The 2 is needed because
                                        #arange doesn't end at tf but at tf-dt


        w0 = w[1]
        t0 = t[1] + dt
        if w[1,1] < 0: #Checks if the 'y' position is in the ground or not
            done = True
        if t[-1] > 30:
            return print('Something went wrong, baseball is in the air to long')

    #Baseball has it the ground in the last step
    if done:
        x0 = w[0,0]
        y0 = w[0,1]

        x1 = w[1,0]
        y1 = w[1,1]

        frac = y0/(y0-y1)
        d = x0 * frac + x1*(1-frac)
    return d
