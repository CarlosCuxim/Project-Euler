/* ========== Project Euler. Problem #7 ==========
*
* By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
*
* What is the 10 001st prime number?
*
* -----------------------------------------------*/

#include <iostream>
#include <cmath>

bool isPrime(long n);

int main()
{
    
    int n, pn=0;
    long i=2, p;
    std::cout << "Escribe un número: ";
    std::cin >> n;

    while(pn<n){
        if(isPrime(i)){
            ++pn;
            p = i;
        }
        ++i;
    }
    
    std::cout << "El " << n << "-ésimo número primo es " << p << std::endl;

    return 0;
}

bool isPrime(long n){
    for(int i=2; i<=sqrt(n); ++i)
        if(n%i==0)
            return false;

    return true;
}