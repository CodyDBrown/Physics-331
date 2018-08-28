import numpy as np

def bisect_eq2(xL, xR):
    """
    Find a solution to the equation f(x) = e^x - 3*x^2 = 0 using a bisection
    method. Starts with the interval between xL, xR and returns a
    solution. The Solution will be accurate to 0.5e-5. f(xL) and f(xR)
    need to have different signs (one positive, one negative).

    Inputs
    ----------
    xL: Lower 'x' value I want to evaluate the function f(x) at
    xR: Higher 'x' value I want to evaluate the function f(x) at

    Output
    ----------
    x_zero: 'x' value that when put into f(x) returns zero.
    """

    #Evaluate the function at the left and right values.
    fL = np.exp(xL) - 3*xL**2
    fR = np.exp(xR) - 3*xR**2

    #Keep doing bisect until the difference between the two values is less than
    # 10**-5
    while xR - xL > 1.0e-5:
        xMP = 0.5*(xL + xR)    # Mid-point
        fMP = np.exp(xMP) - 3*xMP**2 # Function evaluated at the mid point

        if fMP * f_left > 0.0:         # mp value has same sign as left
            xL = xMP               # Reset the left to be the mp
            f_left = fMP
        else:
            xR = xMP               # or set right value to mp
    x_zero = 0.5*(xL + xR)
    return x_zero
