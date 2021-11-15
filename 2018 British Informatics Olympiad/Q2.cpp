/* NOT SOLVED

 revers3ntropy

terminal run command:
    g++ template.cpp -o template -std=c++20 -stdlib=libc++

    Problem N name from Competition Year Round N
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
#define foreach(n) for (auto element : (n))
#define log(s) cout << s << endl;

typedef unsigned long long int ull;
typedef long long int ll;
typedef string str;

double EPS = 1e-9;
int INF_I = 1000000005;
long long INF_LL = 1000000000000000005LL;

#define square(x) ((LL)(x) * (x))

str ALPHABET_L = "abcdefghijklmnopqrstuvwxyz";
str ALPHABET_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
str DIGITS = "0123456789";

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

str generate_cypher (int key) {
    str alphabet = str(ALPHABET_U);

    int idx = 0;
    str out;
    while (!alphabet.empty()) {
        fori (key-1) {
            idx++;
            if (idx >= alphabet.size())
                idx = 0;
        }
        out += alphabet[idx];
        alphabet.erase (alphabet.begin()+idx);
    }

    return out;
}

str encrypt (str cypher, str msg) {
    str out;
    foreach (msg) {
        int idx = ALPHABET_U.find(element);
        out += cypher[idx];

        char first = cypher[0];
        cypher.erase(cypher.begin());
        cypher.push_back(first);
    }
    return out;
}

void solve () {
    vt<str> inp = *split(input());
    int key = stoi(inp[0]);
    str word = inp[1];
    str cypher = generate_cypher(key);
    fori(6) cout << cypher[i];
    cout << endl;
    log(encrypt(cypher, word));
}

int main() {
    solve();
    return 0;
}