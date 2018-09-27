from efld import efld

def efld_mag2(x):
    """
    I want to find the magnitude of the electric field for the arrangment of
    charged particles given in the program efld.py

    Input
    ----------
    x:  Two element array (x(0) = x value, x(1) = y value) of where I want to
        find the magnitude of the electric field.

    Output
    ----------
    mag: magnitude of the electric field evaluated at the input point 'x'
    """

    #Run the program efld and set it’s returned value to ‘e’
    e = efld(x)

    #Find the magnitude squared of 'e'
    mag = e[0]**2 + e[1]**2
    return mag
