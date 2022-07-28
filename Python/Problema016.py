# ========== Project Euler. Problem #16 =========

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

# -----------------------------------------------

# Función para obtener la suma de los dígitos de un número n
def SumOfDigits(n, d=10):
    S = 0
    while n>0:
        S += n%d
        n = n//d

    return S


n = 1000

print(f"La suma de los dígitos de 2^{n} es {SumOfDigits(2**n)}")