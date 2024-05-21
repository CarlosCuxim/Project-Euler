# ================================== Project Euler. Problem #23 ====================================

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# --------------------------------------------------------------------------------------------------

def NumberOfDigits(n, b=10):
    d = 0
    while(n>0):
        n //= b
        d += 1
    return d

def MinFibDig(n):
    Fa = 1
    F = 1
    i = 2

    while NumberOfDigits(F)<n:
        aux = Fa
        Fa = F
        F = Fa + aux
        i += 1

    return i

n = 1000

print(f"El índice del primer número de Fibonacci en contener {n} dígitos es {MinFibDig(n)}")