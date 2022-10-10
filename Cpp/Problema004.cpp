/* ========== Project Euler. Problem #4 ==========
*
* A palindromic number reads the same both ways. The largest palindrome made from the product
* of two 2-digit numbers is 9009 = 91 × 99.
*
* Find the largest palindrome made from the product of two 3-digit numbers.
*
* -----------------------------------------------*/

#include <iostream>
#include <cmath>

int numDigits(int n);
int reverseNum(int n);
bool isPalindrome(int n);

int main()
{

    int n, pmax = 0;

    for(int i=100; i<=999; ++i)
        for(int j=100; j<=999; ++j){
            n = j*i;
            if(pmax<n && isPalindrome(n)){
                pmax = n;
            }
        }

    std::cout << "El mayor palíndromo producto de números de 3 dígitos es "
              << pmax << std::endl;

    return 0;
}

// Función que obtiene el número de dígitos en base 10
int numDigits(int n){
    int num_dig = 1;
    while( n >= pow(10,num_dig) )
        num_dig += 1;
    return num_dig;
}

// Función que me regresa el inverso de un número 1234 -> 4321
int reverseNum(int n){
    int u, d = numDigits(n), reverse = 0;

    while(n>0){
        u = n%10;
        n = n/10;
        reverse += u*pow(10, d-1);
        --d;
    }

    return reverse;
}

// Función que me retorna si un número es un palíndromo
bool isPalindrome(int n){
    return n == reverseNum(n);
}