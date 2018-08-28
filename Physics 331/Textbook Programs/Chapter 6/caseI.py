def caseI(w, x):
    """
    Evaluate the functions describing the eignenmode of case I from the book.

    Inputs
    ----------
    w:

    x:  dumby varraible
    """
    c_sq = 100.0  #Square of the wave speed (m/s)**2
    f1 = w[1]
    f2 = -w[0]*w[2]**2 / c_sq
    f3 = 0                     # Differenetial of the frequency. Frequency is constant so it's zero
    f = np.array([f1, f2, f3])
    return f
