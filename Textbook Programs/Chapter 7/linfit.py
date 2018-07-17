import numpy as np
def linfit(x, y, sigma_y):
    """
    This function will make a least-squares fit to some data with a straight line f(x) = a + b*x
    
    Inputs
    ----------
    x: independent variable
    y: dependent variable
    sigma_y: array of uncertainties in the dependent variable
    
    Output
    ----------
    fitpar: array of fit parameters
        fitpar[0]: y intersept (a)
        fitpar[1]: uncertainty in y intersept
        fitpar[2]: slope (b)
        fitpar[3]: uncertainty in slope
        fitpar[4]: reduced chi-squared
    """
    npar = 2            #Number of fitting paramiters. If we were doing ax^2 + bx + c then npar = 3
    npts = len(x)       #Number of data points
    
    if npts < npar:
        print("Not enough data points to fit a first order polynomial")
        return
    
    if npts != len(y) or npts != len(sigma_y):
        print("Lengths of the inputs must be the same. len(x) = {}, len(y) = {},"
              "len(sigma_y) = {}".format(len(x),len(y), len(sigma_y)))
        return
    
    #Make sure everything is a np.array that'll make the math easier
    x = np.array(x)
    y = np.array(y)
    sigma_y = np.array(sigma_y)
    
    sw = sum(1 / sigma_y**2)
    sy = sum(y / sigma_y**2)
    sx = sum(x / sigma_y**2)
    sx2= sum((x / sigma_y)**2)
    sxy= sum((y*x / sigma_y)**2)
    
    #Find the fit paramiters
    a = (sx2*sy - sx*sxy)/Delta
    b = (sxy*sw - sx*sy)/Delta
    da = np.sqrt(sx2 / Delta)
    db = np.sqrt(sw / Delta)
    
    fit = a + b*x
    chi2 = sum(((y - fit) / sigma_y)**2)
    if npts > npar:
        chi2red = chi2 / (npts - npar)
    else:
        chi2red = 0
    
    return [a, da, b, db, chi2red] 
