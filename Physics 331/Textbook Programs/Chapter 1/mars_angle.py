import numpy as np

def mars_angle(d):
    """
    Find the angle, in degrees, that mars appears in the sky on some day 'd' of
    the year 2000

    Input
    ----------
    d: This is the day that I want to evaluate things at

    Output
    ----------
    theta: Angle between Earth and Mars for the given input day 'd'
    """

    Pe = 365.256    #Period of the Earths orbit (days)
    Pm = 686.980    #Period of Mars orbit (days)
    d0 = 187        #Day in the year 2000 that mars crosses theta = 0
    Re = 1.496e8    #Radius of Earths Orbit (km)
    Rm = 2.279e8    #Radius of Mars orbit (km)

    phi_e = 2*np.pi*d/Pe
    phi_m = 2*np.pi*(d-d0)/Pm

    #Find the x and y positions for Earth and Mars
    xe = Re*np.cos( phi_e )
    ye = Re*np.sin( phi_e )
    xm = Rm*np.cos( phi_m )
    ym = Rm*np.sin( phi_m )

    if (xm-xe) > 0:
        theta = np.arctan((ym - ye) / (xm - xe))
    else:
        theta = np.arctan((ym - ye) / (xm - xe)) + np.pi
    theta = 180*theta / np.pi

    return theta
