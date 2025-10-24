# Question: House Robber Problem
#
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, which will automatically alert the police if two adjacent houses are robbed on the same night.
#
# Given an integer array nums representing the amount of money in each house, return the maximum amount of money you can rob tonight without alerting the police.
#
# Input:
#
# You do not need to handle input reading. You only need to implement the function:
#
# def rob(nums: List[int]) -> int:
# # Your code here
#
# The function parameter is:
#
# - nums: List of integers representing the money in each house
#
# Custom Input Format (for testing):
#
# 1. First line: Single integer n — the number of houses
# 2. Second line: n space-separated integers — amount of money in each house
#
# Output:
#
# Return a single integer — the maximum amount of money that can be robbed tonight without alerting the police.
#
# Constraints:
#
# - 1 ≤ nums.length ≤ 10^4
# - 0 ≤ nums[i] ≤ 400
#
# Example 1:
#
# Input:
# 5
# 1 2 10 4 0
#
# Output:
# 11
#
# Explanation:
# Possible combination: 1 + 10 + 0 = 11
#
# Example 2:
#
# Input:
# 5
# 2 7 9 3 1
#
# Output:
# 12
#
# Explanation:
# Possible combination: 2 + 9 + 1 = 12


#Solution:

def rob(nums):
    # Dictionary to store results of subproblems for memoization
    memo = {}

    def helper(nums, index):
        # If index is beyond the last house, no money can be robbed
        if index > len(nums) - 1:
            return 0

        # If index is exactly the last house, rob it
        if index == len(nums) - 1:
            return nums[index]

        # If we already computed the result for this index, return it
        if index in memo:
            return memo[index]

        # Option 1: Rob the current house and skip the next one
        robthis = nums[index] + helper(nums, index + 2)

        # Option 2: Skip the current house and consider the next house
        robthat = helper(nums, index + 1)

        # Store the maximum of robbing this house vs skipping it
        memo[index] = max(robthis, robthat)

        # Return the stored result for this index
        return memo[index]

    # Start the recursion from the first house
    return helper(nums, 0)


