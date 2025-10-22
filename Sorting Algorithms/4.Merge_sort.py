"""
Title: Merge Sort
Contributor: https://github.com/Him-an-shi


Description:
Merge Sort is a Divide and Conquer-based sorting algorithm. It works by recursively dividing 
the array into two halves, sorting each half, and then merging them back together in sorted order.

Example to understand:
Let arr = [38, 27, 43, 3, 9, 82, 10]

Divide Phase:
[38, 27, 43, 3, 9, 82, 10]
→ [38, 27, 43, 3] and [9, 82, 10]
→ [38, 27] [43, 3] and [9, 82] [10]
→ [38] [27] [43] [3] [9] [82] [10]

Merge Phase:
[38] + [27] → [27, 38]
[43] + [3] → [3, 43]
[27, 38] + [3, 43] → [3, 27, 38, 43]
[9] + [82] → [9, 82]
[9, 82] + [10] → [9, 10, 82]
[3, 27, 38, 43] + [9, 10, 82] → [3, 9, 10, 27, 38, 43, 82]

Time Complexity Explanation:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n) — always divides the array log(n) times.
- Space Complexity: O(n) — requires extra space for merging.

Note: Merge Sort is a **stable** sort (preserves order of equal elements).
"""

def merge_sort(arr):
    """
    Performs merge sort on a list of elements.

    Parameters:
    arr (list): List of integers to sort.

    Returns:
    list: Sorted list.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index
        left_half = arr[:mid]  # Divide into left half
        right_half = arr[mid:]  # Divide into right half

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Copy the data into original list in sorted order
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was left in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # Output: [3, 9, 10, 27, 38, 43, 82]

"""
Advantages:
1. Consistent time complexity of O(n log n).
2. Stable sorting algorithm.
3. Works well with Linked Lists and large datasets.

Disadvantages:
1. Requires additional memory (O(n)).
2. Recursive calls add overhead, not suitable for small systems with limited stack memory.

LeetCode Equivalent:
LeetCode 148 — Sort List (Linked List version using Merge Sort)
https://leetcode.com/problems/sort-list/description/
"""
