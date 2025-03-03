#include <iostream>
using namespace std;

// input price
double price_input(){
    double price = 0;
    cout << "What is the bill? ";
    cin >> price;
    return price;
}

// input tip rate
double tip_input(){
    double rate = 0;
    cout << "What is the tip percentage? ";
    cin >> rate;
    return rate;
}

// output tips and total price
void price_output(double price, double rate){
    double tip = price * rate * 0.01;
    double total = price + tip;

    cout << fixed; // 소수점 고정
    cout.precision(2); // 두 자리까지 출력
    cout << "The tip is $" << tip << endl;
    cout << "The total is $" << total << endl;
    cout.unsetf(ios::fixed); // 설정 해제
}

int main(){
    double price = 0;
    double rate = 0;

    price = price_input();
    rate = tip_input();

    price_output(price, rate);

    return 0;
}

