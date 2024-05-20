/* ================================== Project Euler. Problem #12 ===================================
*
* The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle
* number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
* 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
*
* Let us list the factors of the first seven triangle numbers:
* 1: 1
* 3: 1, 3
* 6: 1, 2, 3, 6
* 10: 1, 2, 5, 15
* 15: 1, 3, 5, 15
* 21: 1, 3, 7, 21
* 28: 1, 2, 4, 7, 14, 28
*
* We can see that 28 is the first triangle number to have over five divisors.
*
* What is the value of the first triangle number to have over five hundred divisors?
*
* ----------------------------------------------------------------------------------------------- */

#include <iostream>

long triangle(long);
long numberDivisor(long);

int main(){

    int limit = 500;
    long n = 1;
    long divSum = 1;

    while(divSum<limit){
        n++;
        divSum = numberDivisor(triangle(n));
    }
    
    std::cout << "El primer número triangular que tiene más de " << limit  << " divisores es " 
        << triangle(n) << " con " << divSum << " divisores" << std::endl;

    

    return 0;
}

long triangle(long n){
    return (n*(n+1))/2;
}

long numberDivisor(long n){
    
    long S = 0;

    for(long i=1; i*i<=n; i++){
        if(n%i==0){
            if(i*i == n){
                S++;
            } else {
                S += 2;
            }
        }
    }
    return S;
}