/* ================================== Project Euler. Problem #15 ===================================
*
* Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
* there are exactly 6 routes to the bottom right corner.
*
* How many such routes are there through a 20x20 grid?
*
* ----------------------------------------------------------------------------------------------- */

#include <iostream>


unsigned long Combination(int n, int k){
    unsigned long C = 1;
    int currentDiv = k;

    for(int i=n; i>n-k; i--){
        C *= i;
        while(currentDiv>1 && C%currentDiv==0){
            C /= currentDiv;
            currentDiv--;
        }
    }
    
    return C;
}

int main(){
    int n = 20;
    int m = 20;

    std::cout << Combination(n+m,n) << std::endl;
    


    return 0;
}