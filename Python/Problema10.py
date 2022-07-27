# ========== Project Euler. Problem #10 =========

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# -----------------------------------------------

# Revisa si algún elemento de la lista lo divide:
def isNotDivisible(n, L):
    for i in L:
        if i>n**0.5:
            break
        if n%i == 0:
            return False
    
    return True

# Criba de Eratóstenes de números menores a n
def Eratosthenes(n):
    if n<2:
        return []
    elif n==2:
        return [2]
    L = [2]
    for i in range(3,n, 2):
        if isNotDivisible(i, L):
            L.append(i)

    return L


# Función que suma los primos menores a n
def sumPrimesLess(n):
    return sum(Eratosthenes(n))


n = 2000000

print(f"La suma de los primos menores a {n} es {sumPrimesLess(n)}")

