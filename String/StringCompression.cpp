#include <bits/stdc++.h>
using namespace std;

string compressString(string s) {
    string ans = "";
    for (int i = 0; i < s.size(); i++) {
        int count = 1;
        while (i + 1 < s.size() && s[i] == s[i + 1]) {
            count++;
            i++;
        }
        ans += s[i];
        ans += to_string(count);
    }
    return ans;
}

int main() {
    string s = "aabbccc";
    cout << "Compressed String: " << compressString(s);
    return 0;
}
