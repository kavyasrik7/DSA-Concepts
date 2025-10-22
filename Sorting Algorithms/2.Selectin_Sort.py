"""
Title: Selection Sort
Contributor: https://github.com/Him-an-shi


Description:
Selection Sort is a simple comparison-based sorting algorithm. It works by repeatedly selecting 
the smallest (or largest) element from the unsorted portion of the array and swapping it with 
the first unsorted element, gradually growing the sorted portion.

Example to understand:
Let arr = [64, 25, 12, 22, 11]

Step-by-step process:
Initial array: [64, 25, 12, 22, 11]
Step 1: Find minimum (11) → swap with 64 → [11, 25, 12, 22, 64]
Step 2: Find minimum from remaining (12) → swap with 25 → [11, 12, 25, 22, 64]
Step 3: Find minimum from remaining (22) → swap with 25 → [11, 12, 22, 25, 64]
Step 4: Remaining elements already sorted → Final: [11, 12, 22, 25, 64]

Time Complexity Explanation:
- Best, Average, and Worst Case: O(n²) → because two nested loops always execute.
- Space Complexity: O(1) → in-place sorting.
"""

def selection_sort(arr):
    """
    Performs selection sort on a list of elements.

    Parameters:
    arr (list): List of integers to sort.

    Returns:
    list: Sorted list.
    """
    n = len(arr)

    for i in range(n):
        min_index = i  # Assume current index holds the minimum value

        # Find the index of the minimum element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Example usage:
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # Output: [11, 12, 22, 25, 64]

"""
Advantages:
1. Easy to understand and implement.
2. Makes at most (n-1) swaps — good when swap operation is costly.
3. Works well for small datasets.

Disadvantages:
1. Inefficient for large datasets — O(n²) comparisons.
2. Unstable sort — equal elements might get reordered.
3. Always performs the same number of comparisons regardless of input order.

LeetCode Equivalent Concept:
- Finding kth smallest/largest element-https://leetcode.com/problems/kth-largest-element-in-an-array/description/
- Array manipulation with minimum swaps-https://leetcode.com/problems/smallest-string-with-swaps/description/
"""
