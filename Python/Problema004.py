# ================================== Project Euler. Problem #4 =====================================

# A palindromic number reads the same both ways. The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# --------------------------------------------------------------------------------------------------


# Obtiene el número de dígitos de un número n
def NumberOfDigit(n):
    d = 1
    while n > n%10**d:
        d += 1

    return d

# Función para determinar si una función es palindrómica.
#     La función calcula el primer y último dígito, si son iguales entonces de manera recursiva
#     comparará el número al quitar el primer y último dígito.
#     Dado que hay números como 10111 cuya diferencia entre el número de dígitos del original y el
#     número al quitar el primer y último dígito no es exactamente 2, entonces es necesario
#     introducir el número de dígitos manualmente para que la recursividad funcione.
def isPalindromic(n, NumDig=0):
    # Si no hay entrada usará el número de dígitos por defecto
    if(NumDig==0):
        NumDig = NumberOfDigit(n)

    if NumDig == 1:
        return True
    else:
        # Calculo del primer y último dígito
        d1 = n%10
        dm = n//10**(NumDig-1)
        
        if d1 != dm:
            return False
        else:
            # Cálculo del número de en medio
            n = n%10**(NumDig-1)
            n = n//10
            return isPalindromic(n, NumDig-2)


# Función que calcula el número palíndromo máximo que es producto de números de n dígitos
def MaxPalindromeByProduct(n):
    p = 0
    for i in range(10**(n-1), 10**n):
        for j in range(10**(n-1), 10**n):
            m = i*j
            if(isPalindromic(m) and m>p):
                print(f"{i} x {j} = {m}")
                p = m


    return p