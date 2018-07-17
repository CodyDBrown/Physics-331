def sky_diver(v,t):
    """
    Acceleration of an object falling from gravity, with air resistance. dv/dt = g - alpha * v**2
    
    Input
    ----------
    v: Velocity of the object
    t: Dumby variable put in so that euler/rk2 can handle it. There should be away to get rid of this but 
       I don't know what it is yet so for now it stays in
       
    Output
    ----------
    a: Acceleration for a given velocity
    
    """
    g = 9.8         # Acceleration from gravity (m/s/s)
    rho = 1.2       # Mass density of the air they're falling in (kg/m**3)
    a = 1.0         # cross-sectional area of the sky diver (m**2)
    C_d = 1.0       # coefficient of drag
    M = 100.0       # mass of the diver (kg)
    alpha = 0.5 * rho * a * C_d / M
    return g - alpha * abs(v)*v
    