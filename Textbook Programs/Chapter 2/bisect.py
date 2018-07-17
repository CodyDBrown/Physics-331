def bisect(func_name, x_left, x_rigt):
    """
    Find the solution the input equation f(x) = 0 for some input function. Start
    with the interval x_left x_rigt, and return a soltuion with a relative error
    0.5e-5.

    Input
    ----------
    func_name: This is the name of the function that I want to find roots for
    x_left: Smaller 'x' value I want to evaluate func_name at
    x_rigt: Higher 'x' value I want to evaluate func_name at

    Output
    ----------
    x_zero: 'x' value that returns func_name(x) = 0
    """
    f_left = func_name(x_left)
    f_rigt = func_name(x_rigt)
    #print("Function at the left: {} \nFunction at the right: {} ".format(f_left, f_rigt))
    if f_left * f_rigt > 0:     # Same sign on both sides
        return print("Both values give the same sign.") #Exit if inputs are wrong

    while np.abs( x_rigt - x_left ) > 1.0e-5 * np.max(np.abs([x_left,x_rigt])):
        x_mp = 0.5*(x_left + x_rigt)
        f_mp = func_name(x_mp)

        if f_mp == 0:       # Got lucky and found the root exactly
            return x_mp

        if f_mp * f_rigt > 0:
            x_rigt = x_mp
            f_rigt = f_mp

        else:
            x_left = x_mp
            f_left = f_mp
    x_zero = 0.5 * (x_left + x_rigt)

    return x_zero
