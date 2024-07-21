// A program that can take a string tokenize it and join the tokens using a hyphen '-'
// Autor: Tesfamichael Tafere

#include <bits/stdc++.h>
using namespace std;

string split_and_join(const string& line) {
    // Create a string stream from the input line : must include the sstream library
    istringstream stream(line);
    vector<string> tokens;
    string token;

    while (getline(stream, token, ' ')) { // we can also use the strtok() method but the stream method is more easier
        tokens.push_back(token);
    }
    string result;
    for (size_t i = 0; i < tokens.size(); ++i) {
        if (i > 0) {
            result += "-";
        }
        result += tokens[i];
    }
    return result;
}

int main() {
    string line = "this is a string";
    string result = split_and_join(line);
    cout << result << endl; // Outputs: this-is-a-string
    return 0;
}
