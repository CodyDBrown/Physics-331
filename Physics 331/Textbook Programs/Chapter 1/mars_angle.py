def mars_angle(d):
    from numpy import pi, cos, sin, arctan
    """
    Find the angle, in degrees, that mars appears in the sky on some day 'd' of 
    the year 2000
    """
    Pe = 365.256    #Period of the Earths orbit (days)
    Pm = 686.980    #Period of Mars orbit (days)
    d0 = 187        #Day in the year 2000 that mars crosses theta = 0
    Re = 1.496e8    #Radius of Earths Orbit (km)
    Rm = 2.279e8    #Radius of Mars orbit (km) 
    
    phi_e = 2*pi*d/Pe
    phi_m = 2*pi*(d-d0)/Pm
    
    xe = Re*cos( phi_e )
    ye = Re*sin( phi_e )
    xm = Rm*cos( phi_m )
    ym = Rm*sin( phi_m ) 
    
    if (xm-xe) > 0:
        theta = arctan((ym - ye) / (xm - xe))
    else:
        theta = arctan((ym - ye) / (xm - xe)) + pi
    theta = 180*theta / pi
        
    return theta