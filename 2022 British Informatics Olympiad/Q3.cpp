#include <string>
#include <iostream>
#include <vector>

//cabd 5

using namespace std;

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

vector<string> cars_possible_preferences (string final) {
    vector<string> out;
    int num_cars = final.size();

    for (int i = 0; i < num_cars; i++) {
        int idx = final.find((char)(i + 'a'));

        if (idx == 0) {
            out.emplace_back("A");
            continue;
        }

        string possibilities;

        for (int j = 0; j < idx; j++) {
            if (final[j] < final[idx]) {
                possibilities += ((char)((int)'A' + j));
            }
        }

        possibilities += (char)((int)'A' + idx);

        out.emplace_back(possibilities);
    }

    return out;
}

string ith_preference_list (vector<string> possible_preferences, int n) {
    string out;

    int num_cars = possible_preferences.size();

    vector<int> current_idxs;
    current_idxs.reserve(num_cars);
    for (int z = 0; z < num_cars; z++) current_idxs.push_back(0);

    int idx = num_cars-1;

    for (int i = 0; i < n-1; i++) {
        current_idxs[idx]++;

        if (current_idxs[idx] >= possible_preferences[idx].size()) {
            current_idxs[idx]--;
            idx--;
            for (int j = idx+1; j < num_cars; j++) {
                current_idxs[j] = 0;
            }
            i--;
        }
    }

    for (int j = 0; j < num_cars; j++) {
        out += possible_preferences[j][current_idxs[j]];
    }

    return out;
}

int main () {
    string out;
    getline(cin, out);
    auto pair = split(out);
    string final = pair[0];
    int n = stoi(pair[1]);

    cout << ith_preference_list(cars_possible_preferences(final), n) << endl;
}