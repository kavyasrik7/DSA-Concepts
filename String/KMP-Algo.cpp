#include <bits/stdc++.h>
using namespace std;

vector<int> buildLPS(string pat) {
    int n = pat.size();
    vector<int> lps(n);
    for (int i = 1, len = 0; i < n;) {
        if (pat[i] == pat[len]) lps[i++] = ++len;
        else if (len) len = lps[len - 1];
        else lps[i++] = 0;
    }
    return lps;
}

int KMPsearch(string text, string pat) {
    vector<int> lps = buildLPS(pat);
    int i = 0, j = 0, n = text.size(), m = pat.size();
    while (i < n) {
        if (text[i] == pat[j]) i++, j++;
        if (j == m) return i - j;
        else if (i < n && text[i] != pat[j]) {
            if (j) j = lps[j - 1];
            else i++;
        }
    }
    return -1;
}

int main() {
    string text = "hello world", pat = "world";
    cout << "Pattern found at index: " << KMPsearch(text, pat);
    return 0;
}
