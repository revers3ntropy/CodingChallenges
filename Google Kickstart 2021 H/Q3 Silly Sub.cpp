#include <iostream>


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