"""
Title: Counting Sort
Contributor: https://github.com/AsparkArcane


Description:
Counting Sort is a non-comparison integer sorting algorithm. It operates by
counting the number of objects that have each distinct key value. It then uses
these counts to determine the positions of each element in the sorted output.
It is only suitable for inputs where the range of values (k) is not
significantly larger than the number of elements (n).

Example to understand:
Let arr = [1, 4, 1, 2, 7, 5, 2]

1. Find max value: 7
2. Create count array (size max+1): [0, 0, 0, 0, 0, 0, 0, 0]
3. Store counts of each element:    [0, 2, 2, 0, 1, 1, 0, 1]
   (2 ones, 2 twos, 1 four, 1 five, 1 seven)
4. Store cumulative counts:        [0, 2, 4, 4, 5, 6, 6, 7]
   (Position of last '1' is 2, last '2' is 4, etc.)
5. Build output array (iterating arr in reverse for stability):
   - arr[6]=2: count[2] is 4. Put 2 at output[3]. dec count[2] to 3.
   - arr[5]=5: count[5] is 6. Put 5 at output[5]. dec count[5] to 5.
   - arr[4]=7: count[7] is 7. Put 7 at output[6]. dec count[7] to 6.
   - arr[3]=2: count[2] is 3. Put 2 at output[2]. dec count[2] to 2.
   - arr[2]=1: count[1] is 2. Put 1 at output[1]. dec count[1] to 1.
   - arr[1]=4: count[4] is 5. Put 4 at output[4]. dec count[4] to 4.
   - arr[0]=1: count[1] is 1. Put 1 at output[0]. dec count[1] to 0.

Final Output: [1, 1, 2, 2, 4, 5, 7]

Time Complexity Explanation:
- Best Case: O(n + k)
- Average Case: O(n + k)
- Worst Case: O(n + k)
- Where n is the number of elements and k is the range of input values.
- Space Complexity: O(n + k) — Requires extra space for count and output arrays.

Note: Counting Sort is a **stable** sort (preserves order of equal elements).
"""

def counting_sort(arr):
    """
    Performs counting sort on a list of non-negative integers.

    Parameters:
    arr (list): List of non-negative integers to sort.

    Returns:
    list: The sorted list (modified in-place).
    """
    if not arr:
        return arr

    # 1. Find the maximum element
    max_val = max(arr)

    # 2. Create a count array
    count = [0] * (max_val + 1)

    # 3. Store the count of each element
    for num in arr:
        count[num] += 1

    # 4. Store the cumulative count (for stability)
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # 5. Create an output array
    output = [0] * len(arr)

    # 6. Build the output array
    # Iterate in reverse to maintain stability
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        output[count[num] - 1] = num
        count[num] -= 1

    # 7. Copy the sorted output back to the original array
    for i in range(len(arr)):
        arr[i] = output[i]
    
    return arr


# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1, 0]
print(counting_sort(arr))  # Output: [0, 1, 2, 2, 3, 3, 4, 8]

"""
Advantages:
1. Linear time complexity O(n+k) when k is not too large.
2. Stable sorting algorithm.
3. Simple to implement.

Disadvantages:
1. Not in-place, requires O(n+k) extra space.
2. Only practical for non-negative integers.
3. Inefficient if the range (k) is much larger than n.

LeetCode Equivalent:
LeetCode 75 — Sort Colors
(A classic example where k=3 (colors 0, 1, 2))
https://leetcode.com/problems/sort-colors/
"""