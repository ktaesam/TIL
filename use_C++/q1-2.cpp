#include <iostream>

void swap(int * a, int * b){
    int temp = *a;
    //std::cout<<"a "<<a<<" b "<<b<<std::endl;
    *a = *b;
    *b = temp;
    //std::cout<<"a "<<a<<" b "<<b<<std::endl;
}

void swap(char * a, char * b){
    char temp = *a;
    *a = *b;
    *b = temp;
}

void swap(double * a, double * b){
    double temp = *a;
    *a = *b;
    *b = temp;
}

int main(void){
    int num1 = 20, num2 = 30;
    swap(&num1, &num2);
    std::cout<<num1<<" "<<num2<<std::endl;

    char ch1 = 'A', ch2 = 'Z';
    swap(&ch1, &ch2);
    std::cout<<ch1<<" "<<ch2<<std::endl;

    double db1 = 1.111, db2 = 9.999;
    swap(&db1, &db2);
    std::cout<<db1<<" "<<db2<<std::endl;

    return 0;
}