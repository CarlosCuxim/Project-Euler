# ========== Project Euler. Problem #3 ==========

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# -----------------------------------------------




# Función para obtener el mayor factor primo de un número n
def MaxPrimeFactor(n):
    p = 2
    
    while(n>1):
        if(n%p==0):
            n /= p
        else:
            p += 1
    return p

n = 600851475143

print(f"El mayor factor primo de {n} es {MaxPrimeFactor(n)}")