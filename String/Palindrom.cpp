#include <iostream>
using namespace std;

bool isPalindrome(string s) {
    int i = 0, j = s.size() - 1;
    while (i < j) {
        if (s[i] != s[j]) return false;
        i++; j--;
    }
    return true;
}

int main() {
    string s = "madam";
    cout << s << " is palindrome? " << (isPalindrome(s) ? "Yes" : "No");
    return 0;
}
