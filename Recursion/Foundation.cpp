/*
Title: Sum of Natural Numbers using Recursion
Contributor: https://github.com/fatimaa-dev


Description:
1. This program demonstrates how recursion works by calculating
   the sum of the first 'n' natural numbers.
2. The problem is broken down as:
      sum(n) = n + sum(n - 1)
3. The base case occurs when n = 0, where the sum becomes 0.
4. Each function call is stored on the stack until the base case is reached,
   after which all calls return one by one.
*/

#include <iostream>
using namespace std;

// Recursive function to calculate sum of first n natural numbers
int sumOfNaturalNumbers(int n) {
    // Base case
    if (n == 0) {
        cout << "Reached base case (n = 0)" << endl;
        return 0;
    }

    // Recursive call
    int result = n + sumOfNaturalNumbers(n - 1);

    // Returning the computed sum
    return result;
}

int main() {
    int n = 5; // Example input
    cout << "Calculating sum of first " << n << " natural numbers:\n" << endl;

    int total = sumOfNaturalNumbers(n);
    cout << "\nFinal Sum = " << total << endl;

    return 0;
}

/*
Example Output:
Calculating sum of first 5 natural numbers:

Calculating: 5 + sumOfNaturalNumbers(4)
Calculating: 4 + sumOfNaturalNumbers(3)
Calculating: 3 + sumOfNaturalNumbers(2)
Calculating: 2 + sumOfNaturalNumbers(1)
Calculating: 1 + sumOfNaturalNumbers(0)
Reached base case (n = 0)
Returning sum up to 1 = 1
Returning sum up to 2 = 3
Returning sum up to 3 = 6
Returning sum up to 4 = 10
Returning sum up to 5 = 15

Advantages:
1. Simple and intuitive way to understand recursive flow.
2. Demonstrates how recursive calls build up and return results.

Disadvantages:
1. Less efficient for large n due to multiple function calls.
2. Stack memory usage increases with depth of recursion.
*/
