def getstats(x, y):
    """
    Determine the statistical measured for an array of data points 'x' and 'y'
    
    Inputs
    ----------
    x: Independent varriable
    y: dependent varriable.
    
    Outputs
    ----------
    mean: Mean of 'x'
    dmean: Uncertainty in the mean
    variance: Variance
    
    """
    import numpy as np
    
    #Make sure the input is an array
    x = np.array(x)
    y = np.array(y)
 
    #Check to make sure the inputs are the same length
    if len(x) != len(y):
        print('ERROR: Arrays x ({}) and y ({}) need to be the same length'.format(len(x), len(y)))
        return
    
    
    sy = sum(y)
    sxy = sum(x*y)
    sx2y = sum(x**2 * y)
    
    mean = sxy / sy
    
    if len(x) > 1:
        variance = (sx2y -2*mean*sxy + mean**2 * sy) / (sy - 1)
    else:
        variance = 0
        
    dmean = np.sqrt(variance / sy)
    stats = np.array([mean,dmean, variance])
    
    return stats