"""
Title: Insertion Sort
Contributor: https://github.com/Him-an-shi


Description:
Insertion Sort is a simple and intuitive comparison-based sorting algorithm. It builds the final
sorted list one element at a time by comparing each element with the already sorted part and 
placing it in the correct position.

Example to understand:
Let arr = [12, 11, 13, 5, 6]

Step-by-step process:
- Start from the second element (index 1), as the first element is considered sorted.
- Compare the current element with elements in the sorted part and shift elements accordingly.

Initial array: [12, 11, 13, 5, 6]
Step 1: [11, 12, 13, 5, 6]  -> 11 inserted before 12
Step 2: [11, 12, 13, 5, 6]  -> 13 stays as it is
Step 3: [5, 11, 12, 13, 6]  -> 5 inserted at the beginning
Step 4: [5, 6, 11, 12, 13]  -> 6 inserted after 5

Time Complexity Explanation:
- Best Case (Already Sorted): O(n)
- Worst/Average Case: O(n²) — because for every element, it might compare with all previous elements.
- Space Complexity: O(1) — in-place sorting.
"""

def insertion_sort(arr):
    """
    Performs insertion sort on a list of elements.

    Parameters:
    arr (list): List of integers to sort.

    Returns:
    list: Sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be placed at the correct position
        j = i - 1

        # Shift elements of the sorted segment that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Insert key at correct position

    return arr


# Example usage:
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # Output: [5, 6, 11, 12, 13]

"""
Advantages:
1. Simple to implement and understand.
2. Efficient for small or nearly sorted arrays.
3. In-place sorting with O(1) extra space.
4. Stable sorting algorithm (does not change the relative order of equal elements).

Disadvantages:
1. Inefficient for large datasets due to O(n²) time complexity.
2. Not suitable for real-time large-scale applications like Quick Sort or Merge Sort.

LeetCode Equivalent: https://leetcode.com/problems/insertion-sort-list/description/
"""
