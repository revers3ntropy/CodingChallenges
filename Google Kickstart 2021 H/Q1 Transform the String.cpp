#include <iostream>
#include <tuple>

using namespace std;


int dist (char s, std::string match) {
    int lowest = 30;

    for (auto c : match) {
        int forward = abs(s - c) ;
        if (forward < lowest)
            lowest = forward;

        int round = (c > s ? (('z'+1) - c) + (s - ('a'-1)) : (('z'+1) - s) + (c - ('a'-1)))-1;
        if (round < lowest)
            lowest = round;
    }

    return lowest;
}

int solve () {

    int total = 0;

    std::string S;
    std::cin >> S;
    std::string F;
    std::cin >> F;

    std::string new_S;

    // remove all letters that are already favourites
    for (auto c : S) {
        if (F.find(c) == std::string::npos) {
            new_S.push_back(c);
        }
    }

    for (auto c : S) {
        total += dist(c, F);
    }

    return total;
}

int main() {
    std::string test_cases_str;
    std::cin >> test_cases_str;
    int test_cases = std::stoi(test_cases_str);

    for (int i = 0; i < test_cases; i++) {
        std::cout << "Case #" << i+1 << ": " << solve() << std::endl;
    }
}