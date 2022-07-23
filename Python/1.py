# ========== Project Euler. Problem #1 ==========

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# -----------------------------------------------




# Función que calcula la suma de los múltiplos de 3 o 5 menores a n
def SumMultiples3or5(n):
    S = 0

    for i in range(1,n):
        if (i%3==0) or (i%5==0):
            S+=i

    return S

n = 1000

print(f"La suma de los múltiplos de 3 o 5 menores a {n} son: {SumMultiples3or5(n)}")