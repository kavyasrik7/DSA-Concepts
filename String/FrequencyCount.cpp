#include <bits/stdc++.h>
using namespace std;

int main() {
    string s = "banana";
    unordered_map<char, int> freq;
    for (char c : s) freq[c]++;
    
    cout << "Character Frequencies:\n";
    for (auto &p : freq)
        cout << p.first << " : " << p.second << "\n";
    return 0;
}
