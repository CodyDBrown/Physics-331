from efld import efld
"""
This first line is telling python to look at the file efld.py. Inside that file
there should be a function called efld. Without this first line the program wont 
know what do to when I try and call efld.
"""
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

    e = efld(x)
    mag = e[0]**2 + e[1]**2
    return mag
