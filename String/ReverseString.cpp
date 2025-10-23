#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string s = "Darshan";
    reverse(s.begin(), s.end());
    cout << "Reversed String: " << s;
    return 0;
}
