/* ================================== Project Euler. Problem #6 ====================================
*
* The sum of the squares of the first ten natural numbers is,
*
* 1^2 + 2^2 + ... + 10^2 = 385
*
* The square of the sum of the first ten natural numbers is,
*
* (1 + 2 + ... + 10)^2 = 3025
*
* Hence the difference between the sum of the squares of the first ten natural numbers and the square
* of the sum is 3025 - 385 = 2640.
*
* Find the difference between the sum of the squares of the first one hundred natural numbers and the
* square of the sum.
*
* ----------------------------------------------------------------------------------------------- */

#include <iostream>

long sumSquare(int n);
long squareSum(int n);

int main()
{
    int n;
    std::cout << "Escriba un número: ";
    std::cin >> n;

    std::cout << "La diferencia entre el cuadrado de la suma y la suma de cuadrados de los primeros "
              << n << " números es " << sumSquare(n) - squareSum(n) << std::endl;
}

long sumSquare(int n){
    long S = 0;
    for(int i=1; i<=n; ++i)
        S += i;

    return S*S;
}

long squareSum(int n){
    long S = 0;
    for(int i=1; i<=n; ++i)
        S += i*i;

    return S;
}