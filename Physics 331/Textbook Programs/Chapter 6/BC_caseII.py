from caseII import caseII
from rk2 import rk2
def BC_caseII(omega):
    """
    Finds the value of w_1(x) at the end point. x = L = 1 (m)

    """
    L = 1.

    w0 = [0.0, 1.0, omega]
    w = rk2(w0, 0.0, 0.001,1, caseII)

    return w[-1, 0]
