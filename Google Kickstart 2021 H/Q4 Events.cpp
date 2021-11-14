#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>
#include <math.h>

using namespace std;
using ll = long long int;
using ull = unsigned long long int;

std::vector<std::string>* split(const char *str, char c = ' ') {
    // https://stackoverflow.com/questions/53849/how-do-i-tokenize-a-string-in-c
    auto* result = new vector<std::string>();
    do {
        const char *begin = str;
        while(*str != c && *str)
            str++;
        result->emplace_back(begin, str);
    } while (0 != *str++);
    return result;
}

struct BigNumber {
    ull denominator;
    ll numerator;

    BigNumber () {
        numerator = 0;
        denominator = 1;
    }

    explicit BigNumber (std::string number) {

        std::vector<std::string>* parts = split(number.c_str(), '.');

        if (parts->size() > 2) {
            // has multiple decimal points ==> invalid
            numerator = 0;
            denominator = 0;
        } else if (parts->size() == 1) {
            // is a simple int
            numerator = std::stoi((*parts)[0]);
            denominator = 1;
        } else {
            // has fractional part
            number.erase(std::remove(number.begin(), number.end(), '.'), number.end());
            numerator = std::stoi(number);
            denominator = pow(10, ((*parts)[1].size()));
            simplify();
        }
    }

    BigNumber(ll nu, ull de) :
    numerator(nu), denominator(de) {
        simplify();
    }

    [[nodiscard]] std::string str () const {
        // TODO: make this work to beyond floating point precision
        if (denominator == 0)
            return "Infinity";
        if (denominator == 1)
            return std::to_string(numerator);
        return std::to_string(numerator/denominator);
    }

    void simplify () {
        if (denominator == 0)
            return;

        ull gcd_ = gcd((ull)std::abs(numerator), denominator);
        numerator /= gcd_;
        denominator /= gcd_;
    }

    BigNumber operator + (ll n) {
        if (n == 0) return *this;
        if (n < 0) {
            n *= -1;
            numerator *= -1;
        }
        return {(ll)(numerator + n*denominator), denominator};
    }
    BigNumber operator - (ll n) {
        if (n == 0) return *this;
        if (n < 0) {
            n *= -1;
            numerator *= -1;
        }
        return {(ll)(numerator - n*denominator), denominator};
    }
    BigNumber operator * (ll n) {
        if (n == 0) return {0, 1};
        if (n < 0) {
            n *= -1;
            numerator *= -1;
        }
        return {numerator * n, denominator};
    }
    BigNumber operator / (ll n) {
        if (n == 0) return {0, 0};
        if (n < 0) {
            n *= -1;
            numerator *= -1;
        }
        return {numerator, denominator * n};
    }


    BigNumber operator + (BigNumber n) const {
        return {
            (ll)(numerator * n.denominator + n.numerator * denominator),
            denominator * n.denominator
        };
    }
    BigNumber operator - (BigNumber n) const {
        return {
            (ll)(numerator * n.denominator - n.numerator * denominator),
            denominator * n.denominator
        };
    }
    BigNumber operator * (BigNumber n) const {
        return {
            numerator * n.numerator,
            denominator * n.denominator
        };
    }
    BigNumber operator / (BigNumber n) const {
        return {
            (ll)(numerator * n.denominator),
            denominator * n.numerator
        };
    }
};

class Event {
    Event* parent;
    int prob_not_parent;
    // set prob_if_parent on root event
    int prob_if_parent;

    int prob () {
        if (!parent)
            return prob_if_parent;

        int parent_prob = parent->prob();

    }
};

int solve () {
    int value;

    return value;
}

int main() {
    std::string test_cases_str;
    std::cin >> test_cases_str;
    int test_cases = std::stoi(test_cases_str);

    for (int i = 0; i < test_cases; i++) {
        std::cout << "#" << i << ": " << solve() << std::endl;
    }

}