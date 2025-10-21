#include <stdio.h>

#define MAX 10  // Maximum supported rows/columns for simplicity

/*
 * multiplyMatrices
 * -----------------
 * Multiply two matrices: result = first * second
 *
 * Parameters:
 *  - first:  2D array representing the first matrix (size r1 x c1)
 *  - second: 2D array representing the second matrix (size c1 x c2)
 *  - result: 2D array to store the product (size r1 x c2)
 *  - r1:     number of rows in the first matrix
 *  - c1:     number of columns in the first matrix (and rows in second)
 *  - c2:     number of columns in the second matrix
 *
 * The function assumes c1 == number of rows in 'second'. It initializes the
 * result matrix to 0, then performs the standard triple-loop multiplication.
 */
void multiplyMatrices(int first[MAX][MAX], int second[MAX][MAX], int result[MAX][MAX], int r1, int c1, int c2) {
    // Initialize result matrix elements to 0
    for (int i = 0; i < r1; ++i) {
        for (int j = 0; j < c2; ++j) {
            result[i][j] = 0;
        }
    }

    // Perform multiplication
    // For each cell (i,j) in the result, sum first[i][k] * second[k][j] over k.
    for (int i = 0; i < r1; ++i) {
        for (int j = 0; j < c2; ++j) {
            for (int k = 0; k < c1; ++k) {
                result[i][j] += first[i][k] * second[k][j];
            }
        }
    }
}

/*
 * displayMatrix
 * -------------
 * Print the given matrix to stdout with spaces separating elements and each
 * row on a new line.
 *
 * Parameters:
 *  - matrix: 2D array to display
 *  - row:    number of rows
 *  - col:    number of columns
 */
void displayMatrix(int matrix[MAX][MAX], int row, int col) {
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int first[MAX][MAX], second[MAX][MAX], result[MAX][MAX];
    int r1, c1, r2, c2;

    // Read dimensions for the first matrix
    printf("Enter rows and columns for first matrix: ");
    if (scanf("%d %d", &r1, &c1) != 2) {
        printf("Invalid input for first matrix dimensions.\n");
        return 1;
    }
    if (r1 <= 0 || r1 > MAX || c1 <= 0 || c1 > MAX) {
        printf("Rows/columns must be between 1 and %d.\n", MAX);
        return 1;
    }

    // Read dimensions for the second matrix
    printf("Enter rows and columns for second matrix: ");
    if (scanf("%d %d", &r2, &c2) != 2) {
        printf("Invalid input for second matrix dimensions.\n");
        return 1;
    }
    if (r2 <= 0 || r2 > MAX || c2 <= 0 || c2 > MAX) {
        printf("Rows/columns must be between 1 and %d.\n", MAX);
        return 1;
    }

    // Check if multiplication is possible: number of columns in first == rows in second
    if (c1 != r2) {
        printf("Error! Column of first matrix is not equal to row of second matrix.\n");
        return 0;
    }

    // Input first matrix elements row by row
    printf("Enter elements of first matrix:\n");
    for (int i = 0; i < r1; ++i) {
        for (int j = 0; j < c1; ++j) {
            if (scanf("%d", &first[i][j]) != 1) {
                printf("Invalid input for first matrix elements.\n");
                return 1;
            }
        }
    }

    // Input second matrix elements row by row
    printf("Enter elements of second matrix:\n");
    for (int i = 0; i < r2; ++i) {
        for (int j = 0; j < c2; ++j) {
            if (scanf("%d", &second[i][j]) != 1) {
                printf("Invalid input for second matrix elements.\n");
                return 1;
            }
        }
    }

    // Multiply the two matrices and store the result in 'result'
    multiplyMatrices(first, second, result, r1, c1, c2);

    // Display the product matrix
    printf("\nResultant Matrix:\n");
    displayMatrix(result, r1, c2);

    return 0;
}

/*
Related LeetCode (matrix operations / multiplication examples):
 - 48. Rotate Image
 - 54. Spiral Matrix
 - 73. Set Matrix Zeroes
 - 240. Search a 2D Matrix II
 - 766. Toeplitz Matrix
*/