def caseII(w, x):
    import numpy as np
    c_sq = 1 / (0.001 + 0.018 * x)
    f1 = w[1]
    f2 = -w[0] * w[2]**2 / c_sq
    f3 = 0
    f = np.array([f1, f2, f3])
    
    return f