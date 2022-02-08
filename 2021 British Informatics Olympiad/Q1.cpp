/* NOT SOLVED

 revers3ntropy

 Joseph Coppin King's Ely Year 12

terminal run command:
    g++ Q1.cpp -o q1 -std=c++20 -stdlib=libc++

    Problem 1 Down Pat from British Informatics Olympiad 2021
    https://www.olympiad.org.uk/papers/2021/bio/bio21-exam.pdf

        Is s1, s2 or s1+s2 a 'pat'?

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

bool isPat(str s);

bool isPatAtIdx (str s, int idx) {
    log(idx);
    str firstHalf = s.substr(0, idx);
    str secondHalf = s.substr(idx);

    int maxRight;
    foreach (secondHalf) {
        if ((int)element > maxRight)
            maxRight = (int)element;
    }

    foreach (firstHalf) {
        if ((int)element > maxRight)
            return false;
    }

    if (!isPat(reverse_string(firstHalf)))
        return false;
    if (!isPat(reverse_string(secondHalf)))
        return false;

    return true;
}

bool isPat (str s) {
    if (s.size() < 2)
        return true;

    for (int i = 1; i <= s.size()-1; i++)
        if (isPatAtIdx(s, i))
            return true;

    return false;
}

void solve () {
    vt<str> i = *split(input());
    str s1 = i[0];
    str s2 = i[1];
    log(isPat(s1) ? "YES" : "NO");
    log(isPat(s2) ? "YES" : "NO");
    log(isPat(s1 + s2) ? "YES" : "NO");
}

int main() {
    solve();
    return 0;
}