/*NOT_SOLVED

revers3ntropy

  Problem 2 Painter from Google Kickstart 2021 Round H
  https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d9a88

  'what is the minimum number of strokes required to paint it'

  Spent so long on this one! I knew that there was an easier solution, but I couldn't quite figure it out;
  I tried to implement a brute force method. Saw the solution and thought 'Obviously!'

  14/11/21

Example 1:

  input
2
9
YYYBBBYYY
6
YYGGBB

  output
Case #1: 3
Case #2: 2

Example 2:
    input
1
5
ROAOR

    output
Case #1: 3

*/

#include <iostream>
#include <vector>

using namespace std;

class Colour {
public:
    bool r;
    bool y;
    bool b;

    bool matches (Colour* c) {
        return c->b == b && c->r == r && c->y == y;
    }
};

bool matches (vector<Colour> c1, vector<Colour> c2) {
    for (int i = 0; i < c1.size(); i++)
        if (!c1[i].matches(&c2[i]))
            return false;
    return true;
}

Colour from_char (char c) {
    switch (c) {
        case 'R': return {1, 0, 0};
        case 'Y': return {0, 1, 0};
        case 'B': return {0, 0, 1};
        case 'O': return {1, 1, 0};
        case 'P': return {1, 0, 1};
        case 'G': return {0, 1, 1};
        case 'A': return {1, 1, 1};
        default: return {1, 0, 0};
    }
}

class Node {
public:
    int start;
    int end;
    Colour colour;
    Node* parent;

    bool valid (vector<Colour> current, const vector<Colour>& target) {
        for (int i = start; i < end; i++) {
            current[i].r = current[i].r || colour.r;
            current[i].y = current[i].y || colour.y;
            current[i].b = current[i].b || colour.b;
        }

        if (matches(current, target))
            return true;
        else {
            if (parent)
                return parent->valid(current, target);
            return false;
        }
    }
};

std::vector<Node> generate_tree(int length, int Q) {
    std::vector<Node> nodes;
    std::vector<Node> root_nodes;
    std::vector<Node> leaf_nodes;

    for (int i = 0; i < length; i++) {
        for (int j = i; j < length-1; j++) {
            for (int c = 0; c < 3; c++) {
                Node node = {i, j, from_char(c == 0 ? 'R' : c == 1 ? 'G' : 'B')};
                nodes.push_back(node);
                leaf_nodes.push_back(node);
            }
        }
    }

    std::function<void(Node, int)> generate_children = [&](Node root, int depth) {
        if (depth >= Q-1) {
            leaf_nodes.push_back(root);
            return;
        }

        for (int i = 0; i < length-1; i++) {
            for (int j = i; j < length-1; j++) {
                for (int c = 0; c < 3; c++) {
                    Node child = {i, j, from_char(c == 0 ? 'R' : c == 1 ? 'G' : 'B')};
                    nodes.push_back(child);
                    generate_children(child, depth+1);
                }
            }
        }
    };

    for (auto node : root_nodes)
        generate_children(node, 0);

    return leaf_nodes;
}

int solve () {
    std::string length_str;
    cin >> length_str;
    std::string target;
    cin >> target;

    std::vector<Colour> new_target = {};

    char current;
    for (auto c : target) {
        if (c != current) {
            current = c;
            new_target.push_back(from_char(c));
        }
    }

    int length = new_target.size();

    if (length < 2)
        return 1;

    int Q = 0;
    while (true) {
        Q++;
        auto leaves = generate_tree(length, Q);

        for (auto leaf : leaves) {
            std::vector<Colour> str;
            str.reserve(length);
            for (int i = 0; i < length; i++) {
                str.push_back({0, 0, 0});
            }
            if (leaf.valid(str, new_target))
                return Q;
        }
    }
}

int main() {
    std::string test_cases_str;
    std::cin >> test_cases_str;
    int test_cases = std::stoi(test_cases_str);

    for (int i = 0; i < test_cases; i++) {
        std::cout << "Case #" << i+1 << ": " << solve() << std::endl;
    }
}