import numpy as np
def deriv_eq2(x):
    """
    Evaluated the derivative of equation 2 in the book f(x) = exp(x) - 3*x**2,
    f'(x) = exp(x) - 6*x

    Inputs
    ----------
    x: Number I want to evaluate the derivative at.

    Output
    ----------
    fp: Value of the function evaluated at the input 'x', f'(x) = fp
    """
    return np.exp(x) - 6 * x
