/* ================================== Project Euler. Problem #13 ===================================
*Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
*
* 37107287533902102798797998220837590246510135740250
* ...
* 53503534226472524250874054075591789781264330331690
*
* ----------------------------------------------------------------------------------------------- */

#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <cmath>

using namespace std;



long str2int(string numstr, int len){

    long number;
    number = stol(numstr.substr(0, len));

    return number;
}


long cutinteger(long n, int cut){
    int len = log10(n)+1;
    if(len<=cut){
        return n;
    }
    return n/pow(10,len-cut);
}



int main(){

    const int idxlen = 100;

    array<string, idxlen> text;

    // Se guarda el archivo en el array text
    ifstream auxFile("./auxiliar/13.txt");
    string line;
    int i=0;
    while(getline(auxFile, line)){
        text[i] = line;
        i++;
    }
    auxFile.close();


    int len = 15; // necesario para la precisión
    int cut = 10; // limite de dígitos a considerar
    ulong S = 0;


    for(i=0; i<idxlen; i++){
        S += str2int(text[i], len);
    }
    
    cout << cutinteger(S, cut) << endl;
    

    return 0;
}

