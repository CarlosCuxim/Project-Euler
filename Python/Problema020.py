# ================================== Project Euler. Problem #20 ====================================

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

# --------------------------------------------------------------------------------------------------

def Factorial(n):
    P = 1
    for i in range(1,n+1):
        P*=i
    return P

def SumDigits(n):
    S = 0
    while n>0:
        S+= n%10
        n=n//10
    return S


n = Factorial(100)

print(f"La suma de los dígitos de 100! es {SumDigits(n)}")