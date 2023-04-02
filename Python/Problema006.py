# ================================== Project Euler. Problem #6 =====================================

# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square
# of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the
# square of the sum.

# --------------------------------------------------------------------------------------------------


# Suma de 1 hasta n
def SumRange(n):
    S = 0
    for i in range(n+1):
        S += i
    return S

# Suma los cuadrados de 1 hasta n
def SumSquareRange(n):
    S = 0
    for i in range(n+1):
        S += i**2
    return S

n = 100

print(f"""La diferencia entre la suma de los cuadrados y el cuadrado de la suma de
los primeros {n} números naturales es {SumRange(n)**2 - SumSquareRange(n)}""")