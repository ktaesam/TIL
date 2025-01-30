#include <iostream>

int main(void)
{
    // Q1
    int result = 0;
    int num;

    for(int i = 1; i < 6; i++){
        std::cout<<i<<"번째 정수 입력 : ";
        std::cin>>num;

        result += num;
    }
    std::cout<<"합계 :"<<result<<std::endl;

    //Q2
    char name[100];
    char phone[200];

    std::cout<<"이름을 입력하세요 :";
    std::cin>>name;
    std::cout<<"번호를 입력하세요 :";
    std::cin>>phone;

    std::cout<<"이름 : "<<name<<std::endl;
    std::cout<<"번호 : "<<phone<<std::endl;

    //Q3
    int num9;

    std::cout<<"번호를 입력하세요: ";
    std::cin>>num9;

    for(int i = 1; i < 10; i++){
        int result9 = num9 * i;
        std::cout<<num9<<" X "<<i<<" = "<<result9<<std::endl;
    }
    std::cout<<"구구단 끝!\n";

    //Q4
    double add_pri = 0;
    while(add_pri != -1){
        std::cout<<"판매 금액을 만원 단위로 입력: ";
        std::cin>>add_pri;

        double salary = 50 + add_pri * 0.12;
        std::cout<<"급여: "<<salary<<"만원"<<std::endl;
    }
    std::cout<<"급여 계산기 종료"<<std::endl;

    return 0;
}