# ================================== Project Euler. Problem #7 =====================================

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# --------------------------------------------------------------------------------------------------

# Función que indica si un número n es primo o no
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

# Devuelve el n-ésimo número primo
def nthPrime(n):
    p = 2
    i = 1
    while i<n:
        p += 1
        if isPrime(p):
            i += 1
    
    return p

n = 10001

print(f"El {n}-ésimo número primo es {nthPrime(n)}")