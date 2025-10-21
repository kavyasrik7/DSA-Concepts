/*
Title: Factorial of a Number using Recursion
Contributor: https://github.com/fatimaa-dev

Description:
1. The factorial of a number n (written as n!) is the product of all positive integers from 1 to n.
   Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
2. The factorial function can be defined recursively as:
      factorial(n) = n × factorial(n - 1)
3. The base case occurs when n = 0 or n = 1, where factorial(n) = 1.
4. Each function call multiplies n with the factorial of the previous number (n - 1).
*/

#include <iostream>
using namespace std;

// Recursive function to calculate factorial
int factorial(int n) {
    // Base case: factorial of 0 or 1 is 1
    if (n == 0 || n == 1) {
        return 1;
    }

    // Recursive call: factorial(n) = n * factorial(n - 1)
    int result = n * factorial(n - 1);

    // Returning the computed factorial
    cout << "Returning factorial of " << n << " = " << result << endl;
    return result;
}

int main() {
    int n = 5; // Example input
    cout << "Calculating factorial of " << n << ":\n" << endl;

    int fact = factorial(n);
    cout << "\nFinal Result: " << n << "! = " << fact << endl;

    return 0;
}

/*
Example Output:
Calculating factorial of 5:

Calculating: 5 * factorial(4)
Calculating: 4 * factorial(3)
Calculating: 3 * factorial(2)
Calculating: 2 * factorial(1)
Reached base case (n = 1), returning 1
Returning factorial of 2 = 2
Returning factorial of 3 = 6
Returning factorial of 4 = 24
Returning factorial of 5 = 120

Advantages:
1. Simple and clear demonstration of recursive logic.
2. Easy to implement and understand for beginners.

Disadvantages:
1. Can cause stack overflow for very large n due to deep recursion.
2. Slightly slower than iterative method because of multiple function calls.
*/
