# ================================== Project Euler. Problem #5 =====================================

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
# remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# --------------------------------------------------------------------------------------------------

# Función que calcula el mínimo entero divisible por un rango de números de 1 a n
#     La función trabaja de manera recursiva, dado que estamos buscando el mínimo común múltiplo de
#     un conjunto de números, entonces por definición tenemos que mcm(1,...,n-1) | mcm(1,...,n). De
#     esta forma no es necesario comprobar todos los números, sino que basta con calcular los
#     múltiplos de mcm(1,...,n-1). De este modo, primero calculamos el valor de la función en n-1
#     para reducir la búsqueda a múltiplos de este.
def SmallDivisibleByRange(n):
    m = 0
    condition = False

    # Cálculo del múltiplo sobre el cual trabajaremos
    if n == 1:
        step = 1
    else:
        step = SmallDivisibleByRange(n-1)

    while not condition:
        m += step
        condition = True
        
        for i in range(1, n+1):
            condition = condition and (m%i == 0)

    return m

n = 20

print(f"El menor entero divisible por todos los números del 1 al {n} es {SmallDivisibleByRange(n)}")