/* ================================== Project Euler. Problem #15 ===================================
*
* 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
* 
* Whats is the sum of the digits of the number 2^1000?
*
* ----------------------------------------------------------------------------------------------- */

#include <iostream>
#include <vector>
#include <string>


class BigNumber{
    private:
        int defaultBase = 10;
    
    public:
        int base;
        std::vector<int> digitList;



        // Constructor
        BigNumber() : base(this->defaultBase) {
            this->digitList.push_back(0);
        }

        BigNumber(int n){
            this->base = this->defaultBase;
            this->digitList.push_back(n);
            normalize();
        }

        BigNumber(int n, int base){
            this->base = base;
            this->digitList.push_back(n);
            normalize();
        }

        BigNumber(std::vector<int> numberList){
            this->base = this->defaultBase;
            this->digitList = numberList;
            normalize();
        }

        BigNumber(std::vector<int> numberList, int base){
            this->base = base;
            this->digitList = numberList;
            normalize();
        }



        // Métodos
        std::string numberString(){
            std::string numberStr;

            for(int i = this->digitList.size()-1; i>=0; i--){
                numberStr += std::to_string(this->digitList[i]);
            }

            return numberStr;
        }

        void print(){
            for(int i = 0; i<this->digitList.size(); i++){
                std::cout << this->digitList[i] << std::endl;
            }
        }

        void normalize(){
            int i=0;
            while(i<this->digitList.size()){
                int carry = this->digitList[i]/this->base; //Números a llevar
                this->digitList[i] = this->digitList[i]%this->base; // Dígito que resulta

                if(carry!=0){// Agrega carry al la siguiente posición
                    if(i+1==this->digitList.size()){
                        this->digitList.push_back(carry);
                    } else{
                        this->digitList[i+1] += carry;
                    }
                }
                
                i++;
            }
        }



        // Sobrecarga de operadores. Si las bases son diferentes se usará la base del primero
        BigNumber operator+(const BigNumber &other){
            int n = this->digitList.size();
            int m = other.digitList.size();
            int len = (n > m) ? n : m; // El máximo de n y m

            std::vector<int> numberList(len);

            for(int i=0; i<len; i++){
                // Revisa si el indice está fuera del rango
                int a = (i<n) ? this->digitList[i] : 0; 
                int b = (i<m) ? other.digitList[i] : 0; 

                numberList[i] = a+b;
            }

            return BigNumber(numberList, this->base);
        }

        BigNumber operator*(const BigNumber &other){
            int n = this->digitList.size();
            int m = other.digitList.size();
            int len = n+m-1; // El número de dígitos necesarios para el producto

            std::vector<int> numberList(len);

            // El calculo del valor se realiza suponiendo usando el algoritmo del producto de polinomios
            for(int k=0; k<len; k++){
                int c = 0;

                for(int i=0; i<=k; i++){
                    int j = k-i;
                    // Revisa si el indice está fuera del rango
                    int a = (i<n) ? this->digitList[i] : 0; 
                    int b = (j<m) ? other.digitList[j] : 0; 

                    c += a*b;

                }

                numberList[k] = c;
            }

            return BigNumber(numberList, this->base);
        }
};

BigNumber pow(BigNumber n, int p){
    if(p == 0){
        return 1;
    } else {
        return n*pow(n, p-1);
    }
}

long Sum(std::vector<int> list){
    long S = 0;

    for(int i : list){
        S += i;
    }
    return S;
}

int main(){

    BigNumber n = 2;
    n = pow(n, 1000);
    
    int S = Sum(n.digitList);

    std::cout << S << std::endl;

    return 0;
}