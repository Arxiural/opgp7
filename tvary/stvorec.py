def obvod(a):
    return 4 * a

def obsah(a):
    return a * a

from . import obdlznik

def obvod(a):
    return obdlznik.obvod(a, a)

def obsah(a):
    return obdlznik.obsah(a, a)