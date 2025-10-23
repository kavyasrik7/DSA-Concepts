# Question: Count Subsets with Target Sum
#
# You are given an array nums of size n containing positive integers, and a target sum k. Your task is to find the number of ways to select a subset of elements from the array such that the sum of the chosen elements is equal to the target sum k. Since the number of ways can be very large, print it modulo 10^9 + 7.
#
# Input:
# User Task:
# As this is a functional problem, your task is to complete the function findWays() which takes an array nums and an integer k as its input parameters and returns the number of ways to select elements from nums that sum up to k.
#
# Custom Input:
# - The first line contains two integers n and k, representing the size of the array and the target sum.
# - The second line contains n space-separated integers representing the elements of nums.
#
# Output:
# Return a single integer — the number of ways to select elements from the array such that the sum equals k, modulo 10^9 + 7.
#
# Constraints:
# 1 ≤ n ≤ 1000
# 1 ≤ k ≤ 10000
# 0 ≤ nums[i] ≤ 1000
#
# Example:
# Input:
# 4 5
# 1 4 4 5
#
# Output:
# 3
#
# Explanation:
# The possible ways are:
# [1, 4]
# [1, 4] (second 4)
# [5]
#
# Hence, the output is 3.

#Solution:

def findWays(nums, k):
    # Define the modulo value to avoid large numbers
    mod = (10**9) + 7

    memo = {}
    def helper(index, curr):
        # Check if result for this subproblem is already computed
        if (index, curr) in memo:
            return memo[(index, curr)]

        # If current sum exceeds target, no need to proceed
        if curr > k:
            return 0

        # Base case: all elements have been considered
        if index == len(nums):
            # If current sum matches target, count as 1 way
            if curr == k:
                return 1
            else:
                return 0

        # Include the current element in the subset
        include = helper(index + 1, curr + nums[index])

        # Exclude the current element from the subset
        exclude = helper(index + 1, curr)

        # Store the result in memo and take modulo to avoid large numbers
        memo[(index, curr)] = (include + exclude) % mod

        return memo[(index, curr)]

    return helper(0, 0)
