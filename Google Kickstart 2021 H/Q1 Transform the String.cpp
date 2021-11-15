/*SOLVED

 revers3ntropy

  Problem 1 Transform the String from Google KickStart 2021 Round H
  https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008da461

  'find the minimum number of operations that are required such that each letter in string S after applying the operations, is present in string F'

  14/11/21

  Took me 1hr... did this at 3 in the morning
  Really simple solution in the end that took me about 10 minutes

Example 1:

  input

2
abcd
a
pppp
p

  output

Case #1: 6
Case #2: 0

 Example 2:

  input

3
pqrst
ou
abd
abd
aaaaaaaaaaaaaaab
aceg

  output

Case #1: 9
Case #2: 0
Case #3: 1

*/

#include <iostream>

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