# 💻 LeetCode 1572: Matrix Diagonal Sum
# Link: https://leetcode.com/problems/matrix-diagonal-sum/
#Contributer: https://github.com/Him-an-shi

# Function to calculate the sum of both diagonals of a square matrix
def diagonalSum(mat):
    # Step 1: Get the size of the matrix (since it's n x n)
    n = len(mat)

    # Step 2: Initialize two variables to keep track of the diagonal sums
    primary_sum = 0      # For elements like mat[0][0], mat[1][1], ...
    secondary_sum = 0    # For elements like mat[0][n-1], mat[1][n-2], ...

    # Step 3: Loop through each row of the matrix
    for i in range(n):
        # Add the element from the primary diagonal
        primary_sum += mat[i][i]

        # Add the element from the secondary diagonal
        secondary_sum += mat[i][n - 1 - i]

    # Step 4: If 'n' is odd, the middle element (center of matrix)
    # is included in both diagonals, so we need to subtract it once.
    if n % 2 == 1:
        middle_index = n // 2
        middle_element = mat[middle_index][middle_index]
        # Subtract the center element because it was counted twice
        return primary_sum + secondary_sum - middle_element

    # Step 5: If matrix size is even, just return the total sum
    return primary_sum + secondary_sum

mat = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

print(diagonalSum(mat))  # Output: 25
