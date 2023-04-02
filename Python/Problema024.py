# ================================== Project Euler. Problem #23 ====================================

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
# of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# --------------------------------------------------------------------------------------------------

from math import factorial

def GetPermutation(n, L):
    l = len(L)

    if l == 1: return L

    f = factorial(l-1)
    q = n//f
    r = n%f

    return [L[q]] + GetPermutation(r, L[:q] + L[q+1:])

def ListToInt(L, b=10):
    l = len(L)
    n = 0
    for i in range(l):
        n += L[i]*b**(l-i-1)
    return n

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n = 1000000
P = GetPermutation(n-1, L)
P = ListToInt(P)

print(f"La millonésima permutacion es {P}")