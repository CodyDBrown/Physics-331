import numpy as np
def equation3(theta):
    """
    Equation 2.3 from the book.

    Input
    ----------
    theta: Angle that I want to evaluate equation 2.3 at. Input should be in degrees

    Output
    ----------
    Value of the function at theta, f(theta)

    """
    th_rad = np.radians(theta)   # Convert the input into radian

    return 250*np.cos(th_rad)* (np.sin(th_rad) + np.sqrt( np.sin(th_rad)**2 + 0.08 ) ) - 200
