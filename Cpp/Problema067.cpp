#include <iostream>
#include <fstream>
#include <string>
#include <array>

const size_t len = 100;


void putString2array(std::string line, std::array<int,len> &list){
    char sep = ' ';
    std::string auxstr = "";
    size_t cidx = 0;

    for(int i=0; i<line.size(); i++){
        if(line[i]==sep){
            list[cidx] = std::stoi(auxstr);
            auxstr = "";
            cidx++;
        } else {
            auxstr += line[i];
        }
        
        if(i+1==line.size()){
            list[cidx] = std::stoi(auxstr);
        }
    }
}

void bestRoute(std::array<std::array<int,len>,len> &M){
    for(int i=len-2; i>=0; i--){
        for(int j=0; j<=i; j++){
            int left = M[i+1][j];
            int right = M[i+1][j+1];
            M[i][j] += (left>right) ? left : right;
        }
    }
}


int main(){

    std::array<std::array<int, len>, len> M = {0};

    
    std::ifstream auxFile("./auxiliar/67.txt");
    std::string line;
    size_t i=0;
    while(std::getline(auxFile,line)){
        putString2array(line, M[i]);
        i++;
    }
    auxFile.close();

    bestRoute(M);

    std::cout << M[0][0] << std::endl;

    
    

    return 0;
}