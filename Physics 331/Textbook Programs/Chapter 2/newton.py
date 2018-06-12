def newton(function_name, deriv_name, x_guess):
    """
    Find the solution to the desired input function
    
    Inputs
    ----------
    function_name:  Name of the function that we want to solve for. This should either be a built in function 
                    or a .py file name.
    deriv_name:     Name of the derivative of function_name
    x_guess:        Newton's Method needs and Initial guess at the solutions. Doesn't have to be a good guess. 
    
    Returns
    ----------
    x_zero:         Returns the value that gives f(x_zero) = 0
    """
    x_zero = x_guess
    
    for i in range(20):
        f = function_name(x_zero)
        fp = deriv_name(x_zero)
        delta_x = -f/fp
        x_zero += delta_x   #This is the same as x_zero = x_zero + delta_x
        
        if abs(delta_x) < 0.5e-5 * abs(x_zero):
            return x_zero
    print("Closest answer after 20 tries is", x_zero)
    return x_zero