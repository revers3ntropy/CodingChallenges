//
// Created by Joseph Coppin on 19/10/2021.
//
#include <iostream>
using namespace std;

int num[] = {1,4,5,9,10,40,50,90,100,400,500,900,1000};
string sym[] = {"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};

string intToRomanNumeral(int number) {
    string out = "";

    int i = 12;
    while (number > 0) {
        int div = number / num[i];
        number = number % num[i];
        while (div--)
            out.insert(0, sym[i]);

        i--;
    }

    return out;
}

int romanNumeralToInt(string numeral) {
    return 0;
}

int main () {
    cout << intToRomanNumeral(7);
    return 0;
}