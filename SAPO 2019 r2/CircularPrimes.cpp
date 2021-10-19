/*
Problem A. Circular Primes from the Computer Programming Olympiad (South Africa) SAPO 2015 round 2

'determine the nth circular prime'

18/10/21

Examples:
 5 => 11
 10 => 71
 15 => 131

Wow c++ is annoying. I am trying to use c++ for the
fist time to solve on of these problems, and it is taking me ages to do.
*/
#include <iostream>
#include <list>

using namespace std;

bool isPrime(int n) {
    if (n == 0 || n == 1) {
        return false;
    } else {
        for (int i = 2; i <= n / 2; ++i) {
            if (n % i == 0)
                return false;
        }
    }
    return true;
}

bool isCircularPrime(int n) {
    string str_n = to_string(n);

    if (!isPrime(n))
        return false;

    for (int j = 0; j < str_n.length(); j++) {
        string new_str(n, '0');

        new_str.replace(n-1, 1, to_string(str_n[0]));

        for (int i = 0; i < n-2; i++)
            new_str.replace(i, 1, to_string(str_n[i+1]));

        str_n = new_str;

        int new_int;

        try {
            new_int = stoi(new_str);
        } catch (...) {
            cout << "not a number 2" << endl;
        }

        if (!isPrime(new_int))
            return false;
    }

    return true;
}

int main () {
     string in;
     cin >> in;
     int N;
     try {
         N = stoi(in);
     } catch (...) {
         cout << "not a number" << endl;
     }

     list<int> found;

     for (int i = 2; found.size() < N; i++) {
         if (isPrime(i))
             cout << "prime: " << to_string(i);
         if (isCircularPrime(i)) {
             found.push_back(i);
         }
     }

     cout << to_string(found.back());
     cout << "finished";

     return 0;
}
