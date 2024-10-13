# Leetcode 53: Maximum Subarray
# Problem List: Blind 75
# Topics: Array, Divide & Conquer, & Dynamic Programming

# Time Complexity: O(N)
# Space Complexity: O(1)

# This is a common problem known as Kadane's Algorithm

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize maxSub to the first element, as at least one element will be part of the subarray
        maxSub = nums[0]
        
        # Initialize curSum to 0, which will keep track of the current subarray sum
        curSum = 0
        
        # Loop through each element in the nums array
        for n in nums:
            # If curSum is negative, it is reset to 0 because a negative sum won't help in maximizing the subarray
            if curSum < 0:
                curSum = 0
                
            # Add the current number to curSum
            curSum +=  n
            
            # Update maxSub if curSum is greater than the previously recorded maxSub
            maxSub = max(maxSub, curSum)
        
        return maxSub
        
        