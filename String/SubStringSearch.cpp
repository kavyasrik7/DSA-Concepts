#include <iostream>
using namespace std;

int substringSearch(string text, string pattern) {
    int n = text.size(), m = pattern.size();
    for (int i = 0; i <= n - m; i++) {
        int j;
        for (j = 0; j < m; j++)
            if (text[i + j] != pattern[j]) break;
        if (j == m) return i;
    }
    return -1;
}

int main() {
    string text = "hello world", pattern = "world";
    int pos = substringSearch(text, pattern);
    cout << "Pattern found at index: " << pos;
    return 0;
}
