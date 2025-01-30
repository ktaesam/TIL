#include <iostream>

int main(void)
{
    // 출력하기
    int num = 20;
    std::cout<<"Hello World!"<<std::endl;
    std::cout<<"Hello "<<"World!"<<std::endl;
    std::cout<<num<<' '<<'A';
    std::cout<<' '<<3.14<<std::endl;

    // 입력하기
    int val1;
    int val2;
    std::cout<<"input 1st val : ";
    std::cin>>val1;

    std::cout<<"input 2nd val : ";
    std::cin>>val2;

    int result = val1 + val2;
    std::cout<<"Sum of val1, val2"<<" is "<<result<<std::endl;
    return 0;
}