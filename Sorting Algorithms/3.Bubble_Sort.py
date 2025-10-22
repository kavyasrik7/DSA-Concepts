"""
Title: Bubble Sort
Contributor: https://github.com/Him-an-shi
Issue: #132

Description:
Bubble Sort is the simplest comparison-based sorting algorithm. It repeatedly compares 
adjacent elements and swaps them if they are in the wrong order. This process continues 
until the array becomes fully sorted.

Example to understand:
Let arr = [5, 1, 4, 2, 8]

Pass-by-pass explanation:
Initial array: [5, 1, 4, 2, 8]

Pass 1:
[1, 5, 4, 2, 8]
[1, 4, 5, 2, 8]
[1, 4, 2, 5, 8]
(no swap needed for 8)

Pass 2:
[1, 4, 2, 5, 8]
[1, 2, 4, 5, 8]

Array becomes sorted before all passes complete, but Bubble Sort continues unless optimized.

Time Complexity Explanation:
- Best Case (Already Sorted with optimization): O(n)
- Worst/Average Case: O(n²)
- Space Complexity: O(1) → in-place sorting.
"""

def bubble_sort(arr):
    """
    Performs bubble sort on a list of elements.

    Parameters:
    arr (list): List of integers to sort.

    Returns:
    list: Sorted list.
    """
    n = len(arr)

    for i in range(n):
        swapped = False  # Optimization: stop if no swap occurs in a pass

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, array is sorted
        if not swapped:
            break

    return arr


# Example usage:
arr = [5, 1, 4, 2, 8]
print(bubble_sort(arr))  # Output: [1, 2, 4, 5, 8]

"""
Advantages:
1. Very easy to understand and implement.
2. Can be optimized to stop early if the array becomes sorted.
3. Stable sorting algorithm (preserves order of equal elements).

Disadvantages:
1. Highly inefficient for large datasets — O(n²) time complexity.
2. Performs unnecessary comparisons if optimization is not used.

"""
