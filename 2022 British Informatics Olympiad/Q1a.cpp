#include <string>
#include <iostream>

using namespace std;

string decrypt (string encrypted) {
    string decrypted('2', encrypted.size());
    for (int i = encrypted.size()-1; i > 0; i--) {
        int new_char = (tolower(encrypted[i]) - 'a' + 1) - (tolower(encrypted[i-1]) - 'a' + 1);
        if (new_char < 0)
            new_char = 26 + new_char;
        char final_char = (new_char % 26) + 'a' - 1;
        encrypted[i] = final_char;
        decrypted[i] = toupper(final_char);
    }
    decrypted[0] = encrypted[0];
    return decrypted;
}

int main () {
    for (int l1 = 0; l1 < 26; l1++) {
        for (int l2 = 0; l2 < 26; l2++) {
            for (int l3 = 0; l3 < 26; l3++) {
                for (int l4 = 0; l4 < 26; l4++) {
                    for (int l5 = 0; l5 < 26; l5++) {
                        string s;
                        s += 'a' + l1;
                        s += 'a' + l2;
                        s += 'a' + l3;
                        s += 'a' + l4;
                        s += 'a' + l5;
                        string d = decrypt(s);
                        string final;
                        for (auto c : d) {
                            if (c != '\u0005')
                                final += c;
                        }
                        if (final == s) {
                            cout << s << endl;
                        }
                    }
                }
            }
        }
    }
}