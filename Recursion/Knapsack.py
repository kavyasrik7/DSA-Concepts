# Question: 0/1 Knapsack Problem
#
# You are given n items and two integer arrays:
#
# - weights[] — where weights[i] denotes the weight of the i-th item
# - values[] — where values[i] denotes the value of the i-th item
#
# You are also given an integer W representing the maximum weight capacity of a knapsack.
#
# Your goal is to determine the maximum total value you can obtain by selecting a subset of the items such that the total weight does not exceed the capacity W.
#
# Input:
#
# You do not need to handle input reading. You only need to implement the function:
#
# def maxProfit(values: List[int], weights: List[int], W: int) -> int:
# # Your code here
#
# The function parameters are:
#
# - values: List of integers representing values of items
# - weights: List of integers representing weights of items
# - W: Integer representing maximum weight capacity
#
# Custom Input Format (for testing):
#
# 1. First line: Single integer n — number of items
# 2. Second line: n space-separated integers — values of the items
# 3. Third line: n space-separated integers — weights of the items
# 4. Fourth line: Single integer W — maximum weight capacity
#
# Output:
#
# Return a single integer — the maximum value obtainable without exceeding the weight W.
#
# Constraints:
#
# - 1 ≤ n ≤ 50
# - 2 ≤ values[i] ≤ 1000
# - 2 < weights[i] ≤ 100
# - 0 < W ≤ 500
#
# Example:
#
# Input:
# 4
# 10 40 30 50
# 5 2 6 3
# 5
#
# Output:
# 90
#
# Explanation:
#
# - For item 0: weight = 5, value = 10
# - For items 1 + 3: total weight = 2 + 3 = 5, total value = 40 + 50 = 90
# - Therefore, the maximum value = 90

#Solution:

def maxWeight(weights, values, W):
    # Memoization dictionary to store results for subproblems
    memo = {}


    def helper(weights, values, W, index):
        # If we've considered all items or the knapsack is full, return 0
        if index == len(weights) or W == 0:
            return 0

        # If this subproblem has been solved before, return the stored result
        if (W, index) in memo:
            return memo[(W, index)]

        # Option 1: Pick the current item (if it fits in the remaining capacity)
        pick = 0
        if W >= weights[index]:
            pick = values[index] + helper(weights, values, W - weights[index], index + 1)

        # Option 2: Do not pick the current item
        notpick = helper(weights, values, W, index + 1)

        # Store the maximum of picking or not picking the current item
        memo[(W, index)] = max(pick, notpick)

        return memo[(W, index)]

    # Start the recursion from index 0 with full capacity W
    return helper(weights, values, W, 0)

