#include <iostream>
using namespace std;

int main(){
    int array[10] = {1,2,3,4,5};

    for (int i = 0; i < 5; i++){
        cout << array[i] << endl;
    }
    cout << array[6] << array[7] << array[8];
    return 0;
}