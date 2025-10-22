"""
Title: Shell Sort
Contributor: https://github.com/AsparkArcane


Description:
Shell Sort is an in-place comparison sort. It is a generalization of
Insertion Sort, which allows the exchange of items that are far apart.
The algorithm starts by sorting pairs of elements far apart (using a 'gap'),
then progressively reduces the gap. The final pass (with gap=1) is a
standard Insertion Sort, but by then the array is "almost sorted",
which is the best-case scenario for Insertion Sort.

Example to understand:
Let arr = [12, 34, 54, 2, 3]

1. Gap = n // 2 = 2
   - Compare/sort sublist at indices (0, 2, 4): [12, 54, 3]
     → Insertion sort on [12, 54, 3] → [3, 12, 54]
     - Array becomes: [3, 34, 12, 2, 54]
   - Compare/sort sublist at indices (1, 3): [34, 2]
     → Insertion sort on [34, 2] → [2, 34]
     - Array becomes: [3, 2, 12, 34, 54]

2. Gap = 2 // 2 = 1
   - Perform standard Insertion Sort on [3, 2, 12, 34, 54]
   - [3, 2] → [2, 3]
   - Array becomes: [2, 3, 12, 34, 54] (already sorted from here)

Final Array: [2, 3, 12, 34, 54]

Time Complexity Explanation:
- Best Case: O(n log n)
- Average Case: O(n (log n)^2) or O(n^(3/2))
- Worst Case: O(n^2)
- The complexity is highly dependent on the gap sequence used.
- Space Complexity: O(1) — It is an in-place sorting algorithm.

Note: Shell Sort is an **unstable** sort (does not preserve order of equal elements).
"""

def shell_sort(arr):
    """
    Performs shell sort on a list of elements.

    Parameters:
    arr (list): List of integers to sort.

    Returns:
    list: The sorted list (modified in-place).
    """
    n = len(arr)
    
    # Start with a large gap, then reduce it
    gap = n // 2

    while gap > 0:
        # Perform a gapped insertion sort for this gap size.
        for i in range(gap, n):
            
            # Save arr[i] and make a hole at position i
            temp = arr[i]

            # Shift earlier gap-sorted elements up
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Put temp (the original arr[i]) in its
            # correct location
            arr[j] = temp
        
        # Reduce the gap
        gap //= 2
    
    return arr


# Example usage:
arr = [12, 34, 54, 2, 3, 22, 11, 90, 1]
print(shell_sort(arr))  # Output: [1, 2, 3, 11, 12, 22, 34, 54, 90]

"""
Advantages:
1. In-place sorting algorithm (O(1) space).
2. Significantly faster than simple Insertion Sort.
3. Efficient for medium-sized lists.

Disadvantages:
1. Not a stable sort.
2. Time complexity is complex to analyze and depends heavily on the gap sequence.
3. Not as fast as O(n log n) sorts (Merge, Heap) for large datasets.

LeetCode Equivalent:
LeetCode 912 — Sort an Array
(Shell Sort is a valid, though not optimal, solution for this problem)
https://leetcode.com/problems/sort-an-array/
"""