def newton(func_name, deriv_name, x_guess):
    """
    Finds the roots of the input function func_name using newtons method

    Inputs
    ----------
    function_name:  Name of the function that we want to solve for. This should
                    either be a built in function or a .py file name.

    deriv_name: Name of the derivative of function_name

    x_guess:    Newton's Method needs and Initial guess at the solutions. Doesn't 
                have to be a good guess. But the better the guess the faster
                you'll get to the correct answer

    Output
    ----------
    x_zero: Returns the value that gives f(x_zero) = 0
    """
    x_zero = x_guess

    for i in range(20):
        f = func_name(x_zero)
        fp = deriv_name(x_zero)
        delta_x = -f/fp
        x_zero += delta_x   #This is the same as x_zero = x_zero + delta_x

        #If x_zero is within the tollerance then we can return the answer and quit
        if abs(delta_x) < 0.5e-5 * abs(x_zero):
            return x_zero
    #If we didn't find an accurate answer after 20 tries, we say it's good enough
    #and return what ever answer we have.
    print("Closest answer after 20 tries is", x_zero)
    return x_zero
