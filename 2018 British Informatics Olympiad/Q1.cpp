/* NOT SOLVED

 revers3ntropy

terminal run command:
    g++ template.cpp -o template -std=c++20 -stdlib=libc++

    Problem 1 Debt Repayment from British Informatics Olympiad 2018 Round 1
    https://www.olympiad.org.uk/papers/2018/bio/bio18-exam.pdf

        'Output the total amount paid'

  15/11/21

Example Input 1:
10 50

Example Output 1:
116.55
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
    vt<int> i = *str_to_ints(input());
    if (i.size() != 2) return "bad input";
    float interest = ((float)i[0])/100;
    float repayment = ((float)i[1])/100;

    float total_paid = 0;
    float debt = 100.0f;

    while (debt > 0) {
        debt += debt * interest;
        float payed = debt * repayment;
        if (payed < 50) payed = 50;
        if (payed > debt) payed = debt;
        debt -= payed;
        total_paid += payed;
    }

    printf("%.2f", total_paid);
    return "";
}

int main() {
    cout << solve() << endl;
    return 0;
}