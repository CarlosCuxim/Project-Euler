# ========== Project Euler. Problem #9 ==========

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# -----------------------------------------------

# Determina si un número n es un cuadrado perfecto
def isSquare(n):
    if n**0.5 - int(n**0.5) == 0:
        return True
    else:
        return False

# Obtiene el producto de la primera terna pitagórica que suma n
def GetPythProd(n):
    for a in range(1, n+1):
        for b in range(a, n+1):
            # Comprueba si es una terna pitagórica
            c2 = a**2 + b**2
            if isSquare(c2):
                c = int(c2**0.5)

                # Revisa si la suma es igual a n
                if a+b+c == n:
                    return a*b*c

n = 1000

print(f"El producto de la terna pitagórica que suma {n} es {GetPythProd(n)}")