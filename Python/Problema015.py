# ========== Project Euler. Problem #15 =========

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

# -----------------------------------------------

# Función que retorna el factorial de n
def Factorial(n):
    P = 1
    for i in range(1,n+1):
        P*=i
    return P

def Choose(n,k):
    return Factorial(n)//(Factorial(k)*Factorial(n-k))

# Número de rutas de una tablero de n x n
def NumRoutes(n):
    return Choose(2*n, n)

n = 20

print(f"El número de rutas de un tablero de {n}x{n} es {NumRoutes(n)}")