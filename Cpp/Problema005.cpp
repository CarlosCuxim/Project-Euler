/*# ========== Project Euler. Problem #5 ==========
*
* 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
* remainder.
*
* What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*
* -----------------------------------------------*/

#include <iostream>

long mcd(long a, long b);
long mcm(long a, long b);

int main(){

    int n = 0;
    long M = 1;
    std::cout << "Escriba un número: ";
    std::cin >> n;

    for(int i=1; i<=n; ++i){
        M = mcm(M, i);
    }
    
    std::cout << "El mínimo común múltiplo de los primeros " << n << " números es "
              << M << std::endl;

    return 0;
}

long mcd(long a, long b){
    long r = a%b;
    if(r==0)
        return b;
    return mcd(b, r);
}

long mcm(long a, long b){
    return (a*b)/mcd(a,b);
}