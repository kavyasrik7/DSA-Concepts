"""
Title: Heap Sort
Contributor: https://github.com/AsparkArcane


Description:
Heap Sort is a comparison-based sorting algorithm that uses a Binary Heap
data structure. It works by first building a Max-Heap from the input array.
Then, it repeatedly extracts the maximum element (the root of the heap) and
moves it to the end of the array, gradually building a sorted list from
right to left.

Example to understand:
Let arr = [4, 10, 3, 5, 1]

1. Build Max-Heap:
   The array is rearranged to satisfy the max-heap property (parent > children).
   → [10, 5, 3, 4, 1]

2. Sort Phase (Extract Max):
   - Swap root (10) with last (1): [1, 5, 3, 4, 10]
   - Reduce heap size by 1. Heapify root (1): [5, 4, 3, 1, 10]

   - Swap root (5) with last (1): [1, 4, 3, 5, 10]
   - Reduce heap size by 1. Heapify root (1): [4, 1, 3, 5, 10]

   - Swap root (4) with last (3): [3, 1, 4, 5, 10]
   - Reduce heap size by 1. Heapify root (3): [3, 1, 4, 5, 10]

   - Swap root (3) with last (1): [1, 3, 4, 5, 10]
   - Reduce heap size by 1. Heapify root (1): [1, 3, 4, 5, 10]

   - Final Array: [1, 3, 4, 5, 10]

Time Complexity Explanation:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n) — Building the heap is O(n), and each of the n
  extractions takes O(log n) time.
- Space Complexity: O(1) — It is an in-place sorting algorithm.

Note: Heap Sort is an **unstable** sort (does not preserve order of equal elements).
"""

def heapify(arr, n, i):
    """
    To heapify a subtree rooted at index i.
    n is the size of the heap.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # See if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Performs heap sort on a list of elements.

    Parameters:
    arr (list): List of integers to sort.

    Returns:
    list: The sorted list (modified in-place).
    """
    n = len(arr)

    # 1. Build a max-heap
    # Start from the last non-leaf node and go backwards
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2. One by one extract elements
    for i in range(n - 1, 0, -1):
        # Move current root (max element) to end
        arr[i], arr[0] = arr[0], arr[i]
        
        # Call max heapify on the reduced heap
        heapify(arr, i, 0)
    
    return arr


# Example usage:
arr = [12, 11, 13, 5, 6, 7]
print(heap_sort(arr))  # Output: [5, 6, 7, 11, 12, 13]

"""
Advantages:
1. Consistent time complexity of O(n log n).
2. In-place sorting algorithm (O(1) space).
3. Efficient for large datasets.

Disadvantages:
1. Not a stable sort.
2. Slower on average than a well-implemented Quick Sort.
3. Poor locality of reference (jumps around in memory).

LeetCode Equivalent:
LeetCode 912 — Sort an Array
(Heap Sort is a standard solution for this general problem)
https://leetcode.com/problems/sort-an-array/
"""