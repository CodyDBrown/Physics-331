from caseI import caseI
from rk2 import rk2
def BC_caseI(omega):
    """
    Finds the value of w_1(x) at the end point. x = L = 1 (m)

    """
    L = 1.

    w0 = [0.0, 1.0, omega]
    w = rk2(w0, 0.0, 0.001,1, caseI)
    return w[-1, 0]
