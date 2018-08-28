import numpy as np
def equation2(x):
    """
    Equation 2.2 from the book.

    Input
    ----------
    x: Value I want to evaluate equation 2.2 at

    Output
    ----------
    Value of the function at 'x', f(x)
    """
    return np.exp(x) - 3*x**2
