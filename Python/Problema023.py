# ================================== Project Euler. Problem #22 ====================================

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the
# number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which
# means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called
# abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
# written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that
# all integers greater than 28123 can be written as the sum of two abundant numbers. However, this
# upper limit cannot be reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant
# numbers.

# --------------------------------------------------------------------------------------------------

from math import floor

Bound = 28123

def d(n):
    S = 1
    for i in range(2,floor(n**0.5)+1):
        if n%i == 0:
            S += i if i == n//i else i + n//i
            
    return S

def isAbundant(n):
    return d(n)>n

def GetListAbundant(n):
    L = []
    print("Calculando: ", end="")
    for i in range(1,n):
        print("\r" + f"Calculando: {i}", end="")
        if isAbundant(i):
            L.append(i)
    print("")
    return L

def isSumOfAbundant(n, L):
    for i in range(len(L)):
        if L[i]>n:
            break
        if n-L[i] in L:
            return True
    return False

def SumNoAbundant(n):
    L = GetListAbundant(n)
    S = 0
    print("Calculando: ", end="")
    for i in range(1, n):
        print("\r" + f"Calculando: {i}", end="")
        if not isSumOfAbundant(i, L):
            S += i
    print("")
    return S

print(f"La suma de los números que no son suma de abundantes debajo de {Bound} es {SumNoAbundant(Bound)}")