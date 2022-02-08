/* NOT SOLVED

 revers3ntropy

 Joseph Coppin King's Ely Year 12

terminal run command:
    g++ Q1.cpp -o q1 -std=c++20 -stdlib=libc++

    Problem 1 Down Pat from British Informatics Olympiad 2021
    https://www.olympiad.org.uk/papers/2021/bio/bio21-exam.pdf



  3/12/21

Example Input 1:
DE C
Example Output 1:
NO
YES
YES
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
#define log(s) cout << (s) << endl;

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

str reverse_string (str s) {
    reverse(s.begin(), s.end());
    return s;
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

void solve () {
    str i = input();
}

int main() {
    solve();
    return 0;
}