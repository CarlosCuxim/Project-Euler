/* ================================== Project Euler. Problem #9 ====================================
*
* A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
*
* a^2 + b^2 = c2
*
* For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
*
* There exists exactly one Pythagorean triplet for which a + b + c = 1000.
* Find the product abc.
*
* ----------------------------------------------------------------------------------------------- */

#include <iostream>
using namespace std;

bool isPythTri(int, int, int);

int main()
{
    int a,b,c, P=1;

    for(a=0; a<=1000; ++a){
        for(b=a+1; 2*b<1000-a; ++b){
            c = 1000-(a+b);
            if(isPythTri(a,b,c))
                P = a*b*c;
        }
    }

    cout << "El producto de la única tripleta tal que a + b + c = 1000 es: " << P << endl;

    return 0;
}

bool isPythTri(int a, int b, int c){
    return (a*a + b*b) == c*c;
}