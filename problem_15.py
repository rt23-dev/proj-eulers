# Lattice paths

def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    return fac

def lat_paths(n):
    noPaths = factorial(n*2)//(factorial(n)**2)
    return noPaths

print(lat_paths(20))