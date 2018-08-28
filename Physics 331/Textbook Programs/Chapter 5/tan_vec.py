from efld import efld
import numpy as np
def tan_vec(r, s):

    """
    Differential equation 5.9 in the book. Solving this will plot out the field
    lines for the point charge distribution we used in chapter 3self.

    Inputs
    ----------
    r:  Position we want to evaluate the function at

    s:  Dumby varriable.

    Output
    ----------
    dr/ds: First order ODE we want to solve
    """
    #Finds the tangent vector to the electric field at point 'r'
    e = efld(r)
    emag = np.sqrt(sum(e**2)) #Magnitude of the electric field
    return e / emag
