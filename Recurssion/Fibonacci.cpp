/*
Title: Fibonacci Series using Recursion
Contributor: https://github.com/fatimaa-dev

Description:
1. The Fibonacci series is a sequence of numbers where each number 
   is the sum of the two preceding ones.
   Example: 0, 1, 1, 2, 3, 5, 8, 13, ...
2. The recursive formula for Fibonacci is:
      fib(n) = fib(n - 1) + fib(n - 2)
3. The base cases occur when:
      fib(0) = 0
      fib(1) = 1
4. Recursion helps in understanding how each term is built from previous ones.
*/

#include <iostream>
using namespace std;

// Recursive function to find nth Fibonacci number
int fibonacci(int n) {
    // Base cases
    if (n == 0) {
        cout << "fib(0) = 0" << endl;
        return 0;
    }
    if (n == 1) {
        cout << "fib(1) = 1" << endl;
        return 1;
    }

    // Recursive calls
    int result = fibonacci(n - 1) + fibonacci(n - 2);

    // Returning the computed Fibonacci number
    cout << "Returning fib(" << n << ") = " << result << endl;
    return result;
}

int main() {
    int n = 6; // Example input
    cout << "Fibonacci Series up to " << n << " terms:\n" << endl;

    for (int i = 0; i < n; i++) {
        cout << "fib(" << i << ") = " << fibonacci(i) << endl;
    }

    return 0;
}

/*
Example Output:
Fibonacci Series up to 6 terms:

fib(0) = 0
fib(1) = 1
Calculating fib(2) = fib(1) + fib(0)
fib(1) = 1
fib(0) = 0
Returning fib(2) = 1
fib(2) = 1
Calculating fib(3) = fib(2) + fib(1)
Calculating fib(2) = fib(1) + fib(0)
fib(1) = 1
fib(0) = 0
Returning fib(2) = 1
fib(1) = 1
Returning fib(3) = 2
fib(3) = 2
... and so on

Advantages:
1. Simple way to understand recursion and overlapping subproblems.
2. Good demonstration of base and recursive cases.

Disadvantages:
1. Highly inefficient for large n due to repeated calculations (O(2^n)).
2. Better solved using iteration or dynamic programming.
*/
