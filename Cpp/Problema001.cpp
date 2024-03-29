/* ================================== Project Euler. Problem #1 ====================================
*
* If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
* The sum of these multiples is 23.
*
* Find the sum of all the multiples of 3 or 5 below 1000.
*
* ----------------------------------------------------------------------------------------------- */

#include <iostream>

int main()
{
    int limit = 0, S = 0;
    std::cout << "Escriba un el límite: ";
    std::cin >> limit;

    for(int i=1; i<limit; i++){
        if(i%3==0 || i%5==0){
            S += i;
        }
    }

    std::cout << "La suma del los múltiplos de 3 o 5 menores que " << limit << " es: " << S << std::endl;

    return 0;
}