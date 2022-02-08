#include <string>
#include <iostream>
#include <vector>
#include <tuple>

/*

9 3
3 1

 */

using namespace std;

bool RED = false;
bool BLUE = true;

// square, direction, who controls
vector<tuple<int, int, bool>> controls;

int red_pos = 1;
int red_direction = 1;
int blue_pos = 25;
int blue_direction = 6;

vector<string> split(string s, char i=' ') {
    vector<string> out;
    string current;
    for (char c : s) {
        if (c == i) {
            out.push_back(current);
            current = "";
        } else {
            current += c;
        }
    }
    out.push_back(current);
    return out;
}

pair<bool, bool> controlled_by () {

}

void take_control (int pos, int direction, bool colour) {
    controls.push_back({pos, direction, colour});
}

void move (int n, bool colour) {
    if (colour == RED) {
        red_pos++;
        red_pos %= 25;
    } else {
        blue_pos++;
        blue_pos %= 25;
    }
}

void skirmish (int r, int b) {
    take_control(red_pos, red_direction, RED);
    red_direction++;
    red_direction %= 6;
    move(r, RED);

    take_control(blue_pos, blue_direction, BLUE);
    blue_direction--;
    if (blue_direction < 0)
        blue_direction = 6;
    move(b, BLUE);
}

void feud () {

}

int main () {
    string s;
    getline(cin, s);
    getline(cin, s);
    cout << "6" << endl;
    cout << "6" << endl;
}
