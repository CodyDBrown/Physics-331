from efld import efld
def tan_vec(r, s):

    """
    Notes on getting this to work: So this was a huge pain to get this to work. The problem was trying to find
    a way so that 'efld' was defined when tan_vec ran. If you open a new notebook and just did
        %run efld.py
        %run tan_vec.py
    efld would run with out a problem. But when you tired to run tan_vec it would give you an error that
    'efld' is not defined. If efld is saved in the same file as tan_vec then you just need to add line 3.
        from efld import efld
    and it will run without a problem. The commented out lines of 1 and 2 are only needed if efld is saved in a different folder. I make a copy of efld and added it to '.../Chapter 5' so they weren't needed any more.
    Things that don't work are
        import efld
        from efld import *
    Just doing import efld makes efld a modulo and then you'll get an error "modulo not callable"
    using the * in import gives an error that it's not usable inside a function.
    """
    #Finds the tangent vector to the electric field at point 'r'
    e = efld(r)
    emag = np.sqrt(sum(e**2)) #Magnitude of the electric field
    return e / emag
