#include <bits/stdc++.h>
using namespace std;

bool isAnagram(string a, string b) {
    if (a.size() != b.size()) return false;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    return a == b;
}

int main() {
    string a = "listen", b = "silent";
    cout << a << " & " << b << " are anagrams? "
         << (isAnagram(a, b) ? "Yes" : "No");
    return 0;
}
