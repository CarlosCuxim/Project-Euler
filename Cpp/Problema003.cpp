/* ================================== Project Euler. Problem #3 ====================================
*
* The prime factors of 13195 are 5, 7, 13 and 29.
*
* What is the largest prime factor of the number 600851475143 ?
*
* ----------------------------------------------------------------------------------------------- */

#include <iostream>

int main()
{
    // El número que hay que evaluar
    long n, m;
    std::cout << "Escriba un número: ";
    std::cin >> n;

    // Variable que contiene el primo actual y el mayor primo
    int p = 2, pmax;

    // Copia del número
    m = n;
    // Se divide al número con el actual número primo, si no puede dividirse,
    // entonces avanza al siguiente primo
    while(m>1){
        if(m%p==0){
            pmax = p;
            m /= p;
        } else
            p += 1;
    }

    std::cout << "El mayor factor primo de " << n << " es " << pmax << std::endl;

    return 0;
}