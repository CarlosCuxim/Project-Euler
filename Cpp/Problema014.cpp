/* ================================== Project Euler. Problem #14 ===================================
*
* The following iterative sequence is defined for the set of positive integers:
* n -> n/2 (n is even)
* n -> 3n+1 (n is odd)
* Using the rule above and starting with 13, we generate the following sequence:
* 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
*
* It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although
* it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
*
* Which starting number, under one million, produces the longest chain?
*
* NOTE: Once the chain starts the terms are allowed to go above one million.
*
* ----------------------------------------------------------------------------------------------- */

#include <iostream>

using namespace std;

long Collatz(long n){
    if(n%2==0){
        return n/2;
    } else {
        return 3*n + 1;
    }
}

long CollatzLen(long n){
    if(n==1){
        return 1;
    } else {
        return CollatzLen(Collatz(n)) + 1;
    }
}


int main(){

    int lim = 1'000'000;
    int longest = 1;
    int longestLen = 1;
    int C;

    for(int i=1; i<lim; i++){
        C = CollatzLen(i);
        if(C>longestLen){
            longestLen = C;
            longest = i;
        }
    }

    cout << longest << endl;

    return 0;
}