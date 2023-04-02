/* ================================== Project Euler. Problem #10 ===================================
*
* The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
*
* Find the sum of all the primes below two million.
*
* ----------------------------------------------------------------------------------------------- */

#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int);

int main()
{
    int n;
    cout << "Escriba el límite: ";
    cin >> n;

    long S=0;
    for(int i=2; i<n; ++i){
        if(isPrime(i))
            S += i;
    }

    cout << "La suma de los primos menores a " << n << " es " << S << endl;

    return 0;
}

bool isPrime(int n){
    for(int i=2; i<=sqrt(n); ++i){
        if(!(n%i))
            return false;
    }
    return true;
}