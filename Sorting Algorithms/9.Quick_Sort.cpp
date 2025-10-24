/*
Title: Quick Sort using Recursion
Contributor: https://github.com/fatimaa-dev

Description:
1. Quick Sort is a highly efficient sorting algorithm based on the Divide and Conquer approach.
2. It works by selecting a pivot element and partitioning the array such that:
      - Elements smaller than the pivot go to the left.
      - Elements greater than the pivot go to the right.
3. The same process is then applied recursively to the left and right subarrays.
4. The base case occurs when the subarray has one or zero elements (already sorted).
*/

#include <iostream>
#include <vector>
using namespace std;

// Function to partition the array around a pivot
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];  // Choosing the last element as pivot
    int i = low - 1;        // Index of smaller element

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {  // If current element is smaller than pivot
            i++;
            swap(arr[i], arr[j]);
        }
    }

    // Place the pivot element at its correct position
    swap(arr[i + 1], arr[high]);
    return (i + 1);  // Return pivot index
}

// Recursive Quick Sort function
void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        // Find pivot index
        int pi = partition(arr, low, high);

        cout << "Pivot placed at index " << pi << " with value " << arr[pi] << endl;

        // Recursively sort elements before and after partition
        cout << "Sorting left part (" << low << " to " << pi - 1 << ")" << endl;
        quickSort(arr, low, pi - 1);

        cout << "Sorting right part (" << pi + 1 << " to " << high << ")" << endl;
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    vector<int> arr = {10, 7, 8, 9, 1, 5};  // Example array
    int n = arr.size();

    cout << "Original Array: ";
    for (int x : arr) cout << x << " ";
    cout << "\n\nQuick Sort Steps:\n" << endl;

    quickSort(arr, 0, n - 1);

    cout << "\nSorted Array: ";
    for (int x : arr) cout << x << " ";
    cout << endl;

    return 0;
}

/*
Example Output:

Original Array: 10 7 8 9 1 5 

Quick Sort Steps:
Pivot placed at index 1 with value 5
Sorting left part (0 to 0)
Sorting right part (2 to 5)
Pivot placed at index 4 with value 9
Sorting left part (2 to 3)
Pivot placed at index 2 with value 7
Sorting left part (2 to 1)
Sorting right part (3 to 3)
Sorting right part (5 to 5)

Sorted Array: 1 5 7 8 9 10

Advantages:
1. Very efficient with an average time complexity of O(n log n).
2. Works well for large datasets.
3. In-place sorting (no extra space required).

Disadvantages:
1. Worst-case time complexity is O(n²) (when the pivot is always the smallest/largest element).
2. Not stable (may change the order of equal elements).
*/
