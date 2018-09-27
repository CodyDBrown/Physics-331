import numpy as np
def efld(x):
    """
    Finds the electric field from three point charges located at (0,0), (1,0),
    and (0,0.5).

    Input
    ----------
    x:  Point where I want to find the electric field. This needs to be a two
        point list or array [x,y].

    Output
    ----------
    e:  Electic field at point x. [E_x, E_y]
    """

    eps0 = 8.8542e-12 #Permittivity of free space (F/m)

    xa = np.array([0.0, 0.0])   #Positions of charge 'a' (m)
    qa = 1.0                    #Charge of 'a' (C)

    xb = np.array([1.0, 0.0])
    qb = 3.0

    xc = np.array([0.0, 0.5])
    qc = -4.0

    ra = x - xa
    rb = x - xb
    rc = x - xc

    ra_mag = np.sqrt(ra[0]**2 + ra[1]**2)
    rb_mag = np.sqrt(rb[0]**2 + rb[1]**2)
    rc_mag = np.sqrt(rc[0]**2 + rc[1]**2)

    e = (qa * ra / ra_mag**3 + qb * rb / rb_mag**3 + qc * rc / rc_mag**3) / (4 * np.pi * eps0) #Electric field (N/C)
    return e
