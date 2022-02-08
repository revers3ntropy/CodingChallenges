/* NOT SOLVED

 revers3ntropy

terminal run command:
    g++ template.cpp -o template -std=c++20 -stdlib=libc++

    Problem 3 Serial Numbers from Competition Year Round N
    https://www.olympiad.org.uk/papers/2018/bio/bio18-exam.pdf

        'Description'

  15/11/21-

Example Input 1:

Example Output 1:

*/

#include <iostream>
#include <tuple>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <utility>
#include <vector>
#include <string>
#include <map>
#include <math.h>

using namespace std;

#define fori(n) for (int i = 0; i < (n); i++)
#define forj(m) for (int j = 0; j < (m); j++)
#define foreach(v) for (auto element : (v))
#define log(s) cout << (s) << endl;
#define log_s(s) cout << to_string(s) << endl;

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

map<str, int> global_mins;

int solve (str inp, vt<str> done_={}) {
    vt<str> done(done_);
    int max_recursion = 0;

    if (global_mins.count(inp)){
        if (done.size() >= global_mins[inp])
            return -1;
        global_mins[inp] = done.size();
    } else
        global_mins[inp] = done.size();

    fori (inp.size()-1) {
        int first = inp[i];
        int last = inp[i+1];

        int min, max;
        if (first > last) {
            max = first;
            min = last;
        } else {
            max = last;
            min = first;
        }

        if (i > 0) {
            int before = inp[i-1];
            if (before > min && before < max) {
                str new_inp = inp;
                swap(new_inp[i], new_inp[i+1]);

                // already done
                if (std::find(done.begin(), done.end(), new_inp) != done.end()) continue;

                done.push_back(inp);
                int res = solve(new_inp, done);
                if (res > max_recursion)
                    max_recursion = res;
                continue;
            }
        }

        if (i <= inp.size()-3) {
            int after = inp[i+2];

            if (after > min && after < max) {
                str new_inp = inp;
                swap(new_inp[i], new_inp[i+1]);

                // already done
                if (std::find(done.begin(), done.end(), new_inp) != done.end()) continue;

                done.push_back(inp);
                int res = solve(new_inp, done);
                if (res > max_recursion)
                    max_recursion = res;
            }
        }
    }

    return max_recursion + 1;
}

int main() {
    input();
    log_s(solve(input()) - 1);
    return 0;
}