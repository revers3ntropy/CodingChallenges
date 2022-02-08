/* NOT SOLVED

 revers3ntropy

terminal run command:
    g++ Q2.cpp -o q2 -std=c++20 -stdlib=libc++

    Problem 2 name from Competition Year Round N
    link

        'Description'

  Date

Example Input 1:

Example Output 1:

*/

#include <iostream>
#include <tuple>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

#define fori(n) for (int i = 0; i < (n); i++)
#define forj(m) for (int j = 0; j < (m); j++)
#define foreach(v) for (auto element : (v))
#define log(s) cout << n << endl;

typedef unsigned long long int ull;
typedef long long int ll;
typedef string str;

double EPS = 1e-9;
int INF_I = 1000000005;
long long INF_LL = 1000000000000000005LL;
str ALPHABET_L = "abcdefghijklmnopqrstuvwxyz";
str ALPHABET_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
str DIGITS = "0123456789";

#define square(x) ((LL)(x) * (x))

#define vt vector

std::vector<std::string>* split(str s, const str& delimiter = " ") {
    auto out = new vt<str>();
    size_t pos = 0;
    str token;
    while ((pos = s.find(delimiter)) != std::string::npos) {
        token = s.substr(0, pos);
        out->push_back(token);
        s.erase(0, pos + delimiter.length());
    }
    out->push_back(s);
    return out;
}

str input () {
    str out;
    getline(cin, out);
    return out;
}

vt<int>* str_to_ints (const str& input, const str& c = " ") {
    auto out = new vt<int>();
    foreach (*split(input, c))
    out->push_back(stoi(element));
    return out;
}


// End of template

str solve () {

    str i = input();

    return "";
}

int main() {
    string test_cases_str;
    cin >> test_cases_str;
    int test_cases = stoi(test_cases_str);

    fori (test_cases)
        cout << "Case #" << i+1 << ": " << solve() << endl;

    return 0;
}