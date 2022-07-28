# ========== Project Euler. Problem #16 =========

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many
# letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23
# letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out
# numbers is in compliance with British usage.

# -----------------------------------------------

# Nombres necesarios
Names = {
    0: "zero",      1: "one",      2: "two",        3: "three",     4: "four",
    5: "five",      6: "six",      7: "seven",      8: "eight",     9: "nine",
    10: "ten",     11: "eleven",  12: "twelve",    13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    20: "twenty",  30: "thirty",  40: "forty",     50: "fifty",    60: "sixty",
    70: "seventy", 80: "eighty",  90: "ninety"
}

# Función que devuelve la forma escrita de un número en inglés
def NumberToLetter(n):
    if n<20:
        return Names[n]

    elif n<100:
        d = n%10
        n = n-d
        pre = "-" + NumberToLetter(d) if d!=0 else ""
        return Names[n] + pre

    elif n<1000:
        d = n%100
        n = n//100
        pre = " and " + NumberToLetter(d) if d!=0 else ""
        return NumberToLetter(n) + " hundred" + pre
    
    elif n<1000000:
        d = n%1000
        n = n//1000
        pre = " " + NumberToLetter(d) if d!=0 else ""
        return NumberToLetter(n) + " thousand" + pre

    elif n<1000000000:
        d = n%1000000
        n = n//1000000
        pre = " " + NumberToLetter(d) if d!=0 else ""
        return NumberToLetter(n) + " million" + pre
    
    elif n == 1000000000:
        return "one billion"

# Cuenta el número de letras de todos los números de 1 a n
def CountLetters(n):
    S = 0
    for i in range(1,n+1):
        S += len(NumberToLetter(i).replace(" ", "").replace("-", ""))
    return S


n = 1000

print(f"El número de letras de los primeros {n} números es {CountLetters(n)}")