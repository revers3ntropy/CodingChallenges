#include <string>
#include <iostream>

//ESVNMCW

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
    string i;
    cin >> i;
    cout << decrypt(i);
}