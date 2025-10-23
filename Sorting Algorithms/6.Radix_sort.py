"""
Title: Radix Sort
Contributor: https://github.com/AsparkArcane


Description:
Radix Sort is a non-comparison integer sorting algorithm. It sorts numbers
by processing them digit by digit. It uses a stable sorting algorithm
(like Counting Sort) as a subroutine to sort the numbers based on each
digit, starting from the least significant digit (LSD) and moving to
the most significant digit (MSD).

Example to understand:
Let arr = [170, 45, 75, 90, 802, 24, 2, 66]

1. Sort by 1s place (LSD):
   - Based on (0, 5, 5, 0, 2, 4, 2, 6)
   → [170, 90, 802, 2, 24, 45, 75, 66]

2. Sort by 10s place:
   - Based on (7, 9, 0, 0, 2, 4, 7, 6)
   → [802, 2, 24, 45, 66, 170, 75, 90]

3. Sort by 100s place (MSD):
   - Based on (1, 0, 0, 0, 8, 0, 0, 0) (padding 0s)
   → [2, 24, 45, 66, 75, 90, 170, 802]

Final Array: [2, 24, 45, 66, 75, 90, 170, 802]

Time Complexity Explanation:
- Best Case: O(d * (n + b))
- Average Case: O(d * (n + b))
- Worst Case: O(d * (n + b))
- Where d is the number of digits in the max number,
  n is the number of elements, and b is the base (e.g., 10).
- Space Complexity: O(n + b) — From the underlying stable sort (Counting Sort).

Note: Radix Sort is a **stable** sort (relies on a stable subroutine).
"""

def counting_sort_for_radix(arr, exp):
    """
    A modified Counting Sort to sort elements based on a specific digit.
    'exp' is the exponent (10^i), representing the current digit's place.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Digits 0-9

    # Store count of occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Store cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array (in reverse for stability)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output back to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Performs radix sort (LSD) on a list of non-negative integers.

    Parameters:
    arr (list): List of non-negative integers to sort.

    Returns:
    list: The sorted list (modified in-place).
    """
    if not arr:
        return arr

    # Find the maximum number to know the number of digits
    max_val = max(arr)

    # Do counting sort for every digit.
    # exp is 1 (1s place), 10 (10s place), 100 (100s place), ...
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    
    return arr


# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))  # Output: [2, 24, 45, 66, 75, 90, 170, 802]

"""
Advantages:
1. Faster than comparison sorts (O(n log n)) if d is small and fixed.
2. Stable sorting algorithm.
3. Works well for large integer keys.

Disadvantages:
1. Not in-place, requires O(n+b) extra space.
2. More complex to implement than comparison sorts.
3. Typically only works for integers (or strings).

LeetCode Equivalent:
LeetCode 164 — Maximum Gap
(This problem is often solved using Radix Sort or Bucket Sort)
https://leetcode.com/problems/maximum-gap/
"""